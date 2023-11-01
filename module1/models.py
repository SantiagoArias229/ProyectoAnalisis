from django.db import models


class pfModel(models.Model):
    func = models.CharField(max_length=255)
    funcg = models.CharField(max_length=255)
    x0 = models.FloatField()
    Tol =  models.FloatField()
    niter = models.IntegerField()
    error= models.IntegerField()
    resultado = models.CharField(max_length=300, default=" ")
    
    def _str_(self):
        return f"La función f{self.func} y la función g {self.funcg}: desde {self.x0} en {self.niter} iteraciones"

class BiseccionModel(models.Model):
    func = models.CharField(max_length=255)
    xi = models.FloatField()
    xs = models.FloatField()
    tol =  models.FloatField()
    iteraciones = models.IntegerField()
    resultado = models.CharField(max_length=300, default=" ")
    
    def __str__(self):
        return f"{self.func}: {self.xi} a {self.xs} en {self.iteraciones} iteraciones"

class secanteModel(models.Model):
    func = models.CharField(max_length=255)
    x0 = models.FloatField()
    x1 = models.FloatField()
    Tol =  models.FloatField()
    niter = models.IntegerField()
    error= models.IntegerField(default=2)
    
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


class rmModel(models.Model):
    func = models.CharField(max_length=255)
    x0 = models.FloatField()
    tol =  models.FloatField()
    iteraciones = models.IntegerField()
    resultado = models.CharField(max_length=300, default=" ")
    
    def __str__(self):
        return f"{self.func}: de {self.x0} en {self.iteraciones} iteraciones"
