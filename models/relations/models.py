from django.db import models

# Create your models here.
class Creator(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    def __str__(self) :
        return f"{self.first_name}-{self.last_name} "

    class Meta:
        ordering=['first_name']

class Language(models.Model):
    name=models.CharField(max_length=50)
    creator=models.OneToOneField(Creator,on_delete=models.CASCADE)# creator tablosu ile oen to one ilişki cascade ile creator silinirse ona ait tablo da siliniyor


    def __str__(self):
        return f"{self.name}-{self.creator}  "

    class Meta:
        ordering=['name']
# YUKARIDA CREATOR İLE LANGUAGE ARASINDA ONE TO ONE İLİŞKİ KURDUK 
# AŞAĞIDA LANGUAGE İLE FREAMWORK ARASINDA ONE TO MANY İLİŞKİ KURDUK
# BÜTÜN MODELSLERDE MAKEMİGRATİONS VE ADMİN PANALDE GÖRÜNMESİN İÇİN ADMİN.PY A GİDİP İMPORT ETMEYİ UNUTMA
 # on_delete properties:
        #  CASCADE=> EĞER PRİMARY SİLİNDİ İSE FOREİNG DE SİL
        #  SET_NULL=> EĞER PRİMARY SİLNDİ İSE FOREİNG NULL YAP(null=True)
        #  SET_DEFAULT=> primary silindi ise foreing default value yap(default="Value")
        #  DO_NOTHİNG=> PRİMARY SİLİNDİ İSE BİRŞEY YAPMA
        #  PROTECT.=> FOREİNG VARSA PRİMARY SİLİNMEZ DEMEK

class Freamwork(models.Model):
    name=models.CharField(max_length=50)
    language=models.ForeignKey(Language,on_delete=models.CASCADE)# Language ilişi kuracağımız models


    def __str__(self):
        return f"{self.name}-{self.language} "

    class Meta:
        ordering=["name"]    


# AŞAĞIDA MANT TO MANY İLİŞKİSİ FRAMWORK İLE DEVELOPER TABLOSU ARASINDA YAPACAĞIZ

class Develepor(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    freamwork=models.ManyToManyField(Freamwork)# Freamwork ilişi kuracağımız models # many to many ilişkide on_delte kullanılmaz
    
    def __str__(self):
         return f"{self.first_name}-{self.last_name} "

    class Meta:
        ordering=["first_name"] 


       
      