from django.db import models

 

class Student(models.Model):
    fisrt_name=models.CharField('adı',max_length=50)  # gettext _('') fonsksiyonu var translation için
    last_name=models.CharField('soyadı', max_length=50)# last name değil soyadı olarak göster dedik
    number=models.IntegerField('numara')

    def __str__(self):# burada str ile ekranda nasıl göstemek istiyoruz onun için yoksa object yazar 
       return f"{self.fisrt_name}-{self.last_name}-{self.number} "
    class Meta:
        ordering=['number'] # öğrenci numarasına göre sıraladı
       # ordering=['-number'] tersten sıralamak için
        verbose_name_plural="Öğrenciler" # admin panalde oluşturduğumuz models isminin nasıl görünmesini istiyorsak onu yazarız burada student models öğrenciler olarak görünecek
        