import cv2

open_hand_class = cv2.CascadeClassifier('/home/omar/Desktop/handtracking/open_palm.xml')
fist_class = cv2.CascadeClassifier('/home/omar/Desktop/handtracking/fist_classifire.xml')

cap = cv2.VideoCapture(0)


while True:
    ret, image = cap.read()
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hand = open_hand_class.detectMultiScale(gray_img)
    fist = fist_class.detectMultiScale(gray_img)
    print(fist, hand)

    if fist == ():
        for x, y, w, h in hand:
            pt1 = (x, y)
            pt2 = (x + w, y + h)
            cv2.rectangle(image, pt1, pt2, color=(255, 0, 0), thickness=2)
            cv2.putText(image, 'hand is open ', (x, y), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)

    elif hand == ():
        for xx, yy, ww, hh in fist:
            pt1x = (xx, yy)
            pt2x = (xx + ww, yy + hh)
            cv2.rectangle(image, pt1x, pt2x, color=(0, 0, 255), thickness=2)
            cv2.putText(image, 'hand is closed ', (xx, yy), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 2)

    cv2.imshow("Show", image)

    if cv2.waitKey(30) & 255 == ord('s'):
        break