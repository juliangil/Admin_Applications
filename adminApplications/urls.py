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

    url(r'^inicio', 'adminApplications.views.inicio'),
    url(r'^register', 'adminApplications.views.register'),
    url(r'^newDevice', 'adminApplications.views.newDevice'),
    url(r'^newApplication', 'adminApplications.views.newApplication'),
    url(r'^allDevices', 'adminApplications.views.allDevices'),
    url(r'^allApplications', 'adminApplications.views.allApplications'),
    url(r'^oneDevice', 'adminApplications.views.oneDevice'),
    url(r'^oneApplication', 'adminApplications.views.oneApplication'),
    url(r'^installApplications', 'adminApplications.views.installApplications'),
    url(r'^deviceDetails', 'adminApplications.views.deviceDetails'),
    url(r'^applicationDetails', 'adminApplications.views.applicationDetails'),
]
