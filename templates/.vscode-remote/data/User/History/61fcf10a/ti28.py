from django.shortcuts import render, redirect
from afrik_kitchen.forms import ContactForm
from django.http import HttpResponse


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            pass
            return redirect('hom/contact_success')
    else:
        form = ContactForm()
    return render(request, 'home/contact.html', {'form': form})


def success(request):
   return HttpResponse('home/contact_success!')