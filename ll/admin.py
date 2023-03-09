from django.contrib import admin

from .models import Lesson

class LessonList(admin.ModelAdmin):
    list_display = ( 'projectname', 'projectnumber', 'author')
    list_filter = ( 'projectname', 'projectnumber')
    search_fields = ('author', )
    ordering = ['author']

admin.site.register(Lesson, LessonList)
