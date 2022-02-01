import cv2
import mediapipe as mp
import time
import handtrackingmod as htm
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector=htm.HandDetector()


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList)!=0:
        if(lmList[8][1]==lmList[4][1] and lmList[8][2]==lmList[4][2]):
            print("1")
            cv2.putText(img, str("Nice"), (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)