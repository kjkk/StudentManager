from django import forms
from profiles.models import TeacherProfile

class AddTeacher(forms.ModelForm):

    class Meta():
        user = TeacherProfile()
        fields = '__all__'

    def __str__(self):
        return self.name
