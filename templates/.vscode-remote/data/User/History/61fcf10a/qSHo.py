from django.shortcuts import render, redirect
from afrik_kitchen.forms import ContactForm
from django.http import HttpResponse

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        #success_url = 'home/contact_success'
        if form.is_valid():
            # Process the form data and get the name
            name = form.cleaned_data['name']
            # Add logic to save the form data or perform any other actions
            
            return redirect('success', name=name)  # Pass the name as a parameter
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request, name):
    message = f"Thank you, {name}, for submitting the form!, Our Manager will attend to  Your request"
    return render(request, 'contact_success.html', {'message': message})