from django.conf.urls import url

from . import views

app_name = 'web'


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^autores/$', views.autores, name='autores'),
    url(r'^autor_detalle/(?P<id>[\w-]+)$', views.autor_detalle, name='autor_detalle'),
]