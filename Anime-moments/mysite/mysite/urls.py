"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
import land.views as land
import edits.views as edits
import subscription.views as sub
import register.views as reg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('land/', land.Land.as_view(), name='land'),
    path('edits', edits.Edits.as_view(), name='edits'),
    path('subscription/', sub.Subscription.as_view(), name='subscription'),
    path('register/', reg.Register.as_view(), name='register'),
    path('accounts/', include('register.urls')),
]
