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

class EducationItem(models.Model):
    section = models.ForeignKey(ResumeSection, on_delete=models.CASCADE, verbose_name="Секція")
    institution = models.CharField(max_length=100, verbose_name="Навчальний заклад")
    speciality = models.CharField(max_length=100, verbose_name="Спеціальність")
    city = models.CharField(max_length=100, verbose_name="Місто")
    degree = models.CharField(max_length=255, verbose_name="Ступінь")
    start_year = models.DateField(verbose_name="Дата початку навчання")
    end_year = models.DateField(blank=True, null=True, verbose_name="Дата закінчення навчання")
    description = models.TextField(max_length=1000, verbose_name="Опис")

    def __str__(self):
        return f"{self.institution} - {self.speciality}"

class ExperienceItem(models.Model):
    section = models.ForeignKey(ResumeSection, on_delete=models.CASCADE, verbose_name="Секція")
    company = models.CharField(max_length=100, verbose_name="Компанія")
    position = models.CharField(max_length=100, verbose_name="Посада")
    city = models.CharField(max_length=100, verbose_name="Місто")
    why_fired = models.CharField(max_length=100, verbose_name="Причина звілнення")
    start_date = models.DateField(verbose_name="Дата початку роботи")
    end_date = models.DateField(blank=True, null=True, verbose_name="Дата звільнення")
    description = models.TextField(max_length=1000, verbose_name="Опис")

    def __str__(self):
        return f"{self.company} - {self.position}"


class SkillItem(models.Model):
    section = models.ForeignKey(ResumeSection, on_delete=models.CASCADE, verbose_name="Секція")
    name = models.CharField(max_length=100, verbose_name="Назва скіла")

    def __str__(self):
        return self.name

class PrivateInformationItem(models.Model):
    GENDER_CHOICES = [
        ("-", "Не обрано"),
        ("female", "Жіноча"),
        ("male", "Чоловіча"),
    ]
    MARITAL_CHOICES = [
        ("married", "Одружений"),
        ("not_married", "Не одружений"),
    ]
    first_name = models.CharField(max_length=15, verbose_name="Ім'я")
    last_name = models.CharField(max_length=15, verbose_name="Прізвище")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата народження")
    avatar = models.ImageField(upload_to='resume_avatars/', null=True, blank=True, verbose_name="Аватар")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Електронна адреса")
    city = models.CharField(max_length=100, verbose_name="Місто проживання")
    gender = models.CharField(max_length=9, choices=GENDER_CHOICES, verbose_name="Стать")
    marial = models.CharField(max_length=15, choices=MARITAL_CHOICES, verbose_name="Сімейний стан")
    github_link = models.URLField(max_length=300, blank=True, null=True, verbose_name="Посилання на Гітхаб")
    other_link = models.URLField(max_length=300, blank=True, null=True, verbose_name="Посилання")
    section = models.ForeignKey(ResumeSection, on_delete=models.CASCADE, verbose_name="Секція")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.section.pk}"

    class Meta:
        verbose_name = "Персональна інформація"
        verbose_name_plural = "Персональна інформація"