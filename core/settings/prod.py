# Production configs
DEBUG = False

ALLOWED_HOSTS = [
    'https://django-todos-api.herokuapp.com',
    'http://django-todos-api.herokuapp.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd6n4sdlvr27lbb',
        'USER': 'wqkdululrgzsxe',
        'PASSWORD': '7c3f1f7fc7dbcaee9fe4172ef78e5588f4628bc03924a6805889e365aee7cbdb',
        'HOST': 'ec2-54-242-43-231.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# Django Cors headers
CORS_ALLOWED_ORIGINS = [

]
