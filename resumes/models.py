from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # template = models.ForeignKey(ResumeTemplate, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True, verbose_name='Чернетка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"
        ordering = ["-created_at"]

class ResumeSection(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    def __str__(self):
        return self.title

class Education(ResumeSection):
    institution = models.CharField(max_length=100, verbose_name="Установа")
    speciality = models.CharField(max_length=100, verbose_name="Спеціальність")
    degree = models.CharField(max_length=255, verbose_name="Степень")
    start_year = models.PositiveIntegerField(verbose_name="Дата початку навчання")
    end_year = models.PositiveIntegerField(blank=True, null=True, verbose_name="Дата закінчення навчання")

class Experience(ResumeSection):
    company = models.CharField(max_length=100, verbose_name="Компанія")
    position = models.CharField(max_length=100, verbose_name="Посада")
    description = models.TextField(max_length=1000, verbose_name="Обов'язки")
    why_fired = models.CharField(max_length=100, verbose_name="Причина звілнення")
    start_date = models.DateField(verbose_name="Дата початку роботи")
    end_date = models.DateField(blank=True, null=True, verbose_name="Дата звільнення")

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва скіла")
    section = models.ForeignKey(ResumeSection, on_delete=models.CASCADE, verbose_name="Секція")\
    
    def __str__(self):
        return f"{self.name} - {self.section.title}"