from django.db import models
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

# Create your models here.

class Dolzhnost(models.Model):
    """Должность"""
    name = models.CharField(_('Name'), max_length=100)
    code = models.CharField(_('Code'), max_length=10)

    def __str__(self):
        return (self.name)



def update_filename(instance, filename):
    return 'static/pics/{0}.jpg'.format(instance.id)

class People(models.Model):
    """Руководители"""
    FEMALE = 0
    MALE = 1
    GENDER_CHOICE = ((FEMALE, _("female")), (MALE, _("male")))

    first_name = models.CharField(_('first name'), max_length=30, blank=True, null=True)
    middle_name = models.CharField(_('middle name'), max_length=30, blank=True, null=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True, null=True)
    phone = models.CharField(_('phone'), max_length=40, blank=True, null=True)
    gender = models.BooleanField(_('gender'), choices=GENDER_CHOICE, default=MALE)
    birth_date = models.DateField(_('Birth date'), blank=True, null=True)

    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))

    picture = models.ImageField(verbose_name="Picture", blank=True, null=True, upload_to=update_filename)
    dolzhnost = models.ForeignKey(Dolzhnost, verbose_name=_('Dolzhnost'), null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)


class About(models.Model):
    """О нас"""
    
    about_us = models.CharField(_('About us'), max_length=500)
    history = models.CharField(_('History'), max_length=1000)
    znachenie_nazvaniya = models.CharField(_('Znachenie_nazvaniya'), max_length=500)
    princips_of_work =  models.CharField(_('Princips_of_work'), max_length=500)


    def __str__(self):
        return '%s' % (self.about_us)

def update_filenamephoto(instance, filename):
    return 'static/OurPhotos/{0}.jpg'.format(instance.id)

class OurPhotos(models.Model):
    """О нас"""
    picture = models.ImageField(verbose_name="Picture", blank=True, null=True, upload_to=update_filenamephoto)
        

    def __str__(self):
        return '%s' % (self.picture)

class FrameworkCategories(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    code = models.CharField(_('Code'), max_length=10)
    text = models.CharField(_('Text'), max_length=1000)
    position = models.IntegerField(_('Position'), default=0)

    def __str__(self):
        return '%s - %s' % (self.name, self.code)

class Technologies(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    code = models.CharField(_('Code'), max_length=10)
    svg = models.CharField(_('Svg'), max_length=105000)
    framework_categories = models.ForeignKey(FrameworkCategories, verbose_name=_('Framework Categories'), null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.name)


class Main(models.Model):
    main_words = models.CharField(_('main_words'), max_length=150)
    sub_words = models.CharField(_('sub_words'), max_length=150)

    def __str__(self):
        return '%s' % (self.main_words)

class Development(models.Model):
    name = models.CharField(_('name'), max_length=50)
    text = models.CharField(_('text'), max_length=200)
    svg = models.CharField(_('Svg'), max_length=5000, default=0)
    position = models.IntegerField(_('Position'), default=0)

    def __str__(self):
        return '%s' % (self.name)
