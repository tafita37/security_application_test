from django.db import models
class Users(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    email = models.CharField(unique=True, max_length=100, db_column='email', null=False)
    password = models.TextField(db_column='password', null=False)

    class Meta:
        managed = False
        db_table = 'users'