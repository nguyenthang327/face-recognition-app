import cv2
import os
import pickle
import face_recognition
import numpy as np
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.imread('Resources/background.png')

# Importing the mode images into a list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# print(len(imgModeList))

#Load the encoding file
print("Loading encode file ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()

encodeListKnown, studentIds = encodeListKnownWithIds
print("Encode File Loaded")

while True:
    success, img = cap.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    imgSize = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgSize = cv2.cvtColor(imgSize, cv2.COLOR_BGR2RGB)

    # Find all the faces and face encodings in the current frame of video
    faceCurFrame = face_recognition.face_locations(imgSize)
    encodeCurFrame = face_recognition.face_encodings(imgSize, faceCurFrame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[1]

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        print("matches", matches)
        print("faceDis", faceDis)

        matchIndex = np.argmin(faceDis)
        
        if matches[matchIndex]:
            # print("Know face detected")
            # print("Student is:", studentIds[matchIndex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)


    # cv2.imshow("Camera", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()