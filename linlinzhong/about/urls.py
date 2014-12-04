from django.conf.urls import patterns, url

from about import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', views.AboutView.as_view(), name='about'),
) 

