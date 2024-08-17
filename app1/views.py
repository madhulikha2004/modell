from django.shortcuts import render
from app1.models import semres

# Create your views here.
def mad(request):
    result=semres.objects.all()

    if request.method=='POST':
        studentname=request.POST.get('studentname')
        pinno=request.POST.get('pinno')
        marks=request.POST.get('marks')
        obj=semres(studentname=studentname,pinno=pinno,marks=marks)
        obj.save()
        result=semres.objects.all()
        return render(request,'mark.html',{'b':result})
    return render(request,'mark.html',{'b':result})
        
