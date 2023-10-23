from django.db import models

# Create your models here.


class ReglaFalsaModel(models.Model):
    xi = models.FloatField()
    xs = models.FloatField()
    iteracions = models.IntegerField()

    def _str_(self):
        return f"{self.funcion}: {self.a} a {self.b} en {self.iteracions} iteraciones"

class BiseccionModel(models.Model):
    func = models.CharField(max_length=255)
    xi = models.FloatField()
    xs = models.FloatField()
    tol =  models.FloatField()
    iteraciones = models.IntegerField()
    
    def _str_(self):
        return f"{self.func}: {self.xi} a {self.xs} en {self.iteraciones} iteraciones"