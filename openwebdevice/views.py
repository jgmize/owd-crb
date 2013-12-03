from django.views.static import serve
from django.conf import settings


def conditional_serve(request, path='', document_root=None):
    document_root = document_root or settings.STATIC_ROOT
    if not path:
        path = '/index.html'
    if path.endswith('/'):
        path += 'index.html'
    return serve(request, path=path, document_root=document_root)
