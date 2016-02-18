from django.conf.urls import include, url
from django.contrib import admin
from lancerApp import views, extra_views

urlpatterns = [
    # Examples:
    url(r'^personal/', include('clientArea.urls')),
    url(r'^lanceradmin/', include(admin.site.urls)),

    url(r'^media/(?P<path>images/.+(?:\.jpeg|\.jpg|\.png))$', extra_views.media, name='media'),
    url(r'^media/(?P<path>files/.+(?:\.pdf|\.doc|\.docx|\.txt))$', extra_views.media, name='media'),

    url(r'^$', views.home, name='home'),
    url(r'^about/', 'lancerApp.views.about', name='about'),
    url(r'^map/', 'lancerApp.views.map_page', name='map'),
    url(r'^news/', 'lancerApp.views.news', name='news'),
    url(r'^contact/', 'lancerApp.views.contact', name='contact'),
    url(r'^partners/', 'lancerApp.views.partners', name='partners'),
    url(r'^service/(?P<service_id>[0-9]+)', 'lancerApp.views.service', name='service'),
    url(r'^service/', 'lancerApp.views.service', name='service'),
    url(r'^price/(?P<service_type>[-\w]+)', 'lancerApp.views.price', name='price'),
    url(r'^price/', 'lancerApp.views.price', name='price'),
]
