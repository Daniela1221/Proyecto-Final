from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "tienda"

urlpatterns = [
    path("", views.home, name="home"),
#     # path("productos/carro/",,name="productos_carro")
]

#PRODUCTOS
urlpatterns += [
    path("producto/list/", views.ProductoList.as_view(), name="producto_list"),
    path("producto/create/",views.ProductoCreate.as_view(),name="producto_create"),
    path("producto/detail/<int:pk>",views.ProductoDetail.as_view(),name="producto_detail"),
    path("producto/update/<int:pk>",views.ProductoUpdate.as_view(),name="producto_update"),
    path("producto/delete/<int:pk>",views.ProductoDelete.as_view(),name="producto_delete")
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(static.MEDIA_URL, document_root=settings.MEDIA_ROOT)