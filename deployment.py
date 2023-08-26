from flask import Flask, render_template, Response, send_file
import cv2
import face_recognition
import numpy as np
import datetime
import pandas as pd
from io import BytesIO

app = Flask(__name__)

# Load the encodings and names from the saved file
encodings_file = np.load("encodings.npz")
known_encodings = encodings_file["encodings"]
known_names = encodings_file["names"]

video = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
attendance = {}  # Use a dictionary to store entry, exit times, duration, and status

# Dictionary mapping roll numbers to names
roll_to_name = {
    "2029051": "Ayush Das",
    "2029041": "Babloo Singh",
    "2029050": "Avantika Giri",
    # Add more roll numbers and corresponding names
}

def generate_frames():
    while True:
        ret, frame = video.read()
        if not ret:
            break
        
        # Perform face recognition and update attendance
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
        roll_numbers = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            roll_number = "Unknown"
            
            if True in matches:
                matched_index = matches.index(True)
                roll_number = known_names[matched_index]
                if roll_number not in attendance:
                    attendance[roll_number] = {"entry": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            roll_numbers.append(roll_number)
        
        # Draw rectangles around detected faces and show roll number
        for (top, right, bottom, left), roll_number in zip(face_locations, roll_numbers):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, roll_number, (left, top - 10), font, 0.5, (0, 255, 0), 2)
        
        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            break
        
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route("/")
def index():
    return render_template("index.html")  # Use your HTML template here

@app.route("/video_feed")
def video_feed():
    return Response(
        generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame"
    )

@app.route("/attendance")
def get_attendance():
    return render_template("attendance.html", attendance=attendance)

@app.route("/mark_exit/<roll_number>")
def mark_exit(roll_number):
    if roll_number not in roll_to_name:
        return "Roll number not found"
    if roll_number not in attendance or "exit" in attendance[roll_number]:
        return "Exit time already marked or entry not found"
    exit_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry_time = attendance[roll_number]["entry"]
    duration = calculate_duration(entry_time, exit_time)
    status = "Present" if duration >= datetime.timedelta(minutes=5) else "Absent"
    attendance[roll_number]["exit"] = exit_time
    attendance[roll_number]["duration"] = duration
    attendance[roll_number]["status"] = status
    return "Exit time marked"

# Helper function to calculate duration
def calculate_duration(entry_time, exit_time):
    entry_datetime = datetime.datetime.strptime(entry_time, "%Y-%m-%d %H:%M:%S")
    exit_datetime = datetime.datetime.strptime(exit_time, "%Y-%m-%d %H:%M:%S")
    duration = exit_datetime - entry_datetime
    return duration

@app.route("/download_csv")
def download_csv():
    data = []
    for roll_number, info in attendance.items():
        entry_time = info["entry"]
        exit_time = info.get("exit", "Not marked")
        duration = info.get("duration", "N/A")
        status = info.get("status", "N/A")
        
        if isinstance(duration, datetime.timedelta):
            hours, remainder = divmod(duration.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            duration_formatted = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            duration_formatted = duration
        
        name = roll_to_name.get(roll_number, "Unknown")
        data.append({"Roll Number": roll_number, "Name": name, "Entry Time": entry_time, "Exit Time": exit_time, "Duration": duration_formatted, "Status": status})
    
    df = pd.DataFrame(data)
    
    buffer = BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    
    return send_file(
        buffer, as_attachment=True, download_name="attendance.csv", mimetype="text/csv"
    )

if __name__ == "__main__":
    app.run(debug=True)
