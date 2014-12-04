from django.contrib import admin

# Register your models here.

from projects.models import Project, Image

class ImageInLine(admin.TabularInline):
    model = Image
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
            ('Project Infomation', {'fields' : ['title',
                                                'description',
                                                'location',
                                                'category',
                                                'subtype',
                                                'scale',
                                                'start_date',
                                                'end_date',
                                                'status',]}),
    ]

    inlines = [ImageInLine]
    list_display= ['title', 'location', 'category', 'subtype', 'start_date']
    search_fields = ['title']

admin.site.register(Project, ProjectAdmin)
