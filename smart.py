import cv2
import time

video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier("C:/Users/User/Documents/AYUSH/COLLEGE/MINOR PROJECT/SMART/Face Recognition/haarcascade_frontalface_default.xml")

# Taking the number of friends and their roll numbers as input.
num_friends = int(input("Enter the number of friends: "))
friend_roll_numbers = []

for i in range(num_friends):
    roll_number = input(f"Enter the roll number for friend {i + 1}: ")
    friend_roll_numbers.append(roll_number)

for roll_number in friend_roll_numbers:
    current_id = 0

    while True:
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        min_face_size = (100, 100)
        faces = facedetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=min_face_size)

        for (x, y, w, h) in faces:
            # Store the captured image with roll number and incremental ID
            image_filename = f'{roll_number}.{current_id}.jpg'
            # Construct the image path using the current roll number
            image_path = f'C:/Users/User/Documents/AYUSH/COLLEGE/MINOR PROJECT/SMART/Face Recognition/Datasets/{roll_number}/{image_filename}'
            cv2.imwrite(image_path, gray[y:y+h, x:x+w])

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            current_id += 1  # Increment the ID for the next image
            cv2.putText(frame, f'Photos Captured: {current_id}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Frame", frame)

        k = cv2.waitKey(1)

        if current_id >= 20:
            break
        
        # Adding a time gap of 5 seconds before capturing images for the next friend
        print(f"Images captured for friend {roll_number}. Waiting for 5 seconds...")
        time.sleep(2)
        
video.release()
cv2.destroyAllWindows()
print("Dataset Collection Done..................")
