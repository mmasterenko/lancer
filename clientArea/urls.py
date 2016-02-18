from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'clientArea.views.visits', name='visits'),
    url(r'^(?P<page_name>[a-z-]+\.html)$', 'clientArea.views.pages', name='pages'),
]
