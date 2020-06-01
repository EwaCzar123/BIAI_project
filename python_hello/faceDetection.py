""" from PIL import Image
import face_recognition


# Load the jpg file into a numpy array
image = face_recognition.load_image_file("but.jpeg")

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
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show() """

from PIL import Image
import face_recognition
import cv2

def faceRecognition(imageName, number_of_times_to_upsample, model):
  operation_image = face_recognition.load_image_file(file)
  return_image = cv2.imread(file)

  face_locations = face_recognition.face_locations(operation_image, number_of_times_to_upsample, model)
  print("{}".format(number_of_times_to_upsample))
  print("Na zdjęciu znaleziono {} twarzy.".format(len(face_locations)))

  for face_location in face_locations:
    top, right, bottom, left = face_location
    print("Położenie twarzy w pikselach Góra: {}, Lewo: {}, Dół: {}, Prawo: {}".format(top, left, bottom, right))

    top_left = (left, top)
    bottom_right = (right, bottom)
    cv2.rectangle(return_image, top_left, bottom_right, (0, 255, 0), 2)

  filename = "Wynik na argumentach: number_of_times_to_upsample=" + str(number_of_times_to_upsample) +", model=" + str(model) + ".jpg"

  cv2.imshow(filename, return_image)
  print("Wciśnij dowolny przycisk aby zamknąć okno")
  cv2.waitKey(0)
  cv2.destroyWindow(filename)

file = "faces.jpg"
faceRecognition(file, 0, "hog")
faceRecognition(file, 1, "hog")
faceRecognition(file, 2, "hog")
faceRecognition(file, 3, "hog")
faceRecognition(file, 0, "cnn")
faceRecognition(file, 1, "cnn")
faceRecognition(file, 2, "cnn")
faceRecognition(file, 3, "cnn")
