from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'clientArea.views.visits', name='visits'),
]
