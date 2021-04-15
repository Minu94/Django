from django.shortcuts import render,redirect
from .models import TrainerRegister,TrainerComplete

# Create your views here.
def registration(request):
    return render(request,'trainer/registration.html')


def complete(request):
    return render(request, 'trainer/complete.html')


def login(request):
    return render(request, 'trainer/login.html')

def home(request):
    return render(request,'trainer/home.html')

def gettrreg(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    pwd = request.POST.get('password')
    trreg = TrainerRegister(firstname=firstname,lastname=lastname,email=email,password=pwd)
    trreg.save()
    return redirect('trlogin')

def gettrlogin(request):
    email = request.POST.get("email")
    pwd = request.POST.get("password")
    if request.method == 'POST':
        try:
            trreg = TrainerRegister.objects.get(email=email)
            if (trreg.email == email) & (trreg.password == pwd):
                context = {}
                firstname = trreg.firstname
                lastname = trreg.lastname
                name = firstname + " " + lastname
                context['name'] = name
                return render(request, 'trainer/complete.html', context)
            else:
                return redirect('trlogin')
        except Exception as e:
            return redirect('trlogin')
    return redirect('trlogin')


def gettrcomplete(request):
    username = request.POST.get('username')
    phonenumber = request.POST.get('phonenumber')
    address = request.POST.get('address')
    education = request.POST.get('education')
    details = request.POST.get('details')
    year = request.POST.get('year')
    percentage = request.POST.get('percentage')
    expert = request.POST.get('expert')
    experience = request.POST.get('experience')
    available = request.POST.get('available')
    hours = request.POST.get('hours')
    mode = request.POST.get('mode')
    days = request.POST.get('days')

    completetr = TrainerComplete(username=username, phonenumber=phonenumber, address=address,
                            education=education, details=details, year=year,
                            percentage=percentage, expert=expert,experience=experience,
                               available=available,hours=hours,mode=mode,days=days)
    completetr.save()
    if request.method=='POST':
        try:
            obj = TrainerComplete.objects.get(username=username)
            course = obj.expert
            context = {}
            context['course'] = course
            return render(request,'trainer/home.html', context)
        except Exception as e :
            return redirect('trcomplete')
    else:
        print('er2')
        return redirect('trcomplete')

    return redirect('trcomplete')
