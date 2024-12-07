from django.contrib import admin
from .models import Course,OnlineClass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'pdf_link', 'video_link')

@admin.register(OnlineClass)
class OnlineClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'zoom_link', 'created_at')
    search_fields = ('title','created_at')


# admin.py
from django.contrib import admin
from .models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'created_at')
    search_fields = ('title', 'description')

admin.site.register(Assignment, AssignmentAdmin)
