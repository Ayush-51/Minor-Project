# Smart Attendance System using Face Recognition

This project demonstrates a Smart Attendance System using Face Recognition. The system captures video from the webcam, performs face recognition to identify individuals, and records their attendance in a CSV file.

## Features

- Real-time face recognition using OpenCV and face_recognition library.
- Attendance records are saved in a CSV file for easy management.
- Web interface to view live video feed and download attendance records.
  
## Installation

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

**User Interaction  ** 

![image](https://github.com/Ayush-51/Minor-Project/assets/85790732/fe6a5481-e11e-431e-a44d-90b8fa047a99)

**Explanation**
In this workflow:

1. The user interacts with the web application through a web browser.
2. The user clicks the "Mark Exit Time" button on the web page to indicate that they are leaving the class.
3. The web browser sends a request to the Flask web server.
4. The Flask web server processes the request using the /mark_exit/<roll_number> route and marks the exit time for the student.
5. After marking the exit time, the Flask route triggers the process to save the attendance data to a CSV file.
6. The data processing component processes the attendance data, calculates duration and status, and prepares the data for CSV generation.
7. The CSV generation component formats the attendance data into a CSV-friendly format.
8. The CSV file generation component creates the actual CSV file containing the attendance data.
9. The attendance data is saved in the CSV file, completing the process.

This workflow demonstrates how the data is processed and saved in a CSV file after the user marks their exit time.


**Contributing**

Contributions are welcome! If you have ideas for improvements, please open an issue or submit a pull request.

