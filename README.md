📸 Face Attendance System

AI-powered facial recognition system for automated attendance tracking.

📝 Overview

This project detects faces using a webcam and automatically marks attendance by matching faces with stored encodings.
Attendance is saved in a CSV file with name + date + time.

🚀 Features
Real-time face detection
Face recognition using encodings
Automatic attendance marking
CSV attendance log
Easy to customize
Uses OpenCV + face_recognition library

🛠️ Tech Stack
Python 3.11
OpenCV (cv2)
face_recognition
NumPy


📂 Project Structure
FACE_ATTENDANCE_SYSTEM/
│── images/              # Training images of students/employees
│── encode.py            # Generates facial encodings
│── attendance.py        # Main attendance script
│── Attendance.csv       # Attendance log file
│── README.md            # Project documentation
│── requirements.txt     # Required Python libraries

🔧 Installation

Clone the repository
git clone https://github.com/AIInnovatorTulsi/FACE_ATTENDANCE_SYSTEM.git


Install dependencies
pip install -r requirements.txt


Add training images inside the images/ folder
(File name = Person Name)

Generate encodings
python encode.py

Run the attendance system
python attendance.py

🎯 How It Works

Load the known face encodings
Detect face from the webcam
Compare with known faces
If matched → mark attendance
Save record in CSV file

📈 Output Example
Name, Date, Time
Tulsi, 2025-11-16, 10:42 AM

🤝 Contribution

Pull requests are welcome! For major changes, please open an issue first.
