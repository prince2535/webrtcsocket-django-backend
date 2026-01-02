from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-secret-key"

# ✅ Keep True for now (OK for local + Render testing)
DEBUG = True

# 🔴 Required for Render (safe during development)
ALLOWED_HOSTS = ["*"]

# ===================== APPS =====================
INSTALLED_APPS = [
    "corsheaders",                 # ✅ MUST be first

    # Django core
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # WebSocket support
    "channels",

    # WebRTC chat app (DO NOT TOUCH)
    "chat",

    # MongoDB auth app (HTTP only)
    "accounts",
]

# ===================== MIDDLEWARE =====================
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # ✅ MUST be first
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
# In-memory layer (NO Redis, works on Render Free)
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    }
}

# ===================== CORS =====================
CORS_ALLOWED_ORIGINS = [
    "https://webrtcsocket-django-frontend.vercel.app",
]

CORS_ALLOW_HEADERS = [
    "content-type",
]

# ===================== STATIC =====================
STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
