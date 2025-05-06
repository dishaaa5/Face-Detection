import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

web = cv2.VideoCapture(0)
while True:
    _ , img = web.read()
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray , 1.1 , 4)
    for (x , y , w , h) in faces:
        cv2.rectangle(img , (x , y) , (x+w , y+h) , (0 , 0 ,255) ,4)

    cv2.imshow("Face Detection" , img)
    if cv2.waitKey(1) & 0xff == 27:
        break

web.release()
cv2.destroyAllWindows()        