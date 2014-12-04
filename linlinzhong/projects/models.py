from django.db import models

# Create your models here.

class Group(models.Model):
    NAME_CHOICES = (
        ('ADMIN', 'Administrator'),
        ('USER',  'User'),
        ('VISITOR', 'Visitor')
    )
    name = models.CharField(max_length=64)

class User(models.Model):
    nick_name = models.CharField(max_length=64, default="Anonymous")
    last_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    group = models.ForeignKey(Group)
    email = models.EmailField(max_length=128)

class Project(models.Model):
    UNCLASSIFIED = 0
    BUILDING = 1
    INTERIOR = 2
    URBAN = 3
    INSTALLATION = 4
    CATEGORY_CHOICES = (
        (UNCLASSIFIED, 'Unclassified'),
        (BUILDING, 'Building'),
        (INTERIOR, 'Interior'),
        (URBAN, 'Urban'),
        (INSTALLATION, 'Installation')
    )
    RESIDENTIAL = 1
    OFFICE = 2
    CULTURAL = 3
    TYPE_CHOICES = (
        (UNCLASSIFIED, 'Unclassified'),
        (RESIDENTIAL, 'Residential'),
        (OFFICE, 'Office'),
        (CULTURAL, 'Cultural'),
    )

    NOT_STARTED = 0
    RESEARCHING = 1
    IN_PROGRESS = 2
    SUSPENDED = 3
    COMPLETED = 4
    ABORTED = 5
    STATUS_CHOICES = (
        (NOT_STARTED, 'Not Started'),
        (RESEARCHING, 'Researching'),
        (IN_PROGRESS, 'In Progress'),
        (SUSPENDED, 'Suspended'),
        (COMPLETED, 'Completed'),
        (ABORTED, 'Aborted'),
    )

    title = models.CharField(max_length=256)
    description = models.TextField()
    location = models.CharField(max_length=256)
    category=models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES, verbose_name="Project Category", default=UNCLASSIFIED)
    subtype=models.PositiveSmallIntegerField(choices=TYPE_CHOICES, verbose_name="Project Type", default=UNCLASSIFIED)
    scale = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField()
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    def cover_image(self):
        return self.image_set.get(embed_project_order__exact=0)
    def category_str(self):
        return Project.CATEGORY_CHOICES[self.category][1]
    def subtype_str(self):
        return Project.TYPE_CHOICES[self.subtype][1]
    def status_str(self):
        return Project.STATUS_CHOICES[self.status][1]

class Image(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    project = models.ForeignKey(Project)
    embed_project_text = models.TextField()
    embed_project_order = models.PositiveSmallIntegerField()
    data = models.ImageField(upload_to='images')
    class Meta:
        ordering = ['embed_project_order']

class Comment(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    


