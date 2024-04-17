from django.shortcuts import redirect
from django.urls import resolve

class RedirectToAPIMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Resolve the requested URL to a view function
        resolver_match = resolve(request.path_info)

        try:
            # Try to resolve the view function for the requested URL
            view_func = resolver_match.func
        except AttributeError:
            # If resolver_match does not have a func attribute, it means the URL could not be resolved.
            # In this case, redirect to '/api/'
            return redirect('/api/')

        # Continue with the request as usual
        return self.get_response(request)
