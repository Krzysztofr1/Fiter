from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SurveyForm
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def home_view(request):
    return render(request, 'home.html')



def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey_data = form.save(commit=False)
            survey_data.user = request.user
            survey_data.save()
            return redirect('survey_success')  # Po zapisaniu danych, przekierowanie na stronę sukcesu
    else:
        form = SurveyForm()

    return render(request, 'survey/survey_form.html', {'form': form})

def survey_success(request):
    return render(request, 'survey/survey_success.html')