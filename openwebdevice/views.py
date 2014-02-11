from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.views.static import serve

    
def conditional_serve(request, path='', document_root=None):
    if request.META['HTTP_HOST'] != settings.CANONICAL_HTTP_HOST:
        return HttpResponsePermanentRedirect(
            'http://%s/%s' % (settings.CANONICAL_HTTP_HOST, path))
    document_root = document_root or settings.STATIC_ROOT
    if not path:
        path = '/index.html'
    elif path.endswith('/'):
        path += 'index.html'
    return serve(request, path=path, document_root=document_root)
