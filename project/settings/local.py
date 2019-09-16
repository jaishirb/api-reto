from .base import *

DEBUG = True

redis_host = os.environ.get('REDIS_HOST', 'localhost')

# Channel layer definitions
# http://channels.readthedocs.org/en/latest/deploying.html#setting-up-a-channel-backend
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [(redis_host, 6379)],
        },
        "ROUTING": "project.routing.channel_routing",
    },
}

ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [

]

WSGI_APPLICATION = 'project.wsgi.local.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'apireto',
        'USER': 'admin',
        'PASSWORD': '99102605167Jbc?!:',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
