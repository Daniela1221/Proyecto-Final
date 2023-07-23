from django.urls import path
from .views import home

app_name = "hogar"

urlpatterns = [
    path("", home, name="home"),

]