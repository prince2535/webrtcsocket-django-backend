from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-secret-key"

DEBUG = True

ALLOWED_HOSTS = ["*"]

# ===================== APPS =====================
INSTALLED_APPS = [
    "corsheaders",

    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "channels",
    "chat",
    "accounts",
]

# ===================== MIDDLEWARE =====================
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

# ===================== URL / ASGI =====================
ROOT_URLCONF = "webrtcsocket.urls"
ASGI_APPLICATION = "webrtcsocket.asgi.application"

# ===================== CHANNELS =====================
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    }
}

# ===================== CORS =====================
CORS_ALLOWED_ORIGINS = [
    "https://webrtcsocket-django-frontend.vercel.app",
]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

CORS_ALLOW_HEADERS = [
    "content-type",
]

# ===================== STATIC =====================
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
