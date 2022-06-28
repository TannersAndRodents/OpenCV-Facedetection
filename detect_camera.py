"""Script for running the detector with the standard system camera.

Opens a window with found faces marked on the video of the camera"""

import cv2
import detector

# Settings
FACE_CASCADE = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
CAMERA = cv2.VideoCapture(0)
FRAME_COLOR = (255,0,0)   #Format: Blue, Green, Reds
FRAME_STROKE = 3

MESSAGE = "Face found!"
MESSAGE_COLOR = (255,255,255)
MESSAGE_SIZE = 30
MESSAGE_FONT = "Times"


detector = detector.Detector()
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

while True:
    #Main Loop, exits when "q" is pressed.

    ret, frame = CAMERA.read() #ret: Boolean whether the frame could be captured

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector.detect_cascade(gray_frame, FACE_CASCADE)
    print(faces)

    stroke = FRAME_STROKE
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x-FRAME_STROKE,y-FRAME_STROKE), 
            (x+w+FRAME_STROKE, y+h+FRAME_STROKE), 
            FRAME_COLOR, FRAME_STROKE)
        cv2.addText(frame, MESSAGE,(x - FRAME_STROKE,y - FRAME_STROKE - 5),
            MESSAGE_FONT,MESSAGE_SIZE, MESSAGE_COLOR)

    print(str(faces))
    if frame is None:
        print('Reading capture failed. Does the Camera work? (frame == None)')
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break