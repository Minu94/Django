from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [path('register', views.UserRegister.as_view(), name="register"),
               path('createprofile',views.CreateProfile.as_view(),name="createprofile"),
               path('home',views.UserHome.as_view(),name="userhome"),
               path('login',views.SignIn.as_view(),name="login"),
               path('logout',views.SignOut.as_view(),name="logout"),
               path('viewprofile',views.ViewProfile.as_view(),name="viewprofile"),
               path('editprofile',views.EditProfile.as_view(),name="editprofile"),
]