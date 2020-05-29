from PIL import Image
import face_recognition
#import cv2  
from django.core.files.storage import FileSystemStorage


# Load the jpg file into a numpy array
image = face_recognition.load_image_file("face.jpg")

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
face_locations = face_recognition.face_locations(image)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
  # You can access the actual face itself like this:
    #redColor = (0,0,255)

    #image = cv2.rectangle(image, (left,top), (right,bottom), redColor, thickness) 
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save("D:/studia-inf/BIAI/BIAI_project/python_hello/mysite/media/face1.jpg")
#cv2.imwrite('D:\studia-inf\BIAI\BIAI_project\python_hello\face1.jpg', image)
#cv2.imshow("face1.jpg", image)  