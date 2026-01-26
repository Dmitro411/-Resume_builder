from django.forms import ModelForm, Form, DateInput, TextInput, FileInput, CheckboxInput, NumberInput, Select
from .models import Resume, ResumeSection, Education, Experience, Skill

class ResumeCreateForm(ModelForm):
    
    class Meta:
        model = Resume
        fields = ["title", "is_draft"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "is_draft": CheckboxInput(attrs={"class": "form-check", "required":True})
        }

class ResumeUpdateForm(ModelForm):

    class Meta:
        model = Resume
        fields = ["title", "is_draft"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "is_draft": CheckboxInput(attrs={"class": "form-check", "required":True})
        }

class ResumeSectionCreateForm(ModelForm):
    
    class Meta:
        model = ResumeSection
        fields = ["title", "order"]
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "order": NumberInput(attrs={"class": "form-control"})
        }
    
class EducationCreateForm(ModelForm):

    class Meta:
        model = Education
        fields = ["institution", "speciality", "degree", "start_year", "end_year"]
        widgets = {
            "institution": TextInput(attrs={"class": "form-control"}),
            "speciality": TextInput(attrs={"class": "form-control"}),
            "degree": TextInput(attrs={"class": "form-control"}),
            "start_year": NumberInput(attrs={"class": "form-control"}),
            "end_year": NumberInput(attrs={"class": "form-control"}),
        }

class ExperienceCreateForm(ModelForm):

    class Meta:
        model = Experience
        fields = ["company", "position", "description", "why_fired", "start_date", "end_date"]
        widgets = {
            "company": TextInput(attrs={"class": "form-control"}),
            "position": TextInput(attrs={"class": "form-control"}),
            "description": TextInput(attrs={"class": "form-control"}),
            "why_fired": TextInput(attrs={"class": "form-control"}),
            "start_date": DateInput(attrs={"type": "date", "class": "form-control"}),
            "end_date": DateInput(attrs={"type": "date", "class": "form-control"}),
        }

class SkillCreateForm(ModelForm):
    
    class Meta:
        model = Skill
        fields = ["name", "section"]
        widgets = {
            "name": TextInput(attrs={"class": "form-control"}),
            "section": Select(attrs={"class": "form-control"}),
        }

    