from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_data(request):
    LCO=Course.objects.all()
    d={'course':LCO}
    if request.method=='POST':
        cno=request.POST['cno']
        cname=request.POST['cname']
        tname=request.POST['tname']
        CO=Course.objects.get_or_create(cno=cno,cname=cname,tname=tname)[0]
        CO.save()
        return HttpResponse("data submitted successfully") 
    
    return render(request,'insert_data.html',d)


def insert_student(request):
    LSO=Course.objects.all()
    d={'students':LSO}
    if request.method=='POST':
        sno=request.POST['sno']
        sname=request.POST['sname']
        cname=request.POST['cname']
        CO=Course.objects.get(cname=cname)
        SO=Student.objects.get_or_create(sno=sno,sname=sname,cname=CO)[0]
        SO.save()
        return HttpResponse("data submitted successfully") 
    return render(request,'insert_student.html',d)
