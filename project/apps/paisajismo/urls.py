from django.urls import path
from .views import home

app_name = "paisajismo"

urlpatterns = [
    path("", home, name="home"),

]