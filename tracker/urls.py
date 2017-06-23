from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

app_name = 'tracker'

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^register/$', views.IndexView.as_view(), name='register'),
    url(r'^$', views.index, name='index'),
    url(r'^tracker/', views.index, name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #url(r'^checkout/$', templates.checkout, name='checkout'),
    url(r'^book/(?P<book_id>[0-9]+)/$', views.detail, name='book_detail'),
    url(r'^dvd/(?P<dvd_id>[0-9]+)/$', views.dvd_detail, name='dvd_detail'),
    url(r'^mag/(?P<mag_id>[0-9]+)/$', views.mags_detail, name='mags_detail'),
    url(r'^newspaper/(?P<newspaper_id>[0-9]+)/$', views.newspaper_detail, name='newspaper_detail'),
    url(r'^music/(?P<mumsic_id>[0-9]+)/$', views.music_detail, name='music_detail'),
]

