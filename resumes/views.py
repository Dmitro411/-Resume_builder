from django.shortcuts import render
from .forms import ResumeCreateForm, ResumeUpdateForm, ResumeSectionCreateForm, EducationItemCreateForm, ExperienceItemCreateForm, SkillItemCreateForm
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
        response = super().form_valid(form)

        DEFAULT_SECTIONS = [
            "Приватна інформація",
            "Освіта",
            "Досвід роботи",
            "Навички",
            "Про себе",
        ]

        for i, title in enumerate(DEFAULT_SECTIONS):
            models.ResumeSection.objects.create(
                resume=self.object,
                title=title,
                order=i
            )

        return response

@login_required
def resume_detail_view(request, pk):
    if request.method == 'GET':
        resume = models.Resume.objects.get(pk=pk, user=request.user)
        sections = resume.sections.all().order_by('order')
        personal_info_form = forms.PrivateInformationItemCreateForm()
        context = {}
        context['resume'] = resume
        context['sections'] = sections
        context['personal_info_form'] = personal_info_form
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
        return reverse("resume-detail", kwargs={"pk": self.object.resume.pk})

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