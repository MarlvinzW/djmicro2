from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(http_method_names=["GET"])
def api_hello(request):
	return Response({"message": "Hello API"})
