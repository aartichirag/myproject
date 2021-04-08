from django.urls import path
from .views import NewAddmission

urlpatterns=[
    path("new/",NewAddmission.as_view(),name="addmission-new")
]