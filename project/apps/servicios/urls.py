from django.urls import path
from .views import home

app_name = "servicios"

urlpatterns = [
    path("", home, name="home"),

]