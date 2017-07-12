from base import *
import dj_database_url
import settings


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


DATABASES['default'] = dj_database_url.config("CLEARDB_DATABASE_URL")

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_ch3eEaRHvrtWq2jb28V5PRfX')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_nfZf9yc1njMtRqBdVndurV0m')

# PayPal environment variables
SITE_URL = 'https://protected-waters-31864.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'https://protected-waters-31864.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'conradcoyle-facilitator@gmail.com'