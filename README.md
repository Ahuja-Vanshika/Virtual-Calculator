# 🧮 Virtual Calculator using Hand Gesture Recognition

This project is an **AI-powered Virtual Calculator** built using **OpenCV** and **cvzone's HandTrackingModule**.  
It allows users to perform arithmetic operations using **hand gestures** instead of pressing physical keys.  

You can interact with the calculator by showing your **index and middle fingers** — when the distance between them is small, it simulates a virtual button click.  
To **exit the program**, simply press the **`f` key**.

---

## 📸 Interface Preview

![Virtual Calculator Interface](b77516fb-42e3-4048-a1d1-84bc68ee8437.png)

---

## ⚙️ Technologies Used
- Python
- OpenCV
- cvzone
- Mediapipe (used internally by cvzone)

---

## 💡 Features
- Real-time hand tracking via webcam  
- Detects index and middle finger pinch to simulate button clicks  
- Supports operations:
  - `+`, `-`, `*`, `/`, `//`, `%`
- `C` button clears the display  
- `=` button evaluates the entered expression  
- Press **`f`** to exit the program  

---
git clone https://github.com/your-username/virtual-calculator.git
cd virtual-calculator
