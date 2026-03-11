from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ResumeListView.as_view(), name='resume-list'),
    path('<int:pk>', views.resume_detail_view, name='resume-detail'),
    path('create/', views.ResumeCreateView.as_view(), name='resume-create'),
    path('update/<int:pk>', views.resume_update_view, name='resume-update'),
    path('section/create/<int:resume_pk>', views.ResumeSectionCreateView.as_view(), name='resume-section-create'),
    path("resume/<int:resume_pk>/personal-info/create/", views.ResumePersonalInfoCreateView.as_view(), name="resume-personal-info-create"),
    path("resume/<int:resume_pk>/education/create/", views.EducationItemCreateView.as_view(), name="resume-education-create"),
    path("resume/<int:resume_pk>/experiance/create/", views.ExperienceItemCreateView.as_view(), name="resume-experiance-create"),
    path("resume/<int:resume_pk>/skill/create/", views.SkillItemCreateView.as_view(), name="resume-skill-create"),
    # DELETE VIEWS
    path('delete/<int:pk>', views.ResumeDeleteView.as_view(), name='resume-delete'),
    path('personal-info-item/delete/<int:pk>', views.delete_personal_info_item_view, name='personal-info-item-delete'),
    path('education-item/delete/<int:pk>', views.delete_education_item_view, name='education-item-delete'),
    path('experience-item/delete/<int:pk>', views.delete_experience_item_view, name='experience-item-delete'),
    path('skill-item/delete/<int:pk>', views.delete_skill_item_view, name='skill-item-delete'),
    # UPDATE
    path('resume/<int:resume_pk>/personal-info/update/<int:pk>/', views.ResumePersonalInfoUpdateView.as_view(), name='resume-personal-info-update'),
    path('resume/<int:resume_pk>/education/update/<int:pk>/', views.ResumeEducationUpdateView.as_view(), name='resume-education-update'),
    path('resume/<int:resume_pk>/experience/update/<int:pk>/', views.ResumeExperienceUpdateView.as_view(), name='resume-experience-update'),
    path('resume/<int:resume_pk>/skill/update/<int:pk>/', views.ResumeSkillUpdateView.as_view(), name='resume-skill-update'),

]