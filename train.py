import os
import face_recognition
import numpy as np

# Path to the directory containing individual's images
dataset_path = "C:/Users/User/Documents/AYUSH/COLLEGE/MINOR PROJECT/SMART/Face Recognition/Datasets"

known_encodings = []
known_names = []

for person_folder in os.listdir(dataset_path):
    person_name = person_folder
    person_images = os.listdir(os.path.join(dataset_path, person_folder))

    for image_file in person_images:
        image_path = os.path.join(dataset_path, person_folder, image_file)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)

        if len(encoding) > 0:
            known_encodings.append(encoding[0])
            known_names.append(person_name)

# Saved the encodings and names for future recognition
# For simplicity, I saved them to a numpy file
np.savez("encodings.npz", encodings=known_encodings, names=known_names)

print("Training completed and encodings saved.......")
