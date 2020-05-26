from django.shortcuts import render


def home(request):

    return render(request, 'home.html')
# Create your views here.

def face_detect(request):

    #wykrywaie twarzy
    return 0