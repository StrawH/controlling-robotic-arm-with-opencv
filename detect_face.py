# import libraries
import cv2

face_cascade = cv2.CascadeClassifier('/home/omar/Desktop/robot_arm_hand_face_tracking/lbpcascade_frontalface.xml')

# define camera index
cap = cv2.VideoCapture(0)

#  start
while True:
    # get image feom camera
    ret, image = cap.read()

    #  convert image to gray and get face dimension in image
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img)
    for x, y, w, h in faces:
        pt1 = (x, y)
        pt2 = (x + w, y + h)
        cv2.rectangle(image, pt1, pt2, color=(255, 0, 0), thickness=2)

    # display the action
    cv2.imshow("omar", image)

    if cv2.waitKey(50) & 255 == ord('s'):
        break