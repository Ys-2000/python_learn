from django.db import models


class userInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

    def __str__(self):
        # list = [self.name, self.password, self.age]
        return self.name



class Department(models.Model):
    title = models.CharField(max_length=16)

    def __str__(self):
        return self.title



