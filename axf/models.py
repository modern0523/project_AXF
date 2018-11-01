from django.db import models

# Create your models here.
class Base(models.Model):
    img = models.CharField(max_length=520)
    name = models.CharField(max_length=250)
    trackid = models.CharField(max_length=10)
    class Meta:
        abstract=True

#轮播图
class Lunbo(Base):
    class Meta:
        db_table='axf_wheel'






