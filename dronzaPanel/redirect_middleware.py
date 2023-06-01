from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class RedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()

        if host.startswith('www.'):
            new_host = host[4:]
            url = request.build_absolute_uri().replace(host, new_host, 1)
            return HttpResponsePermanentRedirect(url)

        return self.get_response(request)