from django.contrib.auth import get_user_model
from django.db import models


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


class TMSITIContact(models.Model):
    fullname = models.CharField(max_length=500)
    email = models.EmailField()
    phone_number = models.IntegerField()
    management = models.ForeignKey(TMSITIManagement, on_delete=models.CASCADE)
    appeal_text = models.TextField()
    appeal_file = models.FileField(upload_to='appeals/', null=True)


class TMSITIElecStandards(AbstractBaseModel):
    doc_number = models.IntegerField()
    doc_title = models.CharField(max_length=500)
    doc_type = models.CharField(max_length=500)
    doc_sign = models.CharField(max_length=500, null=True)
    doc_approved_year = models.IntegerField()

    def __str__(self):
        return f"{self.doc_title} | {self.doc_type} | {self.doc_sign}"

    class Meta:
        verbose_name_plural = 'ElecStandards'
        db_table = 'elec_standards'


class TMSITIBuildingReglements(AbstractBaseModel):
    reglement_number = models.IntegerField()
    reglement_code = models.CharField(max_length=10)
    reglement_title = models.CharField(max_length=500)
    reglement_file = models.FileField(upload_to='buildings/')

    def __str__(self):
        return f"{self.reglement_code} | {self.reglement_title}"


class TMSITISubsystem(AbstractBaseModel):
    subsystem_number = models.IntegerField()
    subsystem_title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.subsystem_number} | {self.subsystem_title}"


class TMSITIGroup(AbstractBaseModel):
    group_number = models.IntegerField()
    group_name = models.CharField(max_length=255)
    group_subsystem = models.ForeignKey(TMSITISubsystem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group_number} | {self.group_name}"

    class Meta:
        verbose_name_plural = 'Groups'
        db_table = 'groups'


class TMSITISHNK(AbstractBaseModel):
    SHNK_code = models.CharField(max_length=10)
    SHNK_date = models.CharField(max_length=128)
    SHNK_title = models.CharField(max_length=255)
    SHNK_file_uz = models.FileField(upload_to='shnks/')
    SHNK_file_ru = models.FileField(upload_to='shnks/')
    SHNK_group = models.ForeignKey(TMSITIGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.SHNK_code} | {self.SHNK_date} | {self.SHNK_title}"

    class Meta:
        verbose_name_plural = 'SHNKS'
        db_table = 'shnks'


class TMSITIDictionary(models.Model):
    word_name_uz = models.CharField(max_length=255, unique=True, db_index=True)
    word_name_ru = models.CharField(max_length=255, unique=True, db_index=True)
    word_name_en = models.CharField(max_length=255, unique=True, db_index=True)
    word_name_turk = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return f"{self.word_name_uz} | {self.word_name_en} | {self.word_name_ru} | {self.word_name_turk}"

    class Meta:
        verbose_name_plural = 'TMSITIDictionaries'
        db_table = "dictionary"
        indexes = [
            models.Index(fields=['word_name_uz']),
            models.Index(fields=['word_name_ru']),
            models.Index(fields=['word_name_en']),
            models.Index(fields=['word_name_turk']),
        ]
