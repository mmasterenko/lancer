from django.conf.urls import include, url
from django.contrib import admin
from lancerApp import views

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.home, name='home'),
    url(r'^about/', 'lancerApp.views.about', name='about'),
    url(r'^map/', 'lancerApp.views.map_page', name='map'),
    url(r'^news/', 'lancerApp.views.news', name='news'),
    url(r'^contact/', 'lancerApp.views.contact', name='contact'),
    url(r'^partners/', 'lancerApp.views.partners', name='partners'),
    url(r'^service/', 'lancerApp.views.service', name='service'),
]
