from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=64, primary_key=True)
    password = models.CharField(max_length=1024)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.user_id


class Memo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    content = models.CharField(max_length=4096)
    private = models.BooleanField(default=True)
    pub_date = models.DateTimeField(verbose_name='date published')

    def __str__(self):
        return self.title
