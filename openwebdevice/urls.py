from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    (r'(?P<path>.*)', 'openwebdevice.views.conditional_serve', {'document_root' : settings.STATIC_ROOT})
)
