from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, AdmissionFormForm
from .models import AdmissionForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('admissions')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login/login.html', {'error': 'Invalid credentials'})
    return render(request, 'login/login.html')


@login_required
def dashboard(request):
    try:
        admission_form = AdmissionForm.objects.get(user=request.user)
        if admission_form.status == 'approved':
            admission_status = "Admitted"
        elif admission_form.status == 'rejected':
            admission_status = "Rejected"
        else:
            admission_status = "Pending Review"
    except AdmissionForm.DoesNotExist:
        admission_form = None
        admission_status = "No application submitted"

    context = {
        'username': request.user.username,
        'email': request.user.email,
        'admission_status': admission_status,
        'admission_form': admission_form,
    }
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def admissions(request):
    if request.method == 'POST':
        form = AdmissionFormForm(request.POST, request.FILES)
        if form.is_valid():
            admission_form = form.save(commit=False)
            admission_form.user = request.user
            admission_form.save()
            return redirect('success')
    else:
        form = AdmissionFormForm()
    return render(request, 'admissions/admissions.html', {'form': form})

def success(request):
    return render(request, 'success/success.html')