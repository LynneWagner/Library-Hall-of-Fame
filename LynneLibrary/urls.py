from django.conf.urls import include, url
from django.contrib import admin
from tracker import views

urlpatterns = (
    url(r'^tracker/', include('tracker.urls')),
    url(r'^admin/', admin.site.urls),
)
