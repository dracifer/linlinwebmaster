from django.conf.urls import patterns, url

from contact import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', views.ContactView.as_view(), name='contact'),
    url(r'^thanks/$', views.ThanksView.as_view(), name='thanks'),
) 

