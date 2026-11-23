
from django.db import models


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Instructor(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    duration = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title


class Enrollment(models.Model):

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Dropped', 'Dropped'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    enrollment_date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Active'
    )

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.full_name} - {self.course.title}"

