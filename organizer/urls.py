"""resultMaker URL Configuration

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

from django.contrib import admin
from django.urls import path,include

from .views import HomeView
from student import urls as studentURL
from examination import urls as examURL
from users import urls as userURL
from result import urls as resultURL
from study import urls as studyURL

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('student/',include(studentURL)),
    path('exam/', include(examURL)),
    path('user/', include(userURL, namespace='dj-auth')),
    path('result/', include(resultURL)),
    path('study/', include(studyURL))
]
