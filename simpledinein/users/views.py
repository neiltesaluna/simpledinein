from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save() # creates user if form is valid
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username} successfully!')
      return redirect('all_recipes')
  else:
    form = UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})