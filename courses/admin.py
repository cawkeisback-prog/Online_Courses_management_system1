from django.contrib import admin
from .models import Student, Instructor, Course, Enrollment
admin.site.register(Student)
admin.site.register(Instructor) 
admin.site.register(Course)
admin.site.register(Enrollment)

# Register your models here.
