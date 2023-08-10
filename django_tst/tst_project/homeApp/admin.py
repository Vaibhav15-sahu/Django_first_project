from django.contrib import admin
from homeApp.models import student, teacher, classRoom, marks

# Register your models here.
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(classRoom)
admin.site.register(marks)
