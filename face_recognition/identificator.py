import numpy as np
import cv2
import pickle


def approvation(results_dic,iterations):
    inverse = [(val, name) for name, val in results_dic.items()]
    if max(inverse)[0] > int((2/3)*iterations):
        return max(inverse)[1]
    else:
        return False

face_cascade = cv2.CascadeClassifier('face_recognition/cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()


def identificate():
    with open("face_recognition/pickles/face-labels.pickle", 'rb') as f:
        og_labels = pickle.load(f)
        labels = {v: k for k, v in og_labels.items()}

    recognizer.read("face_recognition/trainer.yml")
    results = {}

    cap = cv2.VideoCapture(0)
    iteration = 0
    while True:
        #capture frame by frame
        ret,frame = cap.read()

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=4)
        for (x,y,w,h) in faces:     #width, height
            roi_gray = gray[y:y+h,x:x+w]
            roi_color = frame[y:y + h, x:x + w]
            #recognition part
            id_,conf = recognizer.predict(roi_gray)
            if conf >4 and conf <85:# and conf <99:
                try:
                    if labels[id_]:
                        results[labels[id_]] +=1
                except:
                    results[labels[id_]] = 0

                iteration += 1
                if iteration >= 20:
                    cap.release()
                    cv2.destroyAllWindows()
                    return approvation(results,iteration).split('_')


            color = (255, 0, 0)  # BGR 0-255
            stroke = 2
            end_cord_x = x + w #width -> coordinates
            end_cord_y = y + h #height
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

        #display the results frame
        cv2.imshow('frame',frame)

        if cv2.waitKey(20) and 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


