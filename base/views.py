from django.shortcuts import render
# from django.http import HttpResponse

rooms = [{'id':1, 'name': 'onkar is the man'},{'id':2, 'name': 'how are you'},{'id':3, 'name': 'good morning'}]

# Create your views here.
def home(request):
    context = {'rooms': rooms}
    return render(request,'base/home.html',context)

def room(request):
    return render(request,"base/room.html")
