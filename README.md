# 🖐️ Gesture-Based LED & Servo Control

## 📌 Project Description

This project uses hand gestures to control either the **brightness of an LED** or the **angle of a servo motor** connected to an Arduino.

It reads the **distance between your pinky and thumb**, but only activates when specific fingers are raised on your other hand — ensuring intentional control and avoiding accidental triggers.

---

### 🎮 Gesture Logic

| Raised Fingers (Other Hand) | Function Activated | Output Controlled |
|-----------------------------|--------------------|-------------------|
| ☝️ Index only               | LED brightness     | Analog PWM        |
| ✌️ Index + Middle           | Servo control      | Angle (0°–180°)   |

---

## 🔧 Requirements

1. **Arduino board**
2. **Webcam**  
   - If you have a webcam, use it directly.  
   - If not, you can use your phone:
     - **Android** → [DroidCam](https://www.dev47apps.com/)
     - **iOS** → [Reincubate Camo](https://reincubate.com/camo/)
   - Install the app on both your **phone** and your **PC/laptop**, then connect them.

---

## 🛠️ Arduino Setup

1. Open the Arduino IDE
2. Install the **Pyfirmata2** library
3. File → Examples → PyFirmata → StandardFirmata
4. Upload the sketch to your Arduino board

##🐍 Python Environment Setup
Use Python 3.10, and install the following libraries:
  pip install opencv-python mediapipe numpy math pyfirmata2
  
⚠️ Make sure your webcam/phone is working and your Arduino is connected via USB.

##🚀 How to Run
1.Paste the project code into your Python IDE (e.g. PyCharm)
2.Press Run
3.Raise your index finger to activate LED brightness control
4.Raise both index and middle fingers to switch to servo control
5.Move your pinky and thumb to adjust brightness or angle

##✅ You're Good to Go!
Once everything is set up, the system will respond to your gestures in real time.
Simple, intuitive, and fun to use!
