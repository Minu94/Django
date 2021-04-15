from django.shortcuts import render, redirect
from .models import StudRegister,StudComplete

# Create your views here.


def registration(request):
    return render(request,'student/registration.html')


def complete(request):
    return render(request,'student/complete.html')


def login(request):
    return render(request,'student/login.html')


def home(request):
    return render(request,'student/home.html')




def getstreg(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    pwd = request.POST.get('password')
    streg = StudRegister(firstname=firstname,lastname=lastname,email=email,password=pwd)
    streg.save()
    print(email,pwd, 'completed')
    return redirect('stlogin')


def getstlogin(request):
    email = request.POST.get("email")
    pwd = request.POST.get("password")
    if request.method == 'POST':
        try:
            streg = StudRegister.objects.get(email=email)
            print(streg)
            if (streg.email == email) & (streg.password == pwd):
                context={}
                firstname=streg.firstname
                lastname=streg.lastname
                name=firstname+" "+lastname
                context['name']=name
                return render(request,'student/complete.html',context)
            else:
                return redirect('stlogin')
        except Exception as e:
            return redirect('stlogin')
    return redirect('stlogin')







def getcomplete(request):
    username = request.POST.get('username')
    phonenumber = request.POST.get('phonenumber')
    address = request.POST.get('address')
    education = request.POST.get('education')
    details = request.POST.get('details')
    year = request.POST.get('year')
    percentage = request.POST.get('percentage')
    course = request.POST.get('course')
    mode = request.POST.get('mode')
    print(username,phonenumber,address,education,details,year,percentage,course,mode)
    complete = StudComplete(username=username, phonenumber=phonenumber, address=address,
                            education=education, details=details, year=year,
                            percentage=percentage, course=course, mode=mode)
    complete.save()
    if request.method=='POST':
        try:
            obj = StudComplete.objects.get(username=username)
            course = obj.course
            context = {}
            context['course'] = course
            return render(request,'student/home.html', context)
        except:
            return redirect('stcomplete')
    else:
        print('er2')
        return redirect('stcomplete')

    return redirect('stcomplete')


