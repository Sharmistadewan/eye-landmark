# eye-landmark
# Face and Eye Detection with Facial Landmarks

## Overview
This project performs real-time face and eye detection using OpenCV and Dlib. It detects faces, extracts facial landmarks, and highlights eyes using both Haar cascade classifiers and Dlib's shape predictor. The system works with live webcam input and visualizes detected features.

## Features
- Detects faces in real-time using Dlib's frontal face detector.
- Uses Haar cascade classifiers to detect eyes within detected faces.
- Utilizes Dlib's 68-point facial landmark predictor to identify facial features.
- Draws bounding boxes around faces and eyes.
- Marks facial landmarks with circles.

## Requirements
Ensure you have the following dependencies installed:

bash
pip install opencv-python dlib


Additionally, download the *shape predictor model* from Dlib and place it in the project directory:

[Download shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

Extract it and place it in the same directory as the script.

## Usage
1. Run the script:

bash
python face_eye_detection.py


2. The webcam will open, and face/eye detection will begin.
3. Press q to exit the application.

## Code Explanation
- *Face Detection:* Dlib's get_frontal_face_detector() detects faces in a grayscale frame.
- *Eye Detection:* OpenCV's Haar cascade classifier detects eyes inside the face region.
- *Facial Landmark Detection:* Dlib's shape predictor extracts 68 facial landmarks.
- *Visualization:* OpenCV is used to draw rectangles around faces/eyes and mark landmarks with circles.

## Potential Improvements
- Replace Haar cascade for eye detection with Dlib's landmark-based approach for better accuracy.
- Implement a more robust deep-learning-based model for face/eye detection.
- Optimize the real-time processing speed for better performance.

## License
This project is open-source and free to use.
