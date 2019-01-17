from django.shortcuts import HttpResponse
from django.shortcuts import  render

def index(request):
    return HttpResponse("Hello,dear how are you ?")

def one(request):
    return render(request, 'one.html')