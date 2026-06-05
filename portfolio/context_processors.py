from .models import Resume, Education, Certification, Experience, Skill, Project

def portfolio_context(request):
    resume = Resume.objects.filter(is_active=True).first()
    educations = Education.objects.filter(is_active=True)
    certifications = Certification.objects.filter(is_active=True)
    experiences = Experience.objects.filter(is_active=True)
    skills = Skill.objects.filter(is_active=True)
    projects = Project.objects.filter(is_active=True)

    return {
        'resume': resume,
        'educations': educations,
        'certifications': certifications,
        'experiences': experiences,
        'skills': skills,
        'projects': projects,
        'portfolio_name': 'Nithya M',
        'portfolio_role': 'Python Full Stack Developer',
        'portfolio_email': 'nithyam1096@gmail.com',
        'portfolio_location': 'Bangalore, Karnataka',
    }
