from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bloco(models.Model):
    nome = models.CharField(max_length=15, null=False, unique = True)
    legenda = models.TextField()
    imagem = models.ImageField(upload_to="blocos/")
   
    def __str__(self):
        return self.nome

class Piso(models.Model):
    nome = models.CharField(max_length=15, null=False, unique = True)
    bloco = models.ForeignKey(Bloco, on_delete=models.CASCADE)
    
    def get_salas(self):
        return Sala.objects.filter(piso__id = self.id)
    
    def __str__(self):
        return self.nome

class Sala(models.Model):
    nome = models.CharField(max_length=15, null=False, unique = True)
    legenda = models.TextField()
    imagem = models.ImageField("Thumbnail", upload_to="salas/")
    img_360 = models.ImageField(upload_to="360/", null=True)
    piso = models.ForeignKey(Piso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Administrador(models.Model):
    nome = models.CharField(max_length=15, null=False, unique = True)
    email = models.EmailField(unique=True)
    login = models.OneToOneField(User, on_delete=models.CASCADE)
    senha = models.CharField(max_length=128)
    foto = models.ImageField(upload_to="adms_img/", null=True)

    def __str__(self):
        return self.nome
    
    
