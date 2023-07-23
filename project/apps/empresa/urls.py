from django.urls import path
from .views import home

app_name = "empresa"

urlpatterns = [
    path("", home, name="home"),

]