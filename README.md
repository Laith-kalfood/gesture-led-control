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
1.Paste the project code into your Python IDE (e.g. PyCharm)
2.Press Run
3.Raise your index finger to activate LED brightness control
4.Move your pinky and thumb to adjust brightness or angle

## ✅ You're Good to Go!
Once everything is set up, the system will respond to your gestures in real time.
Simple, intuitive, and fun to use!

---

## 📄 License

developed by Laith-kalfood


This project is licensed under the **GNU General Public License v3.0**:
> ⚠️ This project is intended for educational and non-commercial use only.  
> For commercial licensing, please contact the author.
> 
> This program is free software: you can redistribute it and/or modify  
> it under the terms of the GNU General Public License as published by  
> the Free Software Foundation, either version 3 of the License.  
>  
> This program is distributed in the hope that it will be useful,  
> but WITHOUT ANY WARRANTY; without even the implied warranty of  
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Any commercial use requires **explicit permission** from the author.

