from .settings import *

AWS = env.bool('AWS')

if AWS:
    INSTALLED_APPS += (
        'django_ses',
    )
    AWS_SES_ACCESS_KEY_ID = env.str('AWS_SES_ACCESS_KEY_ID')
    AWS_SES_SECRET_ACCESS_KEY = env.str('AWS_SES_SECRET_ACCESS_KEY')
    EMAIL_BACKEND = 'django_ses.SESBackend'
