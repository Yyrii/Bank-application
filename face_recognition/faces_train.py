import os
from PIL import Image
import numpy as np
import cv2
import pickle


face_cascade = cv2.CascadeClassifier('face_recognition/cascades/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

def train():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, "images")

    current_face_id = 0
    labels_ids = {}
    x_train = []
    y_labels = []

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                label = os.path.basename(root).replace(" ", "-").lower()

                if not label in labels_ids:
                    labels_ids[label] = current_face_id
                    current_face_id += 1

                id_ = labels_ids[label]

                pil_image = Image.open(path).convert("L")  # grayscale
                size = (550, 550)
                final_image = pil_image.resize(size, Image.ANTIALIAS)
                image_array = np.array(final_image, "uint8")

                faces = face_cascade.detectMultiScale(image_array,scaleFactor=1.5,minNeighbors=2)

                for (x,y,w,h) in faces:
                    roi = image_array[y:y+h,x:x+w]
                    x_train.append(roi)
                    y_labels.append(id_)


    try:
        os.mkdir('face_recognition/pickles/')
    except Exception as exc:
        print(exc)

    with open("face_recognition/pickles/face-labels.pickle", 'wb') as f:
        pickle.dump(labels_ids, f)

    recognizer.train(x_train,np.array(y_labels))
    recognizer.save("face_recognition/trainer.yml")
