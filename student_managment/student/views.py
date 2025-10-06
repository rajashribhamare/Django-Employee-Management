from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student  

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})  

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})  

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'create_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')
  




