# ITS PURPOSE WAS TO 
# 1. COUNT num IN scanned_img_num.jpg FOR SELECTING RIGHT FILE FOR OCR READING LATER - ALSO JUST ANOTHER NON-TESTED PROTOTYPE (IDEA)
# 2. ALSO STORE FULL IMAGE OF CAR WITH THE NUMBER PLATE INSTEAD OF JUST THE NUMBER PLATE - ALSO JUST ANOTHER NON-TESTED PROTOTYPE (IDEA)

import cv2
import csv
# Import essential libraries
#import requests
#import numpy as np
#import imutils
#
## Replace the below URL with your own. Make sure to add "/shot.jpg" at last.
#url = "http://192.168.61.137:8080/shot.jpg"

harcascade = r"D:\Visual Studio Code Material\Video_Analysis\vid\haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(1)

cap.set(3, 640) # width
cap.set(4, 480) #height

min_area = 500
count = 0
count1 = 0

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x,y,w,h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
            img_roi = img[y: y+h, x:x+w]
            cv2.imshow("ROI", img_roi)


    
    cv2.imshow("Result", img)


    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("plates/scanned_img_" + str(count) + ".jpg", img_roi)
        cv2.imwrite("full/full_img_" + str(count1) + ".jpg", img)
        cv2.rectangle(img, (0,200), (640,300), (0,255,0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results",img)
        cv2.waitKey(500)
        count += 1
        count1 +=1

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

with open('count_name.csv', mode='a', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([count])
    
cap.release()
cv2.destroyAllWindows()