import cv2
import os
import shutil

face_cascade = cv2.CascadeClassifier('face_recognition/cascades/data/haarcascade_frontalface_alt2.xml')

def remove_images():
    try:
        shutil.rmtree('face_recognition/images/')
    except Exception as exc:
        print(exc)

def make_face_images(n, owner):
    try:
        os.mkdir('face_recognition/images')
    except Exception as exc:
        print(exc, ' : images')
    if n>0:
        path = 'face_recognition/images/{}/'.format(owner)
        try:
            os.mkdir(path)
        except Exception as exc:
            print(exc)

        cap = cv2.VideoCapture(0)
        iteration = 0
        while True:
            #capture frame by frame
            ret,frame = cap.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=4)
            for (x,y,w,h) in faces:     #width, height
                roi_gray = gray[y:y+h,x:x+w]

                color = (255, 0, 0)  # BGR 0-255
                stroke = 2
                end_cord_x = x + w #width -> coordinates
                end_cord_y = y + h #height
                cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

                if cv2.waitKey(20) and 0xFF == ord('q'):
                    break

                if iteration < n:
                    img_item = path+"image_{}.png".format(iteration)
                    cv2.imwrite(img_item, roi_gray)
                    iteration += 1
                else:
                    cap.release()
                    cv2.destroyAllWindows()
                    return

            #display the face frame
            cv2.imshow('frame',frame)
