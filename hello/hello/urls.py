"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import newbie.views as newbie
urlpatterns = [
    url(r'^admin/', admin.site.urls),
#   url(r'^helloworld/', include('helloworld.urls')),
#   url(r'^$', helloworld.main),
    url(r'^$', newbie.user_login),
    url(r'^signup/', newbie.user_signup),
    url(r'^logout/', newbie.user_logout),
    url(r'^main/', newbie.main),
    url(r'^mypage/', newbie.mypage),
    url(r'^pato/', newbie.pato),
    url(r'^timetable/', newbie.timetable),
    url(r'^submit/station/', newbie.submit1),
    url(r'^submit/bus1/', newbie.submit2),
    url(r'^submit/bus2/', newbie.submit3),
]
