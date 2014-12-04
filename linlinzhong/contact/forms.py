from django import forms
from django.core.mail import send_mail, EmailMessage
from django.conf import settings

class ContactForm(forms.Form):
    sender_email = forms.EmailField()
    subject = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea)
    cc_sender = forms.BooleanField(required=False)

    def send_email(self):
        subject = '[LZDesign] ' + self.cleaned_data['subject']
        message = self.cleaned_data['message']
        sender_email = self.cleaned_data['sender_email']
        cc_sender = self.cleaned_data['cc_sender']
        headers = {'Reply-To' : sender_email}

        cc_list = []
        if cc_sender:
            cc_list.append(sender_email)

#        send_mail(subject, message, sender_email, recipients)
        email = EmailMessage(subject, message, sender_email, [], bcc=[settings.EMAIL_HOST_USER, 'linda3825612@hotmail.com'], headers=headers, cc=cc_list)
        email.send()
