from base import *


DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_ch3eEaRHvrtWq2jb28V5PRfX')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_nfZf9yc1njMtRqBdVndurV0m')

# PayPal environment variables
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://98de0985.ngrok.io/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'conradcoyle-facilitator@gmail.com'

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]