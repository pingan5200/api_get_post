from django.db import models


# Create your models here.
class Type(models.Model):
    id = models.AutoField('序号', primary_key=True)
    type_name = models.CharField('产品类型', max_length=20)

    def __str__(self):
        return self.type_name


class Product(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('名称', max_length=50)
    weight = models.CharField('重量', max_length=20)
    size = models.CharField('尺寸', max_length=20)
    type = models.ForeignKey('Type', 
                             on_delete=models.CASCADE, 
                             verbose_name='产品类型')

    def __str__(self):
        return self.name
