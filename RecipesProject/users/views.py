from django.shortcuts import render,redirect
from .forms import UserRegistrationForm, CreateProfileForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.models import User
from recipes.models import recipe
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
# Create your views here.

class UserHome(TemplateView):
    model = Profile
    template_name = 'home/home.html'
    context = {}

    def get_object(self,user):
        return Profile.objects.get(user=user)

    def get(self,request,*args,**kwargs):
        user = request.user.id
        if user:
            data = recipe.objects.filter(~Q(created_by=user))
            self.context['data'] = data
            try:
                profile = self.get_object(user)
                self.context['profile'] = 'pro_exist'
                return render(request,self.template_name,self.context)
            except Exception:
                return render(request,self.template_name, self.context)
        return redirect('home')


class UserRegister(TemplateView):
    model = User
    form_class = UserRegistrationForm
    context = {}
    template_name = 'users/registration.html'

    def get(self,request,*args,**kwargs):
        self.context['form'] = self.form_class()
        return render(request,self.template_name,self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            self.context['form'] = form
            return render(request, self.template_name,self.context)


class SignIn(TemplateView):
    form_class = LoginForm
    context = {}
    template_name = 'users/login.html'

    def get(self,request,*args,**kwargs):
        self.context['form'] = self.form_class()
        return render(request, self.template_name, self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('userhome')
            else:
                self.context['form'] = form
                return render(request,self.template_name, self.context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateProfile(TemplateView):
    form_class = CreateProfileForm
    context = {}
    template_name = 'users/createprofile.html'

    def get(self,request,*args,**kwargs):
        form = self.form_class(initial={'user':request.user})
        self.context['form'] = form
        return render(request,self.template_name, self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewprofile')
        else:
            self.context['form'] = form
            return render(request,self.template_name, self.context)


class SignOut(TemplateView):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('home')


class ViewProfile(TemplateView):
    context = {}
    template_name = 'users/viewprofile.html'

    def get(self,request,*args,**kwargs):
        user_id = request.user.id
        try:
            profile = Profile.objects.get(user=user_id)
            self.context['profile'] = profile
        except Exception:
            pass
        data = recipe.objects.filter(created_by=user_id)
        self.context['data'] = data
        return render(request,self.template_name,self.context)


@method_decorator(login_required(login_url='login'),name='dispatch')
class EditProfile(TemplateView):
    context = {}
    form_class = CreateProfileForm
    template_name = 'users/editprofile.html'

    def get_object(self,request):
        return Profile.objects.get(user = request.user)

    def get(self, request, *args, **kwargs):
        user = self.get_object(request)
        form = self.form_class(instance=user)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self,request,*args,**kwargs):
        user = self.get_object(request)
        form = self.form_class(data=request.POST,files=request.FILES,instance=user)
        if form.is_valid():
            form.save()
            return redirect('viewprofile')
        else:
            return render(request, self.template_name, self.context)




