from django.db import models

 

class Student(models.Model):
    COUNTRIES=[# choices İLE BURADAN SEÇER
        ('TR',"Turkey" ),
        ('US',"America" ),
        ('DE',"Germany" ),
        ('FR',"France" ),
        
    ]

    first_name=models.CharField('adı',max_length=50)  # gettext _('') fonsksiyonu var translation için
    last_name=models.CharField('soyadı', max_length=50)# last name değil soyadı olarak göster dedik
    number=models.IntegerField('numara')
    about=models.TextField('Hakkında',blank=True,null=True) # blank=True boş veri gönderebilrim veya null gönderbilrim 
    country=models.CharField('Ülke',max_length=2,choices=COUNTRIES,default='TR' )
    avatar=models.ImageField('resim',blank=True,null=True,upload_to="meida/")# upload_to nereye yüklemek istediğimizi belirler
# pip install pillow resim yüklemek için indirmemiz gereken paket
    register_date=models.DateTimeField(auto_now_add=True) # otomotik olarak oluşturulan kayıtların ne zaman kadedildiğini tutar
    update_date=models.DateTimeField(auto_now=True) # otomotik olarak oluşturulan kayıtların ne zaman kadedildiğini tutar



    def __str__(self):# burada str ile ekranda nasıl göstemek istiyoruz onun için yoksa object yazar 
       return f"{self.first_name}-{self.last_name}-{self.number} "
    class Meta:
        ordering=['number'] # öğrenci numarasına göre sıraladı
       # ordering=['-number'] tersten sıralamak için
        verbose_name_plural="Öğrenciler" # admin panalde oluşturduğumuz models isminin nasıl görünmesini istiyorsak onu yazarız burada student models öğrenciler olarak görünecek
