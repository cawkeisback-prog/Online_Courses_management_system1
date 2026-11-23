
from django import forms
from .models import Student, Instructor, Course, Enrollment


# ==========================
# STUDENT FORM
# ==========================

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['full_name', 'email', 'phone']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
        }

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name'].strip()

        if len(full_name) < 3:
            raise forms.ValidationError(
                'Full name must contain at least 3 characters.'
            )

        return full_name

    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip()

        digits = ''.join(char for char in phone if char.isdigit())

        if len(digits) < 7 or len(digits) > 15:
            raise forms.ValidationError(
                'Phone number must contain between 7 and 15 digits.'
            )

        return phone


# ==========================
# INSTRUCTOR FORM
# ==========================

class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = [
            'full_name',
            'email',
            'phone',
            'specialization'
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter instructor name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),

            'specialization': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter specialization'
            }),
        }

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name'].strip()

        if len(full_name) < 3:
            raise forms.ValidationError(
                'Instructor name must contain at least 3 characters.'
            )

        return full_name

    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip()

        digits = ''.join(char for char in phone if char.isdigit())

        if len(digits) < 7 or len(digits) > 15:
            raise forms.ValidationError(
                'Phone number must contain between 7 and 15 digits.'
            )

        return phone

    def clean_specialization(self):
        specialization = self.cleaned_data['specialization'].strip()

        if len(specialization) < 2:
            raise forms.ValidationError(
                'Please enter a valid specialization.'
            )

        return specialization


# ==========================
# COURSE FORM
# ==========================

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = [
            'title',
            'description',
            'instructor',
            'duration',
            'price'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course description',
                'rows': 4
            }),

            'instructor': forms.Select(attrs={
                'class': 'form-select'
            }),

            'duration': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Example: 3 Months'
            }),

            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter course price',
                'step': '0.01',
                'min': '0'
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if len(title) < 3:
            raise forms.ValidationError(
                'Course title must contain at least 3 characters.'
            )

        return title

    def clean_description(self):
        description = self.cleaned_data['description'].strip()

        if len(description) < 10:
            raise forms.ValidationError(
                'Course description must contain at least 10 characters.'
            )

        return description

    def clean_duration(self):
        duration = self.cleaned_data['duration'].strip()

        if not duration:
            raise forms.ValidationError(
                'Please enter course duration.'
            )

        return duration

    def clean_price(self):
        price = self.cleaned_data['price']

        if price < 0:
            raise forms.ValidationError(
                'Course price cannot be negative.'
            )

        return price


# ==========================
# ENROLLMENT FORM
# ==========================

class EnrollmentForm(forms.ModelForm):

    class Meta:
        model = Enrollment
        fields = [
            'student',
            'course',
            'status'
        ]

        widgets = {
            'student': forms.Select(attrs={
                'class': 'form-select'
            }),

            'course': forms.Select(attrs={
                'class': 'form-select'
            }),

            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
