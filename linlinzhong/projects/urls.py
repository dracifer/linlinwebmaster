from django.conf.urls import patterns, url

from projects import views
from projects import classviews
from django.conf import settings
from django.conf.urls.static import static

import pprint

classViewOn = True

urlpatterns = patterns('',
    # ex: /projects/
    url(r'^$', classviews.ProjectIndexView.as_view() if classViewOn else views.index, name='index'),
    # ex: /projects/5/
    url(r'^(?P<project_id>\d+)/$', classviews.ProjectDetailView.as_view() if classViewOn else views.detail, name='detail'), #(?<name>...) - a re that matches the expression in ... and the value can be accessed by .group(<name>)
    # dev test for ex: /projects/1/
    url(r'^media_files/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # to test media on dev

pprint.pprint(urlpatterns)
