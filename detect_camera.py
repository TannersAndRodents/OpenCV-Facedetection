import cv2


# Selecting which Haarcascade to use for face detection
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while(True):

    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        #print(x,y,w,h)
        roi_gray = gray[y:y+h, x :x+w]
        roi_color = frame[y:y+h, x:x+w]

    
        color = (255,0,0)   #!!BGR
        stroke = 2
        cv2.rectangle(frame, (x,y), (x+w, y+h), color, stroke)
    
    if frame is None:
        print('Reading capture failed. Does the Camera work? (frame == None)')
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.imshow('frame', frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break