from django.contrib import admin
from django.urls import path, include
from .views import resume_detail_view, EducationItemCreateView, ResumeSectionCreateView, ResumeListView, ResumeCreateView, ResumeDeleteView, resume_update_view, ResumeSectionUpdateView, ResumeSectionDeleteView, ResumePersonalInfoCreateView

urlpatterns = [
    path('', ResumeListView.as_view(), name='resume-list'),
    path('<int:pk>', resume_detail_view, name='resume-detail'),
    path('create/', ResumeCreateView.as_view(), name='resume-create'),
    path('update/<int:pk>', resume_update_view, name='resume-update'),
    path('delete/<int:pk>', ResumeDeleteView.as_view(), name='resume-delete'),
    path('section/create/<int:resume_pk>', ResumeSectionCreateView.as_view(), name='resume-section-create'),
    path('section/update/', ResumeSectionUpdateView.as_view(), name='resume-section-update'),
    path('section/delete/', ResumeSectionDeleteView.as_view(), name='resume-section-delete'),
    path("resume/<int:resume_pk>/personal-info/create/", ResumePersonalInfoCreateView.as_view(), name="resume-personal-info-create"),
    path("resume/<int:resume_pk>/education/create/", EducationItemCreateView.as_view(), name="resume-education-create"),
]