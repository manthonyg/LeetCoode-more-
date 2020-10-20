from . import views
from django.urls import path

urlpatterns = {
    path("", views.index, name="index"),
    path("<str:name>", views.name, name="name"),
    path("yang", views.yang, name="yang")
}