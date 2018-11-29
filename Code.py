"""
the arm will move only with hand closed
if port can not be opened test the ports on linux terminal with :
$ python3 -m serial.tools.list_ports -v
"""

# import libraries
import cv2
import numpy as np
# from serial import Serial

# identify arduino port
# Arduino_Serial = Serial ('/dev/ttyACM0', 9600)

# varaibels
number_of_faces = 2
number_of_closed_hands = 3
number_of_opened_hands = 3
cropped_image = 0
distance_to_see_hand = 180
# open cv calssifires
face_cascade = cv2.CascadeClassifier('/home/omar/Desktop/robot_arm_hand_face_tracking/lbpcascade_frontalface.xml')
open_hand = cv2.CascadeClassifier('//home/omar/Desktop/robot_arm_hand_face_tracking/open_palm.xml')
closed_hand = cv2.CascadeClassifier('/home/omar/Desktop/robot_arm_hand_face_tracking/fist_classifire.xml')

# plug the camera
cap = cv2.VideoCapture(0)

while True:
    # get image feom camera
    ret, image = cap.read()

    if ret is True:
        #  convert image to gray and get face dimension in image
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_img)
        hands_open = open_hand.detectMultiScale(gray_img)
        hands_closed = closed_hand.detectMultiScale(gray_img)
        # print(faces, hands_closed, hands_open)

        # vertical line
        cv2.line(image, pt1=(230, 40), pt2=(230, 450), color=(0, 0, 0), thickness=2)
        # horizontal line
        cv2.line(image, pt1=(10, 250), pt2=(500, 250), color=(0, 0, 0), thickness=2)
        # screen center
        cv2.putText(image, '+', (300, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0),
                    thickness=8)

        # make sure there is faces in the image
        if faces != ():

            # number of faces can be detected in the image
            if len(faces) < number_of_faces:
                for x1, y1, w1, h1 in faces:
                    # print('there is a face ')

                    # make a cropped image tpo decrese the time of processing
                    # cropped_image = np.array(image[ y1-110:y1 + h1+110, x1-110:x1 + w1+110])

                    ptf_1 = (x1, y1)
                    ptf_2 = (x1 + w1, y1 + h1)
                    cv2.rectangle(image, pt1=ptf_1, pt2=ptf_2, color=(0, 255, 0), thickness=2)

                    # distance between two points
                    # print(cv2.norm(np.array(ptf_1), np.array(ptf_2)))

                    # texts besides face
                    cv2.putText(image, 'Person Face', (x1+w1, y1+22), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255),
                                thickness=2)
                    cv2.putText(image, 'Detected', (x1+w1, y1+45), cv2.FONT_HERSHEY_DUPLEX, .9, (255, 255, 255),
                                thickness=2)

                    # number of hands can be detected in the image
                    if hands_closed != ():

                        # number of hands can be detected in the image
                        if len(hands_closed) < number_of_closed_hands:
                            cv2.putText(image, '<<Hand Is Closed>>', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (230, 159, 0),
                                        thickness=2)

                            for x2, y2, w2, h2 in hands_closed:
                                # print(hands_closed)
                                print(x2)

                                ptc_1 = (x2, y2)
                                ptc_2 = (x2 + w2, y2 + h2)

                                # the allowed distance to detect hand
                                hand_distance_from_face = cv2.norm(np.array(ptf_1), np.array((x2 + w2, y2)))

                                if int(hand_distance_from_face) < distance_to_see_hand:
                                    cv2.rectangle(image, pt1=ptc_1, pt2=ptc_2, color=(0, 255, 0), thickness=2)
                                    # print(hand_distance_from_face)

                                    # draw lines between face rectangle and hands raectangle
                                    cv2.line(image, pt1=ptf_1, pt2=(x2 + w2, y2), color=(255, 255, 255), thickness=2)
                                    cv2.line(image, pt1=(x1, y1 + h1), pt2=ptc_2, color=(255, 255, 255), thickness=2)

                                    if y2 < 250:
                                        cv2.arrowedLine(image, pt1=(600, 100), pt2=(600, 30), color=(100, 0, 0),
                                                        thickness=6)
                                        # Arduino_Serial.write(str.encode('1'))

                                    elif y2 > 250:
                                        cv2.arrowedLine(image, pt1=(600, 30), pt2=(600, 100), color=(0, 100, 0),
                                                        thickness=6)
                                        # Arduino_Serial.write(str.encode('2'))

                                    if x2 < 230:
                                        cv2.arrowedLine(image, pt1=(630, 70), pt2=(550, 70), color=(0, 0, 100),
                                                        thickness=6)
                                        # Arduino_Serial.write(str.encode('3'))

                                    elif x2 > 230:
                                        cv2.arrowedLine(image, pt1=(550, 70), pt2=(630, 70), color=(0, 0, 150),
                                                        thickness=6)
                                        # Arduino_Serial.write(str.encode('4'))

                    else:
                        if len(hands_open) < number_of_opened_hands:
                            cv2.putText(image, '<<Hand Is Opend>>', (10, 30), cv2.FONT_HERSHEY_DUPLEX, 1, (230, 159, 0),
                                        thickness=2)

                            for x3, y3, w3, h3 in hands_open:
                                # print('there is a palm')

                                pto_1 = (x3, y3)
                                pto_2 = (x3 + w3, y3 + h3)

                                # the allowed distance to detect hand
                                hand_distance_from_face = cv2.norm(np.array(ptf_1), np.array((x3+w3, y3)))

                                if int(hand_distance_from_face) < distance_to_see_hand:
                                    cv2.rectangle(image, pt1=pto_1, pt2=pto_2, color=(0, 255, 0), thickness=2)
                                    # print(hand_distance_from_face)

                                    # draw lines between face rectangle and hands raectangle
                                    cv2.line(image, pt1=ptf_1, pt2=(x3+w3, y3), color=(255, 255, 255), thickness=2)
                                    cv2.line(image, pt1=(x1, y1 + h1), pt2=pto_2, color=(255, 255, 255), thickness=2)

            else:
                print("there is more than one face in the image ")
        else:
            print("there is no face in the picture")

        # start show the image
        cv2.imshow('show', image)

        # stop the image with s button
        if cv2.waitKey(50) & 255 == ord('s'):
            break

    else:
        print("the returned image is not correct ")

cv2.destroyAllWindows()
