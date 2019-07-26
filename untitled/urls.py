"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pollapp import views
from untitled import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('registration/',include('pollapp.urls')),
    path('poll_app/',include('servayapp.urls')),
    path('contact-us',views.contact_us,name='contact_us'),
    path('about-us',views.about_us,name='about_us')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
