from django.db import models
from django.contrib import admin
from django.utils import timezone


class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre


class Desempeno(models.Model):
    nombre = models.CharField(max_length=60)
    anio = models.IntegerField()
    mascotas = models.ManyToManyField(Mascota, through='Categoria')

    def __str__(self):
        return self.nombre


class Categoria (models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    desempeno = models.ForeignKey(Desempeno, on_delete=models.CASCADE)


class CategoriaInLine(admin.TabularInline):
    model = Categoria
    extra = 1


class MascotaAdmin(admin.ModelAdmin):
    inlines = (CategoriaInLine,)


class DesempenoAdmin (admin.ModelAdmin):
    inlines = (CategoriaInLine,)
