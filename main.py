import face_recognition
import os

def find_matching_faces(new_face_path, image_gallery_path):
    # Load the new face image
    new_face = face_recognition.load_image_file(new_face_path)
    new_face_encoding = face_recognition.face_encodings(new_face)[0] if face_recognition.face_encodings(new_face) else None

    # Get a list of file paths in the image gallery
    image_files = [f for f in os.listdir(image_gallery_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Loop through each image in the gallery
    for image_file in image_files:
        # Load the current image from the gallery
        current_image_path = os.path.join(image_gallery_path, image_file)
        current_image = face_recognition.load_image_file(current_image_path)

        # Find face locations and encodings in the current image
        face_locations = face_recognition.face_locations(current_image)
        face_encodings = face_recognition.face_encodings(current_image, face_locations)

        # Compare the new face with faces in the current image
        for face_encoding in face_encodings:
            match = face_recognition.compare_faces([new_face_encoding], face_encoding)
            if match[0]:
                print(f"Match found in {current_image_path}")
                break

# Example usage
new_face_path = "/home/pachari/TS/face-recon/ref_face.jpg"
image_gallery_path = "/home/pachari/TS/face-recon/gallery"
find_matching_faces(new_face_path, image_gallery_path)
