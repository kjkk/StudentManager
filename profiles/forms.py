from django import forms
from profiles.models import TeacherProfile

class AddTeacher(forms.ModelForm):

    class Meta():
        model = TeacherProfile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddTeacher, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs\
            .update({
                'placeholder': 'First Name',
                'class': 'form-control'
            })
        self.fields['last_name'].widget.attrs\
            .update({
                'placeholder': 'Last Name',
                'class': 'form-control'
            })
        self.fields['designation'].widget.attrs\
            .update({
                'placeholder': 'Desgination',
                'class': 'form-control'
            })
        self.fields['department'].widget.attrs\
            .update({
                'placeholder': 'Department',
                'class': 'form-control'
            })
        self.fields['teacher_id'].widget.attrs\
            .update({
                'placeholder': 'ID',
                'class': 'form-control'
            })
        self.fields['dob'].widget.attrs\
            .update({
                'placeholder': 'Date Of Birth',
                'class': 'form-control'
            })
        self.fields['joining_year'].widget.attrs\
            .update({
                'placeholder': 'Joining Year',
                'class': 'form-control'
            })
        self.fields['address'].widget.attrs\
            .update({
                'placeholder': 'Address',
                'class': 'form-control'
            })
        self.fields['is_cc'].widget.attrs\
            .update({
                'placeholder': 'Is_cc',
                'class': 'form-control'
            })
        self.fields['is_hod'].widget.attrs\
            .update({
                'placeholder': 'is_hod',
                'class': 'form-control'
            })
