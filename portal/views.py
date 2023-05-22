from django.shortcuts import render, get_object_or_404, redirect
from .models import App
from .forms import AppForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


def app_list(request):
    apps = App.objects.all()
    return render(request, 'app_list.html', {'apps': apps})

def app_detail(request, pk):
    app = get_object_or_404(App, pk=pk)
    return render(request, 'app_detail.html', {'app': app})


def app_add(request):
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            # Create a new App object with the data from the form
            new_app = App(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                url=form.cleaned_data['url']
            )
            # Save the new App object to the database
            new_app.save()
            return redirect('app_list')
    else:
        form = AppForm()
    return render(request, 'app_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def edit_app(request, app_id):
    app = get_object_or_404(App, id=app_id)

    if request.method == 'POST':
        form = AppForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
            return redirect('app_list')
    else:
        form = AppForm(instance=app)

    return render(request, 'edit_app.html', {'form': form, 'app': app})


