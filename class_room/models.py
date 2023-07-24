from django.db import models


from django.db import models

# Create your models here.
class Bench11(models.Model):
    bench_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_image = models.ImageField(upload_to='student_image', null=True, blank=True)

class Bench12(models.Model):
    bench_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_image = models.ImageField(upload_to='student_image', null=True, blank=True)

class Bench13(models.Model):
    bench_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_image = models.ImageField(upload_to='student_image', null=True, blank=True)

class Bench14(models.Model):
    bench_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_image = models.ImageField(upload_to='student_image', null=True, blank=True)    

class Bench15(models.Model):
    bench_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_image = models.ImageField(upload_to='student_image', null=True, blank=True)

class Bench21(models.Model):
    bench_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_image = models.ImageField(upload_to='student_image', null=True, blank=True)

class Bench22(models.Model):
    bench_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_image = models.ImageField(upload_to='student_image', null=True, blank=True)

class Bench23(models.Model):
    bench_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_image = models.ImageField(upload_to='student_image', null=True, blank=True)

class Bench24(models.Model):
    bench_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_image = models.ImageField(upload_to='student_image', null=True, blank=True)    

class Bench25(models.Model):
    bench_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_image = models.ImageField(upload_to='student_image', null=True, blank=True)

class Bench26(models.Model):
    bench_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100, null=True, blank=True)
    student_image = models.ImageField(upload_to='student_image', null=True, blank=True)
