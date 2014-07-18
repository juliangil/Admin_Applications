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

    url(r'^login/', 'adminApplications.views.login', name='login'),
    url(r'^inicio/', 'adminApplications.views.inicio', name='inicio'),
    url(r'^register/', 'adminApplications.views.register', name='register'),
    url(r'^newDevice/', 'adminApplications.views.newDevice', name='newDevice'),
    url(r'^newApplication/', 'adminApplications.views.newApplication', name='newApplication'),
    url(r'^allDevices/', 'adminApplications.views.allDevices', name='allDevices'),
    url(r'^allApplications/', 'adminApplications.views.allApplications', name='allApplications'),
    url(r'^oneDevice/', 'adminApplications.views.oneDevice', name='oneDevice'),
    url(r'^oneApplication/', 'adminApplications.views.oneApplication', name='oneApplication'),
    url(r'^installApplications/', 'adminApplications.views.installApplications', name='installApplications'),
    url(r'^deviceDetails/', 'adminApplications.views.deviceDetails', name='deviceDetails'),
    url(r'^applicationDetails/', 'adminApplications.views.applicationDetails', name='applicationDetails'),
]
