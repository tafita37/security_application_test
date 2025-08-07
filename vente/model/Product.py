from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(unique=True, max_length=100, db_column='name', null=False)
    description = models.TextField(db_column='description', null=False)
    price = models.FloatField(db_column='price', null=False)
    image = models.CharField(max_length=255, db_column='image', null=False)

    class Meta:
        managed = False
        db_table = 'product'