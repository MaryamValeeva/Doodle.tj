from django.urls import path
from . import views

urlpatterns = [
    path('main', views.show_main, name='show_main'),
    path('a', views.show_about, name='show_about'),
    path('b', views.show_blog, name='show_blog'),
    path('ca', views.show_cases, name='show_cases'),
    path('co', views.show_contact, name='show_contact'),
    path('n', views.show_not_found, name='show_not_found'),
    path('s', views.show_service, name='show_service'),
    path('sol', views.show_solution, name='show_solution'),
    path('t', views.show_technologies, name='show_technologies'),
    path('base', views.show_base, name='show_base'),
    path('base2', views.show_base2, name='show_base2'),
    path('menu', views.show_menu, name='show_menu'),
    path('menu_dop', views.show_menu_dop, name='show_menu_dop'),
]