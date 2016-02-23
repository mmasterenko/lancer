from django.conf.urls import url

urlpatterns = [
    url(r'^(?:index.html)?$', 'clientArea.views.visits', name='visits'),
    url(r'^login\.html$', 'clientArea.views.login_view', name='login'),
    url(r'^logout$', 'clientArea.views.logout_view', name='logout'),
    # url(r'^(?P<page_name>[a-z-]+\.html)$', 'clientArea.views.pages', name='pages'),
]
