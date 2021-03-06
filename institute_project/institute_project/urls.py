"""institute_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include("users.urls")),
    path('course/',include("course.urls")),
    path('student/',include("student.urls")),
    path("addmission/",include("addmission.urls")),
    path("payment/",include("payment.urls")),
    path("inquiry/",include("inquiry.urls")),
    path("chart/",include("chart.urls")),
    path('',LoginView.as_view(template_name="users/sign-in.html",success_url="/home/"),name="login"),
    # path('logout',LogoutView.as_view(template_name="users/sign-up.html",success_url="/home/"),name="logout")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)