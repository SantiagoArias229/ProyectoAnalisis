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
    resultado = models.CharField(max_length=300,default=" ")
    
    def __str__(self):
        return f"{self.func}: {self.x0} a {self.x1} en {self.niter} iteraciones"

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


#MODULE 2
class sorModel(models.Model):
    x0= models.TextField()
    a=models.TextField()
    b=models.TextField()
    tol=models.FloatField()
    niter=models.IntegerField()
    w= models.FloatField()

    def __str__(self) -> str:
        return  f"{self.a}: con solución b {self.b} y condición inicial {self.x0} en {self.niter} iteraciones"

class gsModel(models.Model):
    A = models.JSONField()
    b = models.JSONField(null=True, blank=True)
    x0 = models.JSONField(null=True, blank=True)
    tol = models.FloatField()
    niter=models.IntegerField()



#MODULE 3
