from django.shortcuts import render
from .forms import ResumeCreateForm, ResumeUpdateForm, ResumeSectionCreateForm, EducationCreateForm, ExperienceCreateForm, SkillCreateForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from resumes import models, forms

def resume_detail_view(request):
    if request.method == 'GET':
        resume = models.Resume.objects.get(pk=request.user.pk)
        sections = resume.sections.all()
        context = {}
        context['resume'] = resume
        context['sections'] = sections
        return render(request, "resumes/resume_detail.html", context=context)
    

# class ResumeDetailView(DetailView):
#     model = models.Resume
#     context_object_name = "resume"
#     template_name = "resumes/resume_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         resume = context['resume']
#         education = resume.educations.all()
#         context['education'] = education
#         return context

# class ResumeCreateView(CreateView):
# class ResumeUpdateView(UpdateView):
# class ResumeDetailView(DetailView):
# class ResumeDeleteView(DeleteView):