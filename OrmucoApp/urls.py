from django.contrib import admin
from django.urls import path
from favs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create, name='create'),
]