import environ
from .settings import *

env = environ.Env()

EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = env.str('SENDGRID_API_KEY')
SENDGRID_SANDBOX_MODE_IN_DEBUG = env.bool('SENDGRID_SANDBOX_MODE_IN_DEBUG')
