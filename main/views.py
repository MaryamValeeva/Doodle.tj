from django.shortcuts import render
from .models import Dolzhnost, People, About, OurPhotos, FrameworkCategories, Technologies, Main, Development

# Create your views here.
def show_main(request):
    main=Main.objects.all()[0]    
    develop=Development.objects.all()
    categories=FrameworkCategories.objects.all()
    technologies=Technologies.objects.all()

    return render(request, 'main/main.html', {"main":main, "development":develop, "technologies":technologies, "categories": categories})

def show_about(request):
    dol=Dolzhnost.objects.all()
    peo=People.objects.all()
    about=About.objects.all()[0]
    ourPh=OurPhotos.objects.all()
    categories=FrameworkCategories.objects.all()
    technologies=Technologies.objects.all()

    return render(request, 'main/about.html', {"about":about, "dolzhnost":dol, "people":peo, "OurPhotos":ourPh, "technologies":technologies, "categories": categories})

def show_blog(request):
    categories=FrameworkCategories.objects.all()
    technologies=Technologies.objects.all()

    return render(request, 'main/blog.html', {"technologies":technologies, "categories": categories})

def show_cases(request):
    categories=FrameworkCategories.objects.all()
    technologies=Technologies.objects.all()

    return render(request, 'main/cases.html', {"technologies":technologies, "categories": categories})

def show_contact(request):
    categories=FrameworkCategories.objects.all()
    technologies=Technologies.objects.all()

    return render(request, 'main/contact.html', {"technologies":technologies, "categories": categories})

def show_not_found(request):
    categories=FrameworkCategories.objects.all()
    technologies=Technologies.objects.all()
    
    return render(request, 'main/not_found.html', {"technologies":technologies, "categories": categories})

def show_service(request):
    categories=FrameworkCategories.objects.all()
    technologies=Technologies.objects.all()

    return render(request, 'main/service.html', {"technologies":technologies, "categories": categories})
    

def show_solution(request):
    categories=FrameworkCategories.objects.all()
    technologies=Technologies.objects.all()

    return render(request, 'main/solution.html', {"technologies":technologies, "categories": categories})


def show_technologies(request):
    categories=FrameworkCategories.objects.all()
    technologies=Technologies.objects.all()

    return render(request, 'main/technologies.html', {"technologies":technologies, "categories": categories})

def show_base(request):
    categories=FrameworkCategories.objects.all()
    technologies=Technologies.objects.all()

    return render(request, 'main/base.html', {"technologies":technologies, "categories": categories})

def show_menu(request):
    categories=FrameworkCategories.objects.all()
    technologies=Technologies.objects.all()

    return render(request, 'main/menu.html', {"technologies":technologies, "categories": categories})

def show_footer(request):
    return render(request, 'main/footer.html', {})

def show_menu_dop(request):
    return render(request, 'main/menu_dop.html', {})