from django.urls import path
from .views import home

app_name = "pilares"

urlpatterns = [
    path("", home, name="home"),

]