from rest_framework.decorators import api_view
from rest_framework.response import Response
from .messaging.pika_config import channel as publisher
from .messaging.tasks import tasks

publisher.exchange_declare(exchange='topic_exchange',
                         exchange_type='topic')

@api_view(http_method_names=["GET"])
def api_hello(request):
	tasks.a.delay(4,5)
	return Response({"message": "Hello API"})
