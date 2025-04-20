from django.shortcuts import redirect
from import_receipt.models import SiteSetting


class GoogleLoginToggleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Only apply this logic to social Google login path
        if request.path.startswith("/accounts/google/"):
            setting = SiteSetting.objects.first()
            if setting and not setting.google_login_enabled:
                return redirect("/")  # Or show a custom page
        return self.get_response(request)
