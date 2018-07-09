from django.test import TestCase

# Create your tests here.
class AuthRequiredMiddleware(object):
    def process_request(self, request):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse('landing_page')) # or http response
        return None
