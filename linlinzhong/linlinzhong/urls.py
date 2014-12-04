from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    # Examples:
    # url(r'^$', 'linlinzhong.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/projects/'), name='mainpage'),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^about/', include('about.urls', namespace='about')),
    url(r'^contact/', include('contact.urls', namespace='contact')),
]
