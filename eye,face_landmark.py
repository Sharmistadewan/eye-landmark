import cv2
import dlib

# Load the face detector, shape predictor, and eye cascade
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# Check if eye cascade file is loaded successfully
if eye_cascade.empty():
    print("Error: Unable to load eye cascade file")
    exit()

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector(gray)
    for face in faces:
        # Get the coordinates of the face rectangle
        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()

        # Draw a rectangle around the face
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(gray[y1:y2, x1:x2], scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (ex, ey, ew, eh) in eyes:
            # Draw rectangles around the eyes
            cv2.rectangle(frame, (x1+ex, y1+ey), (x1+ex+ew, y1+ey+eh), (255, 0, 0), 2)

        # Detect facial landmarks
        landmarks = predictor(gray, face)
        for n in range(0, 68):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.circle(frame, (x, y), 4, (255, 0, 0), -1)

    cv2.imshow("Face and Eye Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()