
from django.shortcuts import render, redirect, get_object_or_404

from .models import Student, Instructor, Course, Enrollment
from .forms import StudentForm, InstructorForm, CourseForm, EnrollmentForm


# ==========================
# DASHBOARD
# ==========================

def dashboard(request):
    context = {
        'total_students': Student.objects.count(),
        'total_instructors': Instructor.objects.count(),
        'total_courses': Course.objects.count(),
        'total_enrollments': Enrollment.objects.count(),

        'recent_enrollments': Enrollment.objects.select_related(
            'student', 'course'
        ).order_by('-id')[:5],
    }

    return render(request, 'courses/dashboard.html', context)


# ==========================
# STUDENT MANAGEMENT
# ==========================

def student_list(request):
    students = Student.objects.all().order_by('-id')

    return render(request, 'courses/students/student_list.html', {
        'students': students
    })


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'courses/students/student_form.html', {
        'form': form
    })


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'courses/students/student_form.html', {
        'form': form,
        'student': student
    })


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'courses/students/student_confirm_delete.html', {
        'student': student
    })


# ==========================
# INSTRUCTOR MANAGEMENT
# ==========================

def instructor_list(request):
    instructors = Instructor.objects.all().order_by('-id')

    return render(request, 'courses/instructors/instructor_list.html', {
        'instructors': instructors
    })


def instructor_create(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('instructor_list')
    else:
        form = InstructorForm()

    return render(request, 'courses/instructors/instructor_form.html', {
        'form': form
    })


def instructor_update(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)

    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)

        if form.is_valid():
            form.save()
            return redirect('instructor_list')
    else:
        form = InstructorForm(instance=instructor)

    return render(request, 'courses/instructors/instructor_form.html', {
        'form': form,
        'instructor': instructor
    })


def instructor_delete(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)

    if request.method == 'POST':
        instructor.delete()
        return redirect('instructor_list')

    return render(request, 'courses/instructors/instructor_confirm_delete.html', {
        'instructor': instructor
    })


# ==========================
# COURSE MANAGEMENT
# ==========================

def course_list(request):
    courses = Course.objects.all().order_by('-id')

    return render(
        request,
        'courses/courses/course_list.html',
        {'courses': courses}
    )


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(
        request,
        'courses/courses/course_form.html',
        {'form': form}
    )


def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)

        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)

    return render(
        request,
        'courses/courses/course_form.html',
        {'form': form, 'course': course}
    )


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':
        course.delete()
        return redirect('course_list')

    return render(
        request,
        'courses/courses/course_confirm_delete.html',
        {'course': course}
    )


# ==========================
# ENROLLMENT MANAGEMENT
# ==========================

def enrollment_list(request):
    enrollments = Enrollment.objects.all().order_by('-id')

    return render(
        request,
        'courses/enrollments/enrollment_list.html',
        {'enrollments': enrollments}
    )


def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()

    return render(
        request,
        'courses/enrollments/enrollment_form.html',
        {'form': form}
    )


def enrollment_update(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)

        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)

    return render(
        request,
        'courses/enrollments/enrollment_form.html',
        {'form': form, 'enrollment': enrollment}
    )


def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)

    if request.method == 'POST':
        enrollment.delete()
        return redirect('enrollment_list')

    return render(
        request,
        'courses/enrollments/enrollment_confirm_delete.html',
        {'enrollment': enrollment}
    )


# ==========================
# AVAILABLE COURSES
# ==========================

def available_courses(request):
    search_query = request.GET.get('search', '')

    courses = Course.objects.all().order_by('-id')

    if search_query:
        courses = courses.filter(title__icontains=search_query)

    context = {
        'courses': courses,
        'search_query': search_query,
    }

    return render(
        request,
        'courses/available_courses.html',
        context
    )


# ==========================
# ENROLLED STUDENTS
# ==========================

def enrolled_students(request):
    enrollments = Enrollment.objects.select_related(
        'student', 'course'
    ).all().order_by('-id')

    return render(
        request,
        'courses/enrolled_students.html',
        {'enrollments': enrollments}
    )
