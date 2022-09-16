# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+y0rnb2)!t4*@u2g*$8gz@9wg58mn_usk%*s-51=x__ku8k_7$'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_library_backend_project',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}
