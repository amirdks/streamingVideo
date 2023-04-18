from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponseForbidden


class AmirMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request: HttpRequest):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.user.is_authenticated)
        path = request.GET.get("path")
        if path:
            if r"media\\videos" in path:
                return HttpResponseForbidden()
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
