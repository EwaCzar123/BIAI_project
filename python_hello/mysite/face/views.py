from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from PIL import Image
import face_recognition

global uploaded_file

def home(request):

    return render(request, 'home.html')
# Create your views here.


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        print(uploaded_file.name)

    return render(request, 'home.html')



def face_detect(request, uploaded_file):
# Load the jpg file into a numpy array
    image = face_recognition.load_image_file(uploaded_file.name)

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
        pil_image.show()

    return render(request, 'home.html')


