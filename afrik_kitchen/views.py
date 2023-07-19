from django.shortcuts import render, redirect
from afrik_kitchen.forms import ContactForm
from django.http import HttpResponse

"""This is  to create a form that can be used"""
"""to collect user input for contact"""


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
       
        if form.is_valid():
            # Process the form data and get the name
            name = form.cleaned_data['name']
            
            return redirect('success', name=name)  
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def success(request, name):
    message = f"Thank you, {name}, for submitting the form!,"
    f"our Manager will get back to you within 5 hours"
    return render(request, 'contact_success.html', {'message': message})
