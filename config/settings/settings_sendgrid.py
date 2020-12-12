import os
from .settings import *

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
SENDGRID_SANDBOX_MODE_IN_DEBUG = os.environ.get('SENDGRID_SANDBOX_MODE_IN_DEBUG')
