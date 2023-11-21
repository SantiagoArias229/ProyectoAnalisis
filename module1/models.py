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
    Terror= models.IntegerField()
    resultado = models.CharField(max_length=300,default=" ")

    
    def __str__(self):
        return f"La función {self.func}: en el intervalo de {self.x0} a {self.x1} en {self.niter} iteraciones tiene como resultado:"

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
    x0 = models.FloatField()
    x1 = models.FloatField()
    Tol =  models.FloatField()
    niter = models.IntegerField()
    Terror= models.IntegerField()
    resultado = models.CharField(max_length=300,default=" ")
    
    def __str__(self):
        return f"La función {self.func}: en el intervalo de {self.x0} a {self.x1} en {self.niter} iteraciones tiene como resultado:"


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
    A = models.JSONField()
    b = models.JSONField(null=True, blank=True)
    x0 = models.JSONField(null=True, blank=True)
    tol = models.FloatField()
    niter=models.IntegerField()
    w= models.FloatField( null=False, default=1)
    error= models.IntegerField( null=False, blank=True)

class gsModel(models.Model):
    A = models.JSONField()
    b = models.JSONField(null=True, blank=True)
    x0 = models.JSONField(null=True, blank=True)
    tol = models.FloatField()
    niter=models.IntegerField()

class jacobiModel(models.Model):
    A = models.JSONField()
    b = models.JSONField(null=True, blank=True)
    x0 = models.JSONField(null=True, blank=True)
    tol = models.FloatField()
    niter=models.IntegerField()

#MODULE 3
class lagrange(models.Model):
    x = models.JSONField()
    y = models.JSONField()

class newtonintModel(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    pol = models.TextField(max_length=2000)



class vandermondemodel(models.Model):
    x = models.JSONField()
    y = models.JSONField()



