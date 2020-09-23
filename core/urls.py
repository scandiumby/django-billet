"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from django.views.generic import TemplateView

from core.views import CoreHomeView

app_name = 'core'

urlpatterns = [
    path('core-admin/', admin.site.urls, name="admin"),
    path('', CoreHomeView.as_view(), name='home'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_txt"),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
