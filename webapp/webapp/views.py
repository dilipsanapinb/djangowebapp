from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    data={
        'title':'Home',
        'clist':['Java','Javascript','Python'],
        'students':[
            {'name':'Dilip','email':'dilip@gmail.com'},
            {'name':'Ajay','email':'ajay@gmail.com'}
        ]
    }
    return render(request,"index.html",data)
def aboutus(request):
    return render(request,'aboutus.html')



def course(request):
    return HttpResponse("Course page")

def courseDetails(request,courseId):
    return HttpResponse(courseId)