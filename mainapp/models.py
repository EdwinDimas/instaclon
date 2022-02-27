from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250)
    mensaje = models.CharField(max_length=250)
    foto = models.FileField(upload_to="profile_pics/")
    esPrivado = models.BooleanField()
    user_id = models.ForeignKey(User, on_delete=models.RESTRICT)


class Post(models.Model):
    foto = models.FileField(upload_to="post_pics/")
    mensaje = models.CharField(max_length=250)
    fecha = models.DateField()
    perfil_id = models.ForeignKey(Perfil, on_delete=models.RESTRICT)
    
    
class Like(models.Model):
    perfil_id = models.ForeignKey(Perfil, on_delete=models.RESTRICT)
    post_id = models.ForeignKey(Post, on_delete=models.RESTRICT)
    
    
class Comentario(models.Model):
    mensaje = models.CharField(max_length=500)
    fecha = models.DateField()
    perfil_id = models.ForeignKey(Perfil, on_delete=models.RESTRICT)
    post_id = models.ForeignKey(Post, on_delete=models.RESTRICT)
      

class Seguido(models.Model):
    perfil_id = models.ForeignKey(Perfil, on_delete=models.RESTRICT, related_name="seguido_perfil")
    seguido_id = models.ForeignKey(Perfil, on_delete=models.RESTRICT, related_name="seguido")


class Seguidor(models.Model):
    perfil_id = models.ForeignKey(Perfil, on_delete=models.RESTRICT, related_name="seguidor_perfil")
    seguidor_id = models.ForeignKey(Perfil, on_delete=models.RESTRICT, related_name="seguidor")

