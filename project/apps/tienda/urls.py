from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = "tienda"

urlpatterns = [
    path("", views.home, name="home"),
    path("carrito",views.carrito,name="carrito"),
]

#PRODUCTOS
urlpatterns += [
    path("productos/list/", views.ProductoList.as_view(), name="producto_list"),
    path("productos/create/",views.ProductoCreate.as_view(),name="producto_create"),
    path("productos/detail/<int:pk>",views.ProductoDetail.as_view(),name="producto_detail"),
    path("productos/update/<int:pk>",views.ProductoUpdate.as_view(),name="producto_update"),
    path("productos/delete/<int:pk>",views.ProductoDelete.as_view(),name="producto_delete"),
]

urlpatterns += staticfiles_urlpatterns()