import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-hc9$&mai=#*qy3*#*li$!-k8%02q7t3*wlru@elq96_*hpxy$i'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'redis_cluster.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'redis_cluster.wsgi.application'
from redis.cluster import ClusterNode

REDIS_NODES = [ 
    ClusterNode('172.20.0.31', 6373),
    ClusterNode('172.20.0.32', 6374),
    ClusterNode('172.20.0.33', 6375),
    ClusterNode('172.20.0.34', 6376),
    ClusterNode('172.20.0.35', 6377),
    ClusterNode('172.20.0.36', 6378)
]
REDIS_HOST = os.environ.get("REDIS_HOST", 'localhost')
REDIS_PORT = os.environ.get("REDIS_PORT", 6379)
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", '')
REDIS_DB = os.environ.get("REDIS_DB", 0)
REDIS_URI = f'redis://:{REDIS_PASSWORD}@172.20.0.31:6373,172.20.0.32:6374,172.20.0.33:6375,172.20.0.34:6376,172.20.0.35:6377,172.20.0.36:6378'


GLOBAL_CACHE_DB = os.environ.get("GLOBAL_CACHE_DB", 10)
GLOBAL_CACHE_CONF = {}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f'{REDIS_URI}/{REDIS_DB}',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "herlife_community_cache",
        "TIMEOUT": None
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# app = Celery('your_app_name')
# app.conf.broker_transport_options = {'visibility_timeout': 43200}
# app.conf.broker_connection_retry = True
# app.conf.broker_connection_max_retries = 3
# app.conf.broker_url = CELERY_BROKER_URL
# app.conf.redis_cluster = redis_cluster

# from django.conf import settings
# from redis.cluster import RedisCluster
# from redis import ConnectionPool

# CELERY_BROKER_URL = 'redis://:@172.20.0.31:6373/0,172.20.0.32:6374/0,172.20.0.33:6375/0,172.20.0.34:6376/0,172.20.0.35:6377/0,172.20.0.36:6378/0'

# redis_pool = ConnectionPool.from_url(
#     CELERY_BROKER_URL,
#     max_connections=20,
# )

# redis = RedisCluster(
#     startup_nodes=settings.REDIS_NODES,
#     moved_response=False,
#     decode_responses=True,
# read_from_replicas=True)

# redis.set("aest", "value")