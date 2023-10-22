from django.db import models

# Create your models here.


class ReglaFalsaModel(models.Model):
    xi = models.FloatField()
    xs = models.FloatField()
    iteracions = models.IntegerField()

    def _str_(self):
        return f"{self.funcion}: {self.a} a {self.b} en {self.iteracions} iteraciones"