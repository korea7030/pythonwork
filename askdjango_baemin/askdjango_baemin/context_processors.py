from django.conf import settings

def baemin(request):
    return {
        'settings' : settings
    }
