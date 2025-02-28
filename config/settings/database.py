from config.settings.django import env

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("NAME", cast=str),
        "USER": env("USER", cast=str),
        "PASSWORD": env("PASSWORD", cast=str),
        "HOST": env("HOST", cast=str),
        "PORT": env("PORT", cast=str),
    }
}