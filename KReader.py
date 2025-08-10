# Libraries setup:
# Sme of the libraries are supported only in 3.10 python
import mediapipe as mp
import cv2
import pyfirmata2 as pf2
import math
import numpy as np

# Arduino setup:
board = pf2.Arduino("COM7") # Check the arduino connected COM using the arduino IDE
lightPin = board.get_pin("d:3:p")

# Mediapipe setup
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hand = mp_hands.Hands(max_num_hands=2)

# Stream from camera number 0 (default cam)
vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

while True:

    success, frame = vid.read()

    if success:
        # Converting BGR to RGB
        RGBFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hand.process(RGBFrame)
        if results.multi_hand_landmarks :

            if len(results.multi_hand_landmarks) == 2 :
                hand2_indexTip = results.multi_hand_landmarks[1].landmark[8]
                hand2_indexTip_y = hand2_indexTip.y

                hand2_MCP = results.multi_hand_landmarks[1].landmark[5]
                hand2_MCP_y = hand2_MCP.y

                if hand2_indexTip_y < hand2_MCP_y:
                    # Pinky finger:
                    pinky_Tip = results.multi_hand_landmarks[0].landmark[20]
                    pinky_y = pinky_Tip.y
                    pinky_x = pinky_Tip.x

                    # Thumb:
                    thumbTip = results.multi_hand_landmarks[0].landmark[4]
                    thumb_y = thumbTip.y
                    thumb_x = thumbTip.x

                    # Calculate the distance:
                    d = math.sqrt(((pinky_x - thumb_x) ** 2) + ((pinky_y - thumb_y) ** 2))
                    val = np.interp(d, [0.027, 0.4], [0, 1])

                    lightPin.write(val)
                    print("Command detected : LED controller :" ,val, "    ", d)

                    # Draw the dots and lines:
                    pinky_x_line = int(pinky_x * frame.shape[1])
                    pinky_y_line = int(pinky_y * frame.shape[0])

                    thumb_x_line = int(thumb_x * frame.shape[1])
                    thumb_y_line = int(thumb_y * frame.shape[0])

                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    cv2.line(frame, (pinky_x_line, pinky_y_line), (thumb_x_line, thumb_y_line), (255, 0, 0), 3)

                else:
                    print("No such command.")
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # If you rise one hand only:
            else:
                print("One hand detected.")
        # No hand at all:
        else:
            print("No hands detected.")
        # Show the video:
        cv2.imshow('K Reader', frame)

        # If you pressed Q, the stream will shutdown.
        if cv2.waitKey(1) & 0xFF == ord('q'): # Select your favorite key instead.
            break

    # If it did not success reading:
    else:
        print("Camera filed to open.")
board.exit()

cv2.destroyAllWindows()
