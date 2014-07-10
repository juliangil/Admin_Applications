from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'adminApplications.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', 'adminApplications.views.hello'), 

    # Activamos la url de los mediafiles

    url(r'^', 'adminApplications.views.inicio'),
    url(r'^inicio', 'adminApplications.views.inicio'),
    url(r'^newDevice', 'adminApplications.views.inicio'),
    url(r'^newApplication', 'adminApplications.views.inicio'),
    url(r'^allDevices', 'adminApplications.views.inicio'),
    url(r'^allApplications', 'adminApplications.views.inicio'),
    url(r'^oneDevice', 'adminApplications.views.inicio'),
    url(r'^oneApplication', 'adminApplications.views.inicio'),
    url(r'^installApplications', 'adminApplications.views.inicio'),
    url(r'^deviceDetails', 'adminApplications.views.inicio'),
    url(r'^applicationDetails', 'adminApplications.views.inicio'),
    url(r'^register', 'adminApplications.views.inicio'),
]
