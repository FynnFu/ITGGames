from Home.models import *


class ModelsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        request.menuLink = Link.objects.all()
        request.menuDropdownLink = DropdownLink.objects.all()
        request.footerSocialMedia = SocialMedia.objects.all()
        request.imageLogo = Logo.objects.all()

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
