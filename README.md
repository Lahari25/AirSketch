# AirSketch using ML
A Computer vision project implemented using OpenCV and Mediapipe


Ever wanted to bring your imagination to life by simply waving your finger in the air?

In this project, we'll leverage computer vision techniques using OpenCV to create an interactive drawing application. While Python is preferred for its extensive libraries and straightforward syntax, one can implement this project in any language supported by OpenCV.

Our approach involves detecting and tracking hand landmarks to achieve the desired functionality.

Algorithm

1. Capture Frames: Start by reading video frames and convert them to the HSV color space for easier color detection.
2. Prepare the Canvas: Set up the canvas frame and place the appropriate ink buttons on it.
3. Configure Mediapipe: Adjust the Mediapipe initialization to detect only one hand.
4. Landmark Detection: Pass the RGB frames to the Mediapipe hand detector to identify hand landmarks.
5. Track Coordinates: Record the coordinates of the forefinger and store them in an array for use in subsequent frames (these points will be used for drawing on the canvas).
6. Draw on Canvas: Render the stored points on both the frames and the canvas.
   <br>
Requirements: Ensure that Python 3, NumPy, OpenCV, and Mediapipe are installed on your system.



Requirements: python3 , numpy , opencv, mediapipe.

<img src="https://github.com/Lahari25/AirSketch/blob/main/Screenshot%20Airsketch.png" width="500" height="300">





