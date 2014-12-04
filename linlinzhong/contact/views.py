from django.shortcuts import render

from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from contact.forms import ContactForm

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/thanks/'

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'thanks.html'

    def get_context_data(self, **kwargs):
        context = super(ThanksView, self).get_context_data(**kwargs)
        return context
