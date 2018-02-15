from django.http import HttpResponse
from django.views import View
from .forms import ContactForm
from django.views.generic.edit import FormView

class Base_View(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


class Form_View(FormView):
    template_name = 'class_based_views/contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)