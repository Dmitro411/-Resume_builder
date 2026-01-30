from django.forms import ModelForm, Form, DateInput, TextInput, FileInput, CheckboxInput, NumberInput, Select
from .models import Resume, ResumeSection, EducationItem, ExperienceItem, SkillItem

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
    
class EducationItemCreateForm(ModelForm):

    class Meta:
        model = EducationItem
        fields = ["institution", "speciality", "city", "degree", "start_year", "end_year", "description"]
        widgets = {
            "institution": TextInput(attrs={"class": "form-control"}),
            "speciality": TextInput(attrs={"class": "form-control"}),
            "city": TextInput(attrs={"class": "form-control"}),
            "degree": TextInput(attrs={"class": "form-control"}),
            "start_year": DateInput(attrs={"type": "date", "class": "form-control"}),
            "end_year": DateInput(attrs={"type": "date", "class": "form-control"}),
            "description": TextInput(attrs={"class": "form-control"}),
        }

class ExperienceItemCreateForm(ModelForm):

    class Meta:
        model = ExperienceItem
        fields = ["company", "position", "city", "why_fired", "start_date", "end_date", "description"]
        widgets = {
            "company": TextInput(attrs={"class": "form-control"}),
            "position": TextInput(attrs={"class": "form-control"}),
            "city": TextInput(attrs={"class": "form-control"}),
            "why_fired": TextInput(attrs={"class": "form-control"}),
            "start_date": DateInput(attrs={"type": "date", "class": "form-control"}),
            "end_date": DateInput(attrs={"type": "date", "class": "form-control"}),
            "description": TextInput(attrs={"class": "form-control"}),
        }

class SkillItemCreateForm(ModelForm):
    class Meta:
        model = SkillItem
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={"class": "form-control"}),
        }
        