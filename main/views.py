from django.shortcuts import render
from .models import Dolzhnost, People, About, OurPhotos, FrameworkCategories, Technologies, Main, Development

# Create your views here.
def show_main(request):
    main=Main.objects.all()[0]    
    develop=Development.objects.all()
    return render(request, 'main/main.html', {"main":main, "development":develop})

def show_about(request):
    dol=Dolzhnost.objects.all()
    peo=People.objects.all()
    about=About.objects.all()[0]
    ourPh=OurPhotos.objects.all()
    return render(request, 'main/about.html', {"about":about, "dolzhnost":dol, "people":peo, "OurPhotos":ourPh})

def show_blog(request):
    return render(request, 'main/blog.html', {})

def show_cases(request):
    return render(request, 'main/cases.html', {})

def show_contact(request):
    return render(request, 'main/contact.html', {})

def show_not_found(request):
    return render(request, 'main/not_found.html', {})

def show_service(request):
    return render(request, 'main/service.html', {})

def show_solution(request):
    return render(request, 'main/solution.html', {})

def show_technologies(request):
    categories=FrameworkCategories.objects.all()
    technologies=Technologies.objects.all()

    return render(request, 'main/technologies.html', {"technologies":technologies, "categories": categories})

def show_base(request):
    return render(request, 'main/base.html', {})

def show_base2(request):
    return render(request, 'main/base2.html', {})

def show_menu(request):
    return render(request, 'main/menu.html', {})

def show_menu_dop(request):
    return render(request, 'main/menu_dop.html', {})