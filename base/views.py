from django.shortcuts import render
# from django.http import HttpResponse

# rooms = [{'id':1, 'name': 'onkar is the man'},{'id':2, 'name': 'how are you'},{'id':3, 'name': 'good morning'}]

# Create your views here.
# def home(request):
#     context = {'data': rooms}
#     return render(request,'base/home.html',context)

# def room(request,pk):
#     j = None
#     for i in rooms:
#         if i['id'] == int(pk):
#             j = i
#     context = {'room': j}
#     return render(request,"base/room.html",context)


#222. for loop django template
# name = ["onkar",'raj','max']
# def home(request):
#     data = {'name':name}
#     return render(request,'base/home.html',data)