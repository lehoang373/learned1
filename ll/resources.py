from import_export import resources
from .models import Lesson

class LessonResource(resources.ModelResource):
    class Meta:
        model = Lesson
        fields = ('projectnumber','projectname', 'client', 'projectlocation', 'description', 'division','marketsector','discipline','memo','linkfile')