from django.shortcuts import render
from django.db import transaction

from sio.models import *
from sio.forms import *

def home(request):
    context = {'courses': Course.objects.all(),
               'messages': [],
               'create_student_form': CreateStudentForm(),
               'create_course_form': CreateCourseForm(),
               'register_student_form': RegisterStudentForm(),
               }
    return render(request, 'sio.html', context)

@transaction.atomic
def create_student(request):
    messages = []
    context = {'courses': Course.objects.all(),
               'messages': messages,
               'create_student_form': CreateStudentForm(),
               'create_course_form': CreateCourseForm(),
               'register_student_form': RegisterStudentForm(),
               }

    if request.method == 'GET':
        return render(request, 'sio.html', context)

    form = CreateStudentForm(request.POST)
    context['create_student_form'] = form

    if not form.is_valid():
        return render(request, 'sio.html', context)

    form.save()

    # messages.append('Added %s' % new_student)
    messages.append("Added student!")
    return render(request, 'sio.html', context)

@transaction.atomic
def create_course(request):
    messages = []
    context = {'courses': Course.objects.all(),
               'messages': messages,
               'create_student_form': CreateStudentForm(),
               'create_course_form': CreateCourseForm(),
               'register_student_form': RegisterStudentForm(),
               }

    if request.method == 'GET':
        return render(request,'sio.html', context)

    form = CreateCourseForm(request.POST)
    context['create_course_form'] = form

    if not form.is_valid:
        return render(request, 'sio.html', context)

    form.save()
    messages.append('Added course!' )
    return render(request, 'sio.html', context)

@transaction.atomic
def register_student(request):
    messages = []
    context = {'courses': Course.objects.all(),
               'messages': messages,
               'create_student_form': CreateStudentForm(),
               'create_course_form': CreateCourseForm(),
               'register_student_form': RegisterStudentForm(),
               }

    if request.method == 'GET':
        return render(request, 'sio.html', context)

    form = RegisterStudentForm(request.POST)
    context['register_student_form'] = form

    if not form.is_valid:
        return render(request, 'sio.html', context)

    if Student.objects.filter(andrew_id=request.POST['andrew_id']).count() != 1:
        messages.append("Could not find Andrew ID %s." %
                        request.POST['andrew_id'])

    if Course.objects.filter(course_number=request.POST['course_number']).count() != 1:
        messages.append("Could not find course %s." %
                        request.POST['course_number'])
    if messages:
        return render(request, 'sio.html', context)


    course = Course.objects.get(course_number=request.POST['course_number'])
    student = Student.objects.get(andrew_id=request.POST['andrew_id'])
    course.students.add(student)
    course.save()

    messages.append('Added %s to %s' % (student, course))
    return render(request, 'sio.html', context)
