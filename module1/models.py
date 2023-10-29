from django.db import models


class pfModel(models.Model):
    func = models.CharField(max_length=255)
    xi = models.FloatField()
    xs = models.FloatField()
    tol =  models.FloatField()
    iteraciones = models.IntegerField()
    
    def _str_(self):
        return f"{self.func}: {self.xi} a {self.xs} en {self.iteraciones} iteraciones"

class BiseccionModel(models.Model):
    func = models.CharField(max_length=255)
    xi = models.FloatField()
    xs = models.FloatField()
    tol =  models.FloatField()
    iteraciones = models.IntegerField()
    
    def _str_(self):
        return f"{self.func}: {self.xi} a {self.xs} en {self.iteraciones} iteraciones"

class secanteModel(models.Model):
    func = models.CharField(max_length=255)
    x0 = models.FloatField()
    x1 = models.FloatField()
    Tol =  models.FloatField()
    niter = models.IntegerField()
    error= models.IntegerField()
    
    def _str_(self):
        return f"{self.func}: {self.xi} a {self.xs} en {self.iteraciones} iteraciones"

class newton1Model(models.Model):
    func = models.CharField(max_length=255)
    xi = models.FloatField()
    xs = models.FloatField()
    tol =  models.FloatField()
    iteraciones = models.IntegerField()
    
    def _str_(self):
        return f"{self.func}: {self.xi} a {self.xs} en {self.iteraciones} iteraciones"

class rfModel(models.Model):
    func = models.CharField(max_length=255)
    xi = models.FloatField()
    xs = models.FloatField()
    tol =  models.FloatField()
    iteraciones = models.IntegerField()
    
    def _str_(self):
        return f"{self.func}: {self.xi} a {self.xs} en {self.iteraciones} iteraciones"