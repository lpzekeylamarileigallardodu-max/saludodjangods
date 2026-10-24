import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from saludos.application.saludar_usecase import SaludarUseCase

usecase = SaludarUseCase()


@csrf_exempt
def saludar(request):
    if request.method == "POST":
        nombre = json.loads(request.body or "{}").get("nombre")
    else:
        nombre = request.GET.get("nombre")
    if not nombre:
        return JsonResponse({"error": "nombre requerido"}, status=400)
    return JsonResponse({"mensaje": usecase.execute(nombre)})