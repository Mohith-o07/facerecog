import csv  #helps to manipulate and work with csv files
from datetime import datetime

import cv2  #openCV library
import face_recognition   #face_recognition library
import numpy as np

video_capture = cv2.VideoCapture(0)   #captures video from the first camera
person1_image = face_recognition.load_image_file("faces/person1.jpeg")
person1_encoding = face_recognition.face_encodings(person1_image)[0] #facial encooding of first face detected in the image.
person2_image = face_recognition.load_image_file("faces/person2.jpeg")
person2_encoding = face_recognition.face_encodings(person2_image)[0] #facial encooding of first face detected in the image.
known_face_encodings = [person1_encoding, person2_encoding]
known_face_names = ["person1", "person2"]

# List of expected students
students = known_face_names.copy()

face_locations = []
face_encodings = []

# Get the current date and time
now = datetime.now()
current_date = now.strftime("%d-%m-%Y")

f = open(f"{current_date}.csv", "w", newline="")
lnwriter = csv.writer(f)  #a function that's ready to write to a csv file.

# Define a threshold for face distance
face_distance_threshold = 0.5  #mmaximum difference between the two comparable images.

while True:
    _,frame = video_capture.read()  # _->indicates data that can be ignored.
    #print(_)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  #the frame is resized for faster processing.
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB) #the BGR format recorded by cv2 is converted to RGB format since face_recognition is made for rgb format.

    # Recognize faces
    face_locations = face_recognition.face_locations(rgb_small_frame) #returns a list of tuples, where each tuple contains four integers, typically representing the coordinates of a bounding box around the detected face.
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations) #returns a 2D array where each array represents the facial features (or encoding) of a detected face.

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)  #returns an array of boolean values comparing the face_encoding with every known one.
        #print(matches)
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding) #returns a value of the difference between the compared faces.
        #print(face_distance)
        best_match_index = np.argmin(face_distance) #returns the index of minimum value in the array.

        if matches[best_match_index] and face_distance[best_match_index] <= face_distance_threshold:
            name = known_face_names[best_match_index] #getting the matched face name

            # Add the text if a person is present
            if name in known_face_names:  #displaying the person is present in an opencv frame.
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2
                cv2.putText(frame, name + " Present ", bottomLeftCornerOfText, font, fontScale, fontColor, thickness,
                            lineType)

            if name in students:
                students.remove(name) #removing the detected student from the students array. Here we don't remove the student from known_face_names coz the indexes get changed!(check line 50)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time]) #write name and attendance time to the csv file.

    cv2.imshow("Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):  #condition for stopping the program.
        break

video_capture.release()   #stopping opencv from capturing through webcam.
cv2.destroyAllWindows()   #destroying all opencv windows.
f.close()  #closing the file.
