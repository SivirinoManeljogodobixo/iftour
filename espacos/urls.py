from django.urls import path, include
from . import views

app_name="espacos"

urlpatterns = [
    path('', views.index, name="index"),
    path('bloco/', views.blocodefault, name="bloco_padrao" ),
    path('bloco/add/', views.add_bloco, name='add_bloco'),
    path('bloco/<int:id>/', views.bloco, name="bloco" ),
    path('piso/<int:id>/', views.piso, name="piso" ),
    path('sala/<int:id>/', views.sala, name='sala'),
    path('login_adm/', views.login_adm, name='login_adm'),
    path('cadastro_adm/', views.cadastro_adm, name='cadastro_adm'),  
]
