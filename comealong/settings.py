"""
Django settings for comealong project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'idi2wp2c6-$zz=+yqqfw*w*ttmd^s8@h$k)lx)!tz7uy&-er$h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["comealong.dei.uc.pt", "www.comealong.dei.uc.pt"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',

    'south',
    'social.apps.django_app.default',
    'bootstrap3',
    'redactor',
    #'debug_toolbar',

    'my_user',
    'project',
    'topic',

    'notifications',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.contrib.auth.context_processors.auth',
    "django.core.context_processors.media",
    #"django.core.context_processors.request",
    #'django.contrib.messages.context_processors.auth',
)


ROOT_URLCONF = 'comealong.urls'

WSGI_APPLICATION = 'comealong.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#-----------------------------------------------------------------------------------

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "ui/static"),
)

#Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
MEDIAFILES_DIRS = (
    os.path.join(BASE_DIR, "media"),
)

#Templates
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "ui/templates"),
)
#-----------------------------------------------------------------------------------

#AUTH
AUTH_USER_MODEL = 'my_user.MyUser'

AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

#SOCIAL_AUTH_FACEBOOK_KEY = '725531677540887'
SOCIAL_AUTH_FACEBOOK_KEY = '745274525566602'
#SOCIAL_AUTH_FACEBOOK_SECRET = '5a64571fb9155326f8b69ee92aa77b7b'
SOCIAL_AUTH_FACEBOOK_SECRET = 'bf2114bc3d9477a25abfa6fac6e54cda'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['public_profile', 'email']
SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    'comealong.pipeline.save_profile_picture',
)
