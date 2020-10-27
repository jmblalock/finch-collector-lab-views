from django.shortcuts import render, redirect
from .models import Finch
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()

    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)

    feeding_form = FeedingForm()

    return render(request, 'finches/detail.html', {
        'finch': finch,
        'feeding_form': feeding_form
    })

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)

    # if form is valid
    if form.is_valid():
        #submit the form
        new_form = form.save(commit=False)
        new_form.finch_id = finch_id
        new_form.save()

    return redirect('detail', finch_id=finch_id)