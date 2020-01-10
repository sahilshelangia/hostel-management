"""gpm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from accounts.views import index, contact, contactUs, read_file1, read_file2
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name='index'),
                  path('accounts/', include('accounts.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('gatepass/', include('gatepass_apply.urls')),
                  path('approve/', include('gatepass_approve.urls')),
                  path('manager/', include('manager.urls')), 
                  path('contactUs/', contactUs, name='contactUs'), 
                  path('contact/', contact, name='contact'),
                  path('.well-known/acme-challenge/NAfTgP4hg6-89zx5DTWnuWJ6UpZqK7-ScWj6zF-IbF0', read_file1, name='readfile1'),
                  path('.well-known/acme-challenge/Ku3EbN4vJ4p3BPM2NWST1_YTNf-kSP4Zk2UlhOvp3h4', read_file2, name='readfile2'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
