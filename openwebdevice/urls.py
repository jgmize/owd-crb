from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'(?P<path>.*)', 'openwebdevice.views.conditional_serve', {'document_root' : settings.STATIC_ROOT})
)
