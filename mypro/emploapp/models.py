from django.db import models

class employee(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    emp_id = models.IntegerField()
    # owner = models.ForeignKey('auth.user', related_name='empl', on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname

class stud(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    mark = models.IntegerField()
    # owner = models.ForeignKey('auth.user', related_name='studs', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class cust(models.Model):
    name = models.CharField(max_length=10)
    product = models.CharField(max_length=10)
    cust_id = models.IntegerField()

    def __str__(self):
        return self.name