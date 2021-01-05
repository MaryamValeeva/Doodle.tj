from django.urls import path
from . import views

urlpatterns = [
    path('main', views.show_main, name='show_main'),
    path('about', views.show_about, name='show_about'),
    path('blog', views.show_blog, name='show_blog'),
    path('cases', views.show_cases, name='show_cases'),
    path('contact', views.show_contact, name='show_contact'),
    path('not_found', views.show_not_found, name='show_not_found'),
    path('service', views.show_service, name='show_service'),
    path('solution', views.show_solution, name='show_solution'),
    path('technologies', views.show_technologies, name='show_technologies'),
    path('base', views.show_base, name='show_base'),
    path('menu', views.show_menu, name='show_menu'),
    path('menu_dop', views.show_menu_dop, name='show_menu_dop'),
    path('footer', views.show_footer, name='show_footer'),
]