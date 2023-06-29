from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class Taotk(UserCreationForm):
     class Meta:
          model= User
          fields =['username','email','first_name','last_name','password1','password2']
class Nguoidung(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,blank=False)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
class Phong(models.Model):
    name = models.CharField(max_length=200,null=True)
    gia = models.FloatField()
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    @property
    def ImageURL(self):
        try:
            url=self.image.url
        except:
            url = ''
        return url
class Datphong(models.Model):
    nguoidung = models.ForeignKey(Nguoidung,on_delete=models.SET_NULL,null=True,blank=False)
    tgdat = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id= models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.id)
    @property
    def get_cart_items(self):
            dsdat=self.dsdat_set.all()
            tong=sum([item.sl for item in dsdat])
            return tong
    @property
    def get_cart_tong(self):
            dsdat=self.dsdat_set.all()
            tongtien =sum([item.get_tong for item in dsdat])
            return tongtien
class dsdat(models.Model):
    phong = models.ForeignKey(Phong,on_delete=models.SET_NULL,null=True,blank=False)
    datphong = models.ForeignKey(Datphong,on_delete=models.SET_NULL,null=True,blank=False)
    sl =models.IntegerField(default=0,null=True,blank=False)
    ngaydat = models.DateTimeField(auto_now_add=True)
    @property
    def get_tong(self):
         tong=self.phong.gia * self.sl
         return tong
class ttkhach(models.Model):
    nguoidung = models.ForeignKey(Nguoidung,on_delete=models.SET_NULL,null=True,blank=False)
    datphong = models.ForeignKey(Datphong,on_delete=models.SET_NULL,null=True,blank=False)
    sdt= models.CharField(max_length=11,null=True)
    ngaydat = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id