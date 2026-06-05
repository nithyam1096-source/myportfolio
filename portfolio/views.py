from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('home')
        else:
            messages.error(request, 'Please fill in all required fields correctly.')
    else:
        form = ContactForm()

    return render(request, 'portfolio/index.html', {'form': form})
