from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.core.urlresolvers import reverse
from django.utils import timezone

from projects.models import Project, Image

from pprint import pprint

class ProjectIndexView(View):
    def get(self, request):
        project_list = Project.objects.order_by('start_date')
        #TODO: the following categorization may be handled by DB query
        categorized_project_list = {}
        for project in project_list:
            typed_project = {project.subtype_str() : project}
            categorized_project_list.setdefault(project.category_str(), typed_project)[project.subtype_str()] = project

        template = loader.get_template('projects/index.html')
        context = RequestContext(request, {
            'categorized_project_list' : categorized_project_list,
            })
        return HttpResponse(template.render(context))

class ProjectDetailView(View):
    def get(self, request, project_id):
        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            raise Http404

        # shortcut for contruct HttpResponse as in function index()
        return render(request, 'projects/detail.html', {'project' : project})


