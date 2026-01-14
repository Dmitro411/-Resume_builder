from django.contrib import admin
from .models import Resume, ResumeSection, Education, Experience, Skill

admin.site.register(Resume)
admin.site.register(ResumeSection)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)