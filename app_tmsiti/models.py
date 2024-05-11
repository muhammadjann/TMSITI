from django.db import models
import datetime
from uuid import uuid4
from django.contrib.auth import get_user_model


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class TMSITINews(AbstractBaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateField()
    image = models.ImageField(upload_to='news/')

    class Meta:
        ordering = ['-date_published']
        verbose_name_plural = 'News'
        verbose_name = 'News'
        db_table = 'news'

    def __str__(self):
        return self.title


class TMSITIAnnouncement(AbstractBaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateField()

    class Meta:
        ordering = ['-date_published']
        verbose_name_plural = 'Announcements'
        verbose_name = 'Announcement'
        db_table = 'announcement'

    def __str__(self):
        return self.title


class TMSITIManagement(AbstractBaseModel):
    job_name = models.CharField(max_length=500, null=False, blank=False)
    fullname = models.CharField(max_length=500, null=False, blank=False)
    admission_days = models.CharField(max_length=500)
    phone_number = models.IntegerField()
    email = models.EmailField(),
    specialization_bachelor = models.CharField(max_length=500)
    master_specialty = models.CharField(max_length=500)
    employee_image = models.ImageField(upload_to='employees/')

    def __str__(self):
        return f"{self.fullname} | {self.job_name} | {self.phone_number}"

    class Meta:
        verbose_name_plural = 'Managements'
        db_table = 'managements'


class TMSITIStructuralDivision(AbstractBaseModel):
    staff_job = models.CharField(max_length=255)
    staff_fullname = models.CharField(max_length=255)
    staff_phone_number = models.IntegerField()
    staff_email = models.EmailField()

    def __str__(self):
        return f"{self.staff_fullname} | {self.staff_job}"

    class Meta:
        verbose_name_plural = 'StructuralDivisions'
        db_table = 'structural_division'


class TMSITIStandard(AbstractBaseModel):
    standard_name = models.CharField(max_length=50)
    standard_code = models.IntegerField()
    standard_title = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.standard_name} | {self.standard_code} | {self.standard_title}"

    class Meta:
        verbose_name_plural = 'Standards'
        db_table = 'standards'
