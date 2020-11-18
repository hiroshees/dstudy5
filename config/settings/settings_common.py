
# flash message storage
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert alert-secondary',
    messages.INFO: 'alert alert-info',
    messages.SUCCESS: 'alert alert-success',
    messages.WARNING: 'alert alert-warning',
    messages.ERROR: 'alert alert-danger',
}
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

USE_X_FORWARDED_HOST = True

SITE_NAME = "宴会くん"

