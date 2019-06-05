import logging

import requests
from django.http import JsonResponse
from django.views.generic import TemplateView


def index(request):
    try:
        response = requests.get("http://localhost:8000")
        status = response.status_code
        data = response.json()
    except Exception as e:
        logging.error(e)
        status = 404
        data = None

    return JsonResponse({
        "message": "Hello world!",
        "data": data,
        "status": status
    })


class ProfileView(TemplateView):
    template_name = "profile.html"
