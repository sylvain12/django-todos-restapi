import os
from .base import *

try:
    DJANGO_APP_ENV = os.environ.get('DJANGO_APP_ENV')
    print(DJANGO_APP_ENV)
except EnvironmentError as err:
    raise EnvironmentError(
        'You need to set DJANGO_APP_ENV (dev or prod)!') from err

if DJANGO_APP_ENV == 'dev':
    from .dev import *
else:
    from .prod import *
