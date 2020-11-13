from .settings import *

if DEBUG:
    def show_toolbar(request):
        return True
    
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

