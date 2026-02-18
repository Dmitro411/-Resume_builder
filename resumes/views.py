from django.shortcuts import get_object_or_404, redirect, render
from .forms import ResumeForm, ResumeSectionCreateForm, EducationItemCreateForm, ExperienceItemCreateForm, SkillItemCreateForm, PrivateInformationItemCreateForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from resumes import models, forms
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

class ResumeListView(ListView):
    model = models.Resume
    context_object_name = "resumes"
    template_name = "resumes/resume_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # додаємо форму безпосередньо в кожен об'єкт
        for resume in context["resumes"]:
            resume.update_form = ResumeForm(instance=resume)

        return context
        


class ResumeCreateView(CreateView):
    model = models.Resume
    form_class = ResumeForm
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
        education_form = forms.EducationItemCreateForm()
        experiance_form = forms.ExperienceItemCreateForm()
        skill_form = forms.SkillItemCreateForm()
        context = {}
        context['resume'] = resume
        context['sections'] = sections
        context['personal_info_form'] = personal_info_form
        context['education_form'] = education_form
        context['experiance_form'] = experiance_form
        context['skill_form'] = skill_form
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

class ResumePersonalInfoCreateView(CreateView):
    model = models.PrivateInformationItem
    form_class = PrivateInformationItemCreateForm
    # template_name = "resumes/resume_detail.html"

    def get_success_url(self):
        return reverse("resume-detail", kwargs={"pk": self.object.section.resume.pk})

    def form_valid(self, form):
        resume_id = self.kwargs["resume_pk"]
        resume = models.Resume.objects.get(id=resume_id)
        section = resume.sections.get(title="Приватна інформація")
        form.instance.section = section

        return super().form_valid(form)

    def form_invalid(self, form):
        # Просто редіректимо назад на resume-detail навіть якщо форма не валідна
        resume_id = self.kwargs.get("resume_pk")
        return redirect("resume-detail", pk=resume_id)
    
class EducationItemCreateView(CreateView):
    model = models.EducationItem
    form_class = EducationItemCreateForm

    def get_success_url(self):
        return reverse("resume-detail", kwargs={"pk": self.object.section.resume.pk})

    def form_valid(self, form):
        resume_id = self.kwargs["resume_pk"]
        resume = models.Resume.objects.get(id=resume_id)
        section = resume.sections.get(title="Освіта")
        form.instance.section = section

        return super().form_valid(form)

class ExperienceItemCreateView(CreateView):
    model = models.ExperienceItem
    form_class = ExperienceItemCreateForm

    def get_success_url(self):
        return reverse("resume-detail", kwargs={"pk": self.object.section.resume.pk})

    def form_valid(self, form):
        resume_id = self.kwargs["resume_pk"]
        resume = models.Resume.objects.get(id=resume_id)
        section = resume.sections.get(title="Досвід роботи")
        form.instance.section = section

        return super().form_valid(form)
    
class SkillItemCreateView(CreateView):
    model = models.SkillItem
    form_class = SkillItemCreateForm

    def get_success_url(self):
        return reverse("resume-detail", kwargs={"pk": self.object.section.resume.pk})

    def form_valid(self, form):
        resume_id = self.kwargs["resume_pk"]
        resume = models.Resume.objects.get(id=resume_id)
        section = resume.sections.get(title="Навички")
        form.instance.section = section

        return super().form_valid(form)

def resume_update_view(request, pk):
    resume = get_object_or_404(models.Resume, pk = pk)
    if request.method == 'POST':
        update_form = ResumeForm(request.POST, instance=resume)
        if update_form.is_valid():
            update_form.save()
    return redirect("resume-list")

class ResumeDeleteView(DeleteView):
    model = models.Resume
    success_url = reverse_lazy("resume-list")

class ResumeSectionUpdateView(UpdateView):
    pass

class ResumeSectionDeleteView(DeleteView):
    pass