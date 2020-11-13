from django.conf import settings

def site_common_text(request):
    context = {
        'SITE_NAME': settings.SITE_NAME
    }
    return context
