from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'con_agg'
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
