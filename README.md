# Smart Attendance System using Face Recognition

This project demonstrates a Smart Attendance System using Face Recognition. The system captures video from the webcam, performs face recognition to identify individuals, and records their attendance in a CSV file.

**## Features**

- Real-time face recognition using OpenCV and face_recognition library.
- Attendance records are saved in a CSV file for easy management.
- Web interface to view live video feed and download attendance records.
**
## Installation**

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/face-recognition-attendance.git

1. Install the required Python packages:
pip install flask opencv-python face_recognition pandas

2. Download the face encodings file and place it in the project directory.

**Usage**

1. Run the application:
python app.py
2. Open a web browser and go to http://localhost:5000 to access the web interface.
3. Click on "Start" to view the live video feed and see real-time face recognition.
4. Click on "Start" to view the live video feed and see real-time face recognition.

**Project Structure**

app.py: The main Flask application file.
1. templates/: HTML templates for rendering the web pages.
2. static/: Static files (CSS, images, etc.).
3. encodings.npz: Pre-trained face encodings file.
4. README.md: This documentation.

**Contributing**

Contributions are welcome! If you have ideas for improvements, please open an issue or submit a pull request.

