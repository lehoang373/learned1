from django import forms
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('projectnumber', 'projectname', 'client', 'projectlocation', 'description', 'division','marketsector','discipline','memo','linkfile')
