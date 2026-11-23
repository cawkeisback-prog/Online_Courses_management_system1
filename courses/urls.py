
from django.urls import path
from . import views

urlpatterns = [

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Student Management
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/edit/<int:pk>/', views.student_update, name='student_update'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),

    # Instructor Management
    path('instructors/', views.instructor_list, name='instructor_list'),
    path('instructors/add/', views.instructor_create, name='instructor_create'),
    path('instructors/edit/<int:pk>/', views.instructor_update, name='instructor_update'),
    path('instructors/delete/<int:pk>/', views.instructor_delete, name='instructor_delete'),
        # Course Management
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_create, name='course_create'),
    path('courses/edit/<int:pk>/', views.course_update, name='course_update'),
    path('courses/delete/<int:pk>/', views.course_delete, name='course_delete'),
        # Enrollment Management
    path('enrollments/', views.enrollment_list, name='enrollment_list'),
    path('enrollments/add/', views.enrollment_create, name='enrollment_create'),
    path('enrollments/edit/<int:pk>/', views.enrollment_update, name='enrollment_update'),
    path('enrollments/delete/<int:pk>/', views.enrollment_delete, name='enrollment_delete'),
    path(
    'available-courses/',
    views.available_courses,
    name='available_courses'
),
path(
    'enrolled-students/',
    views.enrolled_students,
    name='enrolled_students'
),

]

