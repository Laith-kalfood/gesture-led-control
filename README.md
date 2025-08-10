# 🖐️ Gesture-Based LED Control

## 📌 Project Description

This project uses hand gestures to control the **brightness of an LED** connected to an Arduino.

It reads the **distance between your pinky and thumb**, but only activates when specific fingers are raised on your other hand — ensuring intentional control and avoiding accidental triggers.

---

### 🎮 Gesture Logic

| Raised Fingers (Other Hand) | Function Activated | Output Controlled |
|-----------------------------|--------------------|-------------------|
| ☝️ Index only               | LED brightness     | Analog PWM        |

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

## 🐍 Python Environment Setup
Use Python 3.10, and install the following libraries:

  pip install opencv-python mediapipe numpy math pyfirmata2
  
⚠️ Make sure your webcam/phone is working and your Arduino is connected via USB.

## 🚀 How to Run
1.Connect the Arduino like this:











<img width="648" height="494" alt="image" src="https://github.com/user-attachments/assets/cef56889-bcba-486c-be16-e5f8781cd4e5" />



2.Paste the project code into your Python IDE (e.g. PyCharm)


3.Press Run


4.Raise your index finger to activate LED brightness control


5.Move your pinky and thumb to adjust brightness or angle

## ✅ You're Good to Go!
Once everything is set up, the system will respond to your gestures in real time.
Simple, intuitive, and fun to use!






