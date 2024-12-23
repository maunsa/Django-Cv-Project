from lib2to3.fixes.fix_input import context
from linecache import cache

from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialMedia, Document


# Create your views here.

def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''

    return obj


def get_image_setting(parameter):
    try:
        obj = ImageSetting.objects.get(name=parameter).file
    except:
        obj = ''

    return obj


def layout(request):

    # DOCUMENTS
    documents = Document.objects.all()  # Document queryset'ini ekleyin

    site_title = get_general_setting('site_title')
    site_keywords =  get_general_setting('site_keywords')
    site_description =  get_general_setting('site_description')
    home_banner_name = get_general_setting('home_banner_name')
    home_banner_title =  get_general_setting('home_banner_title')
    home_banner_description =  get_general_setting('home_banner_description')
    about_myself_welcome =  get_general_setting('about_myself_welcome')
    about_myself_footer =  get_general_setting('about_myself_footer')

    social_medias = SocialMedia.objects.all()

    # IMAGES
    home_banner_image = get_image_setting('home_banner_image')

    context = {
        'documents': documents,
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'home_banner_name': home_banner_name,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        'home_banner_image': home_banner_image,
        'social_medias': social_medias,

    }
    return context

def index(request):


    #SKILLS
    skills = Skill.objects.all()

    experiences = Experience.objects.all().order_by('-start_date')

    educations = Education.objects.all().order_by('-start_date')



    context = {
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
    }

    return render(request, 'index.html',context=context)


def redirect_urls(request, slug):
    doc = get_object_or_404(Document, slug=slug)
    return redirect(doc.file.url)

