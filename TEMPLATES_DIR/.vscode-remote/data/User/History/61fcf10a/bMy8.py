from django.shortcuts import render, redirect
from afrik_kitchen.forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data and get the name
            name = form.cleaned_data['name']
            # Add logic to save the form data or perform any other actions
            
            return redirect('contact_success', name=name)  # Pass the name as a parameter
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def success(request, name):
    message = f"Thank you, {name}, for submitting the form!"
    return render(request, 'contact_success.html', {'message': message})


# def success(request, name):
#    return HttpResponse(f'Success! Thank you, {name}, for submitting the form.')
