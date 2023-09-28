from django.urls import path, include
from . import views

app_name="comentario"

urlpatterns = [
    path('<int:id>/novo', views.novo)
]