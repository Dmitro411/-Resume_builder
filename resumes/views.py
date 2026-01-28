from django.shortcuts import render
from .forms import ResumeCreateForm, ResumeUpdateForm, ResumeSectionCreateForm, EducationCreateForm, ExperienceCreateForm, SkillCreateForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from resumes import models, forms
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

class ResumeListView(ListView):
    model = models.Resume
    context_object_name = "resumes"
    template_name = "resumes/resume_list.html"


class ResumeCreateView(CreateView):
    model = models.Resume
    form_class = ResumeCreateForm
    template_name = "resumes/resume_create.html"
    success_url = reverse_lazy("resume-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def resume_detail_view(request, pk):
    if request.method == 'GET':
        resume = models.Resume.objects.get(pk=pk, user=request.user)
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

class ResumeSectionCreateView(CreateView):
    model = models.ResumeSection
    form_class = ResumeSectionCreateForm
    template_name = "resumes/resume_section_create.html"
 
    def get_success_url(self):
        return reverse("resume-detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        resume_id = self.kwargs["resume_pk"]
        resume = models.Resume.objects.get(id=resume_id)

        form.instance.resume = resume
        return super().form_valid(form)
    

class ResumeUpdateView(UpdateView):
    pass
    # model = models.Resume
    # form_class = Resume

class ResumeDeleteView(DeleteView):
    pass

class ResumeSectionUpdateView(UpdateView):
    pass

class ResumeSectionDeleteView(DeleteView):
    pass