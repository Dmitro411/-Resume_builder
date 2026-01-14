from django.forms import ModelForm, Form, DateInput, TextInput, FileInput, CheckboxInput
from .models import Resume, ResumeSection, Education, Experience, Skill

class ResumeCreateForm(ModelForm):
    
    class Meta:
        model = Resume
        fields = ["title", "is_draft"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "is_draft": CheckboxInput(attrs={"class": "form-check", "required":True})
        }

#TODO Додати форми