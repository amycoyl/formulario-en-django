from django.urls import path
from . import views
app_name = 'anuncios'
urlpatterns = [
    # post views
    path('', views.anuncios_list, name='anuncios_list')
]
from django.contrib import admin
from django.urls import path,  include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('anuncios.urls', namespace='anuncios')),