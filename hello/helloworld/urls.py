from django.conf.urls import include, url
#from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^$', views.helloworld, name='helloworld'),
   # url(r'^admin/', admin.site.urls),
]
