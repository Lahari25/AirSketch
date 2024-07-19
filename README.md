# AirSketch using ML
A Computer vision project implemented using OpenCV and Mediapipe


Ever wanted to draw your imagination by just waiving your finger in air. 
We will be using the computer vision techniques of OpenCV to build this project. The preffered language is python due to its exhaustive libraries and easy to use syntax but understanding the basics it can be implemented in any OpenCV supported language.

Here Hand landmarks detection and tracking is used in order to achieve the objective. <br><br>



# Algorithm

1. Start reading the frames and convert the captured frames to HSV colour space.(Easy for colour detection)
2. Prepare the canvas frame and put the respective ink buttons on it.
3. Adjust the values of teh mediapipe intilization to detect one hand only.
4. Detect teh landmarks by passing the RGB frame to the mediapipe hand detector
5. Detect the landmarks, find the forefinger coordinates and keep storing them in the array for successive frames .(Arrays for drawing points on canvas)
6. Finally draw the points stored in array on the frames and canvas .

Requirements: python3 , numpy , opencv, mediapipe installed on your system.

<img src="https://github.com/Lahari25/AirSketch/blob/main/Screenshot%20Airsketch.png" width="950" height="400">





