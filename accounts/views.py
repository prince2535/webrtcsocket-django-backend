from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import bcrypt
from .mongo import users


@csrf_exempt
def signup(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=400)

    data = json.loads(request.body)
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return JsonResponse({"error": "Missing fields"}, status=400)

    if users.find_one({"email": email}):
        return JsonResponse({"error": "User already exists"}, status=400)

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    users.insert_one({
        "email": email,
        "password": hashed_password
    })

    return JsonResponse({"message": "Signup successful"})


@csrf_exempt
def login(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=400)

    data = json.loads(request.body)
    email = data.get("email")
    password = data.get("password")

    user = users.find_one({"email": email})
    if not user:
        return JsonResponse({"error": "Invalid credentials"}, status=401)

    if not bcrypt.checkpw(password.encode(), user["password"]):
        return JsonResponse({"error": "Invalid credentials"}, status=401)

    return JsonResponse({"message": "Login successful"})
