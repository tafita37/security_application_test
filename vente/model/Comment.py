from django.db import models
from django.utils import timezone

from vente.model.Product import Product
from vente.model.Users import Users

class Comment(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    user = models.ForeignKey(Users, db_column='user_id', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, db_column='product_id', on_delete=models.CASCADE)
    content = models.TextField(db_column='content', null=False)
    created_at = models.DateTimeField(default=timezone.now, db_column='created_at', null=False)

    class Meta:
        managed = False
        db_table = 'comment'