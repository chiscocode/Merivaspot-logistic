from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('tracking/', views.tracking, name='tracking'),
    path('faq/', views.faq, name='faq'),
    path('rider/', views.rider, name='rider'),
    path('assignment/', views.assignment, name='assignment'),
    path('loginrider/', views.login, name='login'),
    path('registerrider/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('search', views.search, name='search'),                                                                                                                                                                                                      

   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)