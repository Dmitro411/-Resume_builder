from django.contrib import admin
from .models import Resume, ResumeSection, EducationItem, ExperienceItem, SkillItem, PrivateInformationItem

admin.site.register(Resume)
admin.site.register(ResumeSection)
admin.site.register(EducationItem)
admin.site.register(ExperienceItem)
admin.site.register(SkillItem)
admin.site.register(PrivateInformationItem)
