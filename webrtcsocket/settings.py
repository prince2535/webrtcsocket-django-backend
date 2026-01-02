from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "dev-secret-key"

# ✅ Keep True for now (Render allows it)
DEBUG = True

# 🔴 REQUIRED FOR RENDER (safe for now)
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
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

    # ✅ NEW: MongoDB auth app (HTTP only)
    "accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ROOT_URLCONF = "webrtcsocket.urls"

# 🔥 CRITICAL: ASGI entry (WebSockets)
ASGI_APPLICATION = "webrtcsocket.asgi.application"

# ✅ In-memory channel layer (NO Redis, safe on Render Free)
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    }
}

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
