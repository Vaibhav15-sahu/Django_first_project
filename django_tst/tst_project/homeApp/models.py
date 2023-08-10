from django.db import models

class student(models.Model):
    name = models.TextField(max_length=20)
    roll_no = models.IntegerField(primary_key=True)
    doa = models.DateField(auto_now_add=True)


class teacher(models.Model):
    name = models.TextField(max_length=20)
    teacher_id = models.IntegerField(primary_key=True)
    subject = models.TextField(max_length=20)

class classRoom(models.Model):
    roomNumber = models.TextField(max_length=10)

class marks(models.Model):
    os = models.TextField(max_length=20)
    dsa = models.TextField(max_length=20)
    oops = models.TextField(max_length=20)