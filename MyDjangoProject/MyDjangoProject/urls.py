from django.contrib import admin
from django.urls import path,include
from MainApp import *

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include('MainApp.urls')),
]