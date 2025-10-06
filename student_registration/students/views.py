from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student

def student_register(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = StudentForm()
    return render(request, 'register.html', {'form': form})

def thank_you(request):
    return render(request, 'thank_you.html')

