import os
from .settings import *

if not DEBUG:
    LOGGING = {
        'version' : 1,
        'disable_existing_loggers' : False,
        
        'loggers' : {
            'django' : {
                'handlers' : ['file'],
                'level' : 'INFO',
                'propagate' : False,
            },
            'app' : {
                'handlers' : ['file'],
                'level' : 'INFO',
                'propagate' : False,
            },
            'console' : {
                'handlers' : ['console'],
                'level' : 'INFO',
                'propagate' : False,
            },
        },
        'handlers' : {
            'console' : {
                'level' : 'INFO',
                'class' : 'logging.StreamHandler',
                'formatter' : 'prod',
            },
            'file' : {
                'level' : 'INFO',
                'class' : 'logging.handlers.TimedRotatingFileHandler',
                'filename' : os.path.join(BASE_DIR, 'logs/django.log'),
                'when' : 'D',
                'interval' : 1,
                'backupCount' : 7,
                'formatter' : 'prod',
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
                'formatter': 'prod',
            },
        },
        'formatters' : {
            'prod' : {
                'format' : '\t'.join([
                    '%(asctime)s',
                    '[%(levelname)s]',
                    '%(pathname)s(Line:%(lineno)d)',
                    '%(message)s',
                ]),
            },
        },
    }
