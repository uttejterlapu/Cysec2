# your_app/middleware.py

from django.http import HttpResponseRedirect
from django.conf import settings

class SessionExpiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated and not request.session.get_expiry_age():
            # If session is expired, redirect to login page
            return HttpResponseRedirect(settings.LOGIN_URL)

        return response
