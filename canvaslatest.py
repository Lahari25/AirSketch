import cv2
import numpy as np
import mediapipe as mp
from collections import deque

# Giving different arrays to handle colour points of different colours
bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]
ppoints = [deque(maxlen=1024)]  # Purple points
opoints = [deque(maxlen=1024)]  # Orange points

# These indexes will be used to mark the points in particular arrays of specific colour
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0
purple_index = 0
orange_index = 0

# The kernel to be used for dilation purpose
kernel = np.ones((5, 5), np.uint8)

# Define colors and their corresponding indexes
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255), (128, 0, 128), (255, 165, 0)]
colorIndex = 0

# Here is code for Canvas setup
paintWindow = np.zeros((800, 1640, 3)) + 255  # Adjusted canvas width to 1640
paintWindow = cv2.rectangle(paintWindow, (40, 1), (340, 120), (0, 0, 0), 2)       # Adjusted rectangle width
paintWindow = cv2.rectangle(paintWindow, (360, 1), (660, 120), (255, 0, 0), 2)    # Adjusted rectangle width
paintWindow = cv2.rectangle(paintWindow, (680, 1), (980, 120), (0, 255, 0), 2)    # Adjusted rectangle width
paintWindow = cv2.rectangle(paintWindow, (1000, 1), (1300, 120), (0, 0, 255), 2)  # Adjusted rectangle width
paintWindow = cv2.rectangle(paintWindow, (1320, 1), (1620, 120), (0, 255, 255), 2) # Adjusted rectangle width
paintWindow = cv2.rectangle(paintWindow, (40, 150), (340, 270), (128, 0, 128), 2)  # Purple rectangle
paintWindow = cv2.rectangle(paintWindow, (360, 150), (660, 270), (255, 165, 0), 2) # Orange rectangle

cv2.putText(paintWindow, "CLEAR", (115, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (415, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)   # Adjusted position
cv2.putText(paintWindow, "GREEN", (695, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)  # Adjusted position
cv2.putText(paintWindow, "RED", (1025, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)  # Adjusted position
cv2.putText(paintWindow, "YELLOW", (1355, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA) # Adjusted position
cv2.putText(paintWindow, "PURPLE", (115, 220), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)  # Added
cv2.putText(paintWindow, "SKYBLUE", (430, 220), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)  # Added

cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)

# Initialize mediapipe
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Read each frame from the webcam
    ret, frame = cap.read()

    # Check if the frame is valid
    if not ret:
        print("Error: Failed to capture frame from webcam.")
        break

    x, y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame = cv2.rectangle(frame, (40, 1), (340, 120), (0, 0, 0), 2)      # Adjusted rectangle width
    frame = cv2.rectangle(frame, (360, 1), (660, 120), (255, 0, 0), 2)   # Adjusted rectangle width
    frame = cv2.rectangle(frame, (680, 1), (980, 120), (0, 255, 0), 2)   # Adjusted rectangle width
    frame = cv2.rectangle(frame, (1000, 1), (1300, 120), (0, 0, 255), 2) # Adjusted rectangle width
    frame = cv2.rectangle(frame, (1320, 1), (1620, 120), (0, 255, 255), 2) # Adjusted rectangle width
    frame = cv2.rectangle(frame, (40, 150), (340, 270), (128, 0, 128), 2)  # Purple rectangle
    frame = cv2.rectangle(frame, (360, 150), (660, 270), (255, 165, 0), 2) # Orange rectangle
    cv2.putText(frame, "CLEAR", (115, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (415, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)   # Adjusted position
    cv2.putText(frame, "GREEN", (695, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)  # Adjusted position
    cv2.putText(frame, "RED", (1025, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)  # Adjusted position
    cv2.putText(frame, "YELLOW", (1355, 80), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA) # Adjusted position
    cv2.putText(frame, "PURPLE", (115, 220), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)  # Added
    cv2.putText(frame, "SKYBLUE", (430, 220), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2, cv2.LINE_AA)  # Added

    # Get hand landmark prediction
    result = hands.process(framergb)

    # Post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * 1640)  # Scaling x coordinates to new width
                lmy = int(lm.y * 800)  # Scaling y coordinates to new height

                landmarks.append([lmx, lmy])

            # Drawing landmarks on frames
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
        fore_finger = (landmarks[8][0], landmarks[8][1])
        center = fore_finger
        thumb = (landmarks[4][0], landmarks[4][1])
        cv2.circle(frame, center, 3, (0, 255, 0), -1)
        if (thumb[1] - center[1] < 30):
            bpoints.append(deque(maxlen=512))
            blue_index += 1
            gpoints.append(deque(maxlen=512))
            green_index += 1
            rpoints.append(deque(maxlen=512))
            red_index += 1
            ypoints.append(deque(maxlen=512))
            yellow_index += 1
            ppoints.append(deque(maxlen=512))  # Purple
            purple_index += 1
            opoints.append(deque(maxlen=512))  # Orange
            orange_index += 1
        elif center[1] <= 120:
            if 40 <= center[0] <= 340:  # Clear Button
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]
                ppoints = [deque(maxlen=512)]  # Purple
                opoints = [deque(maxlen=512)]  # Orange

                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0
                purple_index = 0
                orange_index = 0

                paintWindow[122:,:,:] = 255
            elif 360 <= center[0] <= 660:
                colorIndex = 0  # Blue
            elif 680 <= center[0] <= 980:
                colorIndex = 1  # Green
            elif 1000 <= center[0] <= 1300:
                colorIndex = 2  # Red
            elif 1320 <= center[0] <= 1620:
                colorIndex = 3  # Yellow
        elif 150 <= center[1] <= 270:
            if 40 <= center[0] <= 340:  # Purple
                colorIndex = 4
            elif 360 <= center[0] <= 660:  # Orange
                colorIndex = 5
        else:
            if colorIndex == 0:
                bpoints[blue_index].appendleft(center)
            elif colorIndex == 1:
                gpoints[green_index].appendleft(center)
            elif colorIndex == 2:
                rpoints[red_index].appendleft(center)
            elif colorIndex == 3:
                ypoints[yellow_index].appendleft(center)
            elif colorIndex == 4:
                ppoints[purple_index].appendleft(center)
            elif colorIndex == 5:
                opoints[orange_index].appendleft(center)
    # Append the next deques when nothing is detected to avoid messing up
    else:
        bpoints.append(deque(maxlen=512))
        blue_index += 1
        gpoints.append(deque(maxlen=512))
        green_index += 1
        rpoints.append(deque(maxlen=512))
        red_index += 1
        ypoints.append(deque(maxlen=512))
        yellow_index += 1
        ppoints.append(deque(maxlen=512))  # Purple
        purple_index += 1
        opoints.append(deque(maxlen=512))  # sky blue
        orange_index += 1

    # Draw lines of all the colors on the canvas and frame with increased thickness
    points = [bpoints, gpoints, rpoints, ypoints, ppoints, opoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 4)   # Increased thickness
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 4)  # Increased thickness

    cv2.imshow("Output", frame)
    cv2.imshow("Paint", paintWindow)

    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and destroy all active windows
cap.release()
cv2.destroyAllWindows()
