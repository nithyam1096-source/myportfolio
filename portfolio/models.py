from django.db import models
from django.utils.text import slugify

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('database', 'Database'),
        ('tools', 'Tools & Others'),
    ]

    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, help_text='Font Awesome icon class (e.g., fab fa-python)')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='backend')
    proficiency = models.IntegerField(default=80, help_text='Skill proficiency percentage (0-100)')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text='Comma-separated list of technologies')
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    live_demo_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.technologies.split(',')]


class Resume(models.Model):
    full_name = models.CharField(max_length=200, default='Nithya M')
    title = models.CharField(max_length=200, default='Python Full Stack Developer')
    summary = models.TextField(blank=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Resumes'

    def __str__(self):
        return f'Resume - {self.full_name}'


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=300)
    university = models.CharField(max_length=300)
    cgpa = models.CharField(max_length=20)
    year_passed = models.CharField(max_length=20)
    icon_class = models.CharField(max_length=100, default='fas fa-graduation-cap')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Education'

    def __str__(self):
        return f'{self.degree} - {self.institution}'


class Certification(models.Model):
    title = models.CharField(max_length=300)
    issuer = models.CharField(max_length=200)
    date_earned = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True, null=True)
    icon_class = models.CharField(max_length=100, default='fas fa-certificate')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', '-date_earned']

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    icon_class = models.CharField(max_length=100, default='fas fa-briefcase')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f'{self.title} at {self.company}'


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.subject}'
