import os
from .settings import *

LOGGING = {
    'version' : 1,
    'disable_existing_loggers' : False,
    
    'loggers' : {
        'django' : {
            'handlers' : ['console'],
            'level' : 'INFO',
        },
        'app' : {
            'handlers' : ['console'],
            'level' : 'INFO',
        }
    },
    'handlers' : {
        'console' : {
            'level' : 'INFO',
            'class' : 'logging.StreamHandler',
            'formatter' : 'dev',
        },
        'file' : {
            'level' : 'INFO',
            'class' : 'logging.handlers.TimedRotatingFileHandler',
            'filename' : os.path.join(BASE_DIR, 'logs/django.log'),
            'when' : 'D',
            'interval' : 1,
            'backupCount' : 7,
            'formatter' : 'dev',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'dev',
        },
    },
    'formatters' : {
        'dev' : {
            'format' : '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ]),
        },
    },
}
