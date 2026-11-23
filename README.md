# Online Courses Management System

## Project Overview

The Online Courses Management System is a web-based application developed using Django. It helps manage students, instructors, courses, and student enrollments in one centralized platform.

The system provides an administrative dashboard where users can manage educational information efficiently.

## Main Features

### 1. Dashboard
- View total students.
- View total instructors.
- View total courses.
- View total enrollments.
- Display recent enrollments.

### 2. Student Management
- Add new students.
- View all students.
- Update student information.
- Delete student records.

### 3. Instructor Management
- Add new instructors.
- View instructor records.
- Update instructor information.
- Delete instructor records.

### 4. Course Management
- Create new courses.
- Assign instructors to courses.
- View course details.
- Update and delete courses.

### 5. Enrollment Management
- Enroll students in courses.
- View enrollment records.
- Update enrollment information.
- Delete enrollments.
- Manage enrollment statuses: Active, Completed, and Dropped.

### 6. Available Courses
- Display available courses.
- Search courses by title.

### 7. Enrolled Students
- View students enrolled in courses.
- Display course and enrollment information.

## Technologies Used

- Python
- Django
- SQLite
- HTML5
- CSS3
- JavaScript
- Bootstrap 5
- Bootstrap Icons

## Project Structure

```text
Online_Courses_management_system1/
│
├── courses/
├── myproject/
├── templates/
├── static/
├── manage.py
├── db.sqlite3
├── README.md
└── LICENSE
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/cawkeisback-prog/Online_Courses_management_system1.git
```

### 2. Open the Project Folder

```bash
cd Online_Courses_management_system1
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Django

```bash
pip install django
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Database

This project uses SQLite as its database.

## License

This project is developed for educational purposes as part of a Django Group Project.
