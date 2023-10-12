import cv2
from cvzone.HandTrackingModule import HandDetector

camera = cv2.VideoCapture(0)
detect = HandDetector(maxHands=1)
offset = 20
while True:
    success, img = camera.read()
    hands, img = detect.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgCrop = img[y-offset:y + h+offset, x-offset:x + w+offset]
        cv2.imshow("Track",imgCrop)
    cv2.imshow("video", img)
    cv2.waitKey(1)
