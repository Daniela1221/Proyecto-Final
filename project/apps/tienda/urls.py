from django.urls import path
from .views import home

app_name = "tienda"

urlpatterns = [
    path("", home, name="home"),

]