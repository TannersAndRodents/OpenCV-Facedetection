"""Script for running the detector with the standard system camera.

Opens a window with found faces marked on the video of the camera when executed as script."""

import cv2
from tools import Detector

# Standard Settings
FACE_CASCADE = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
CAMERA = cv2.VideoCapture(0)
FRAME_COLOR = (255,0,0)   #Format: Blue, Green, Reds
FRAME_STROKE = 3

MESSAGE = "Face found!"
MESSAGE_COLOR = (255,255,255)
MESSAGE_SIZE = 30
MESSAGE_FONT = "Yrsa"


def main():
    """Opens a window with found faces marked on the video of the camera.

    Run when file is executed as python script"""
    detector = Detector()
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

    while True:
        #Main Loop, exits when "q" is pressed.

        ret, frame = CAMERA.read() #ret: Boolean whether the frame could be captured

        faces = detector.detect_cascade(frame, FACE_CASCADE)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x-FRAME_STROKE,y-FRAME_STROKE), 
                (x+w+FRAME_STROKE, y+h+FRAME_STROKE), 
                FRAME_COLOR, FRAME_STROKE)
            cv2.addText(frame, MESSAGE,(x - FRAME_STROKE,y - FRAME_STROKE - 5),
                MESSAGE_FONT,MESSAGE_SIZE, MESSAGE_COLOR)

        if frame is None:
            print('Reading capture failed. Does the Camera work? (frame == None)')
            break

        cv2.imshow('frame', frame)

        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()
