from django.db import models

# Create your models here.

class Öğrenci(models.Model):
    isim = models.CharField(max_length=50)
    soyisim = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)
    doğum_tarihi = models.DateField()
    okul = models.CharField(max_length=50)
    bölüm = models.CharField(max_length=50)
    sınıflar = (
        ('1','1. Sınıf'),
        ('2','2. Sınıf'),
        ('3','3. Sınıf'),
        ('4','4. Sınıf'),
    )
    sınıf = models.CharField(max_length=1, choices=sınıflar)
    created_date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.isim

