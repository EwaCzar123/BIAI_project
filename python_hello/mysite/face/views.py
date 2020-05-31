from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.template.response import TemplateResponse
from django.http import HttpRequest, HttpResponseRedirect
import random
import string


from PIL import Image
import face_recognition

from .forms import PictureForm
from .models import Picture

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def home(request):
    form = PictureForm() 
    pics = Picture.objects.all()
    if request.method == 'POST':
        form = PictureForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:  
        form = PictureForm()  
    for pic in pics:
        print("media/{}" .format(pic.photo))
        if(format(pic.photo)!=" "):
            image = face_recognition.load_image_file(f'media/{pic.photo}')
        print("I found {} face(s) in this photograph.".format(len(face_locations)))
        arg = {}
        for face_location in face_locations:

    # Print the location of each face in this image
            top, right, bottom, left = face_location
            print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
            randomS = randomString()
            print(randomS)
            face_image = image[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            pil_image.save("D:/studia-inf/BIAI/BIAI_project/python_hello/mysite/media/{}.jpg".format(randomS))
        
        
        arg['face'] = "{}.jpg".format(randomS)
    arg['file_name'] = uploaded_file.name
    return render(request,'home.html', { 
        'form': form, 'pics': pics
        })

 
# Create your views here.


def upload(request):
    if request.method == 'POST':
        global uploaded_file
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        print(uploaded_file.name)
    arg = {}
    arg['file_name'] = uploaded_file.name
    return TemplateResponse(request, 'home.html', arg)

def model_form_upload(request): 
    if request.method == 'POST':
        form = PictureForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else: 
        form = PictureForm() 
    return render(request,'home.html', { 
        'form': form, 'pics': pics
        })


def face_detect(request):
  
# Load the jpg file into a numpy array
    #global uploaded_file
    #print(uploaded_file.name)
    #picts = pics
    #image = face_recognition.load_image_file(f'media/{uploaded_file.name}')
    #print(image)

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py
    """ face_locations = face_recognition.face_locations(image)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))
    arg = {}
    for face_location in face_locations:

    # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
        randomS = randomString()
        print(randomS)
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save("D:/studia-inf/BIAI/BIAI_project/python_hello/mysite/media/{}.jpg".format(randomS))
        
        
        arg['face'] = "{}.jpg".format(randomS)
    arg['file_name'] = uploaded_file.name """
    return TemplateResponse(request, 'home.html')

