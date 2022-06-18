import cv2


# Selecting which Haarcascade to use for face detection
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while(True):

    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
   
        color = (255,0,0)   #!!BGR
        stroke = 3
        cv2.rectangle(frame, (x-stroke,y-stroke), (x+w+stroke, y+h+stroke), color, stroke)
        cv2.addText(frame, "Face found!",(x-stroke,y-stroke-5),"Times",30, (255,255,255))

    if frame is None:
        print('Reading capture failed. Does the Camera work? (frame == None)')
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break