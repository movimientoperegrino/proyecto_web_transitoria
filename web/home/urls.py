from django.conf.urls import patterns, url


urlpatterns = patterns(
    'home.views',
    url(r'^$', 'index_view', name='vista_inicio'),
)