from django.shortcuts import redirect
from django.urls import resolve

class RedirectToAPIMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Resolve the requested URL to a view function
        resolver_match = resolve(request.path_info)

        # Check if the resolved view function corresponds to a valid endpoint
        if not resolver_match.view_name.startswith('api:'):
            # If not, redirect to '/api/'
            return redirect('/api/')

        return self.get_response(request)
