from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Courses

def home(request):
    context = { "courses" : Courses.objects.all()

    }
    return render(request, "index.html", context)

def new(request):
    context = { "courses" : Courses.objects.all()

    }
    errors = Courses.objects.validate(request.POST)
    if errors:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/')
    Courses.objects.create(
        name = request.POST['name'],
        description = request.POST['desc']
    )
    return render(request, "index.html", context)

def confirm(request, course_id):
    confirm = Courses.objects.get(id=course_id)
    context = {
        "confirm" : confirm
    }
    return render(request, "confirm.html", context)

def destroy(request,course_id):
    course_delete = Courses.objects.get(id=course_id)
    course_delete.delete()
    return redirect('/')