from lib2to3.fixes.fix_input import context

from django.contrib.messages import success
from django.http import JsonResponse

from django.shortcuts import render
from pyexpat.errors import messages
from contact.models import Message
from contact.forms import ContactForm

# Create your views here.

def contact_form(request):

    if request.POST:
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            Message.objects.create(
                name = name,
                email = email,
                message = message,
                subject = subject,
            )
            contact_form.send_mail()

            success = True
            message = 'Contact form sent successfully.'
        else:
            success = False
            message = 'Contact form is not valid.'
    else:
        success = False
        message = 'Request method is not valid.'



    context = {'success': success ,'message': message}
    return JsonResponse(context)

def contact(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'contact_form': contact_form
    }
    return render(request, 'contact.html', context)