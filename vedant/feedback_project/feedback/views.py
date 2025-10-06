from django.shortcuts import render, redirect

from .forms import FeedbackForm

# Create your views here.
def feedback_view(request):
    if request.method =='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')

    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form})


def thank_you(request):
    return render(request, 'feedback/thank_you.html')


def home(request):
    return redirect('feedback_form')  # Redirects to feedback form