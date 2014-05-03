"""
Django settings for uss project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_DIR = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
STATIC_DIR = os.path.join(PROJECT_DIR, "static")
TEMPLATE_DIR = os.path.join(PROJECT_DIR, "templates")
OUT_DIR = os.path.join(PROJECT_DIR, "out")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = []

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_DIR, 'paradise4paws', 'collected')

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    STATIC_DIR,
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'pipeline.finders.PipelineFinder'
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*d+b(l1sv7c4q78(n2w_-etku)d8fylx0i#qlw%9a*2c!f8iw!'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'uss.urls'

WSGI_APPLICATION = 'uss.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates"
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATE_DIR,
)

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',    
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'uss',
    'pipeline',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Pipeline settings
PIPELINE = True
PIPELINE_AUTO = False
PIPELINE_COMPILERS = (
    'pipeline.compilers.less.LessCompiler',
)
PIPELINE_CSS_COMPRESSOR = ''
PIPELINE_JS_COMPRESSOR = ''
PIPELINE_DISABLE_WRAPPER = True
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'
PIPELINE_VERSION = True

PIPELINE_CSS = {
    'uss_css': {
        'source_filenames': (
            r'css/app.css',
        ),
        'output_filename': 'css/uss-style.css',
    },
    'uss_plugin_css': {
        'source_filenames': (
            r'libs/bootstrap/dist/css/bootstrap.min.css',
        ),
        'output_filename': 'css/uss-plugin.css',
    },
}

PIPELINE_JS = {
    'uss_code_js': {
        'source_filenames': (
            r'js/app.js',
            r'js/controllers/url-list.js',
            r'js/controllers/url-detail.js',
            r'js/controllers/pagination.js',            
            r'js/services/services.js',
            r'js/directives/directives.js',
            r'js/filters/filters.js',
        ),
        'output_filename': 'js/usscode.js',
    },
    'uss_lib_js': {
        'source_filenames': (
            r'libs/jquery/jquery.min.js',
            r'libs/angular/angular.min.js',
            r'libs/angular-route/angular-route.min.js',
            r'libs/angular-resource/angular-resource.js',
            r'libs/bootstrap/dist/js/bootstrap.min.js',
            r'libs/angular-bootstrap/ui-bootstrap.min.js',
            r'libs/angular-bootstrap/ui-bootstrap-tpls.min.js',            
        ),
        'output_filename': 'js/uss-lib.js',
    },
}
