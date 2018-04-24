from pika_config import channel as subscriber
from tasks import tasks

subscriber.exchange_declare(exchange='topic_exchange',
							exchange_type='topic')

subscriber.queue_declare(queue="queue_1")

# queue bind example
subscriber.queue_bind(exchange='topic_exchange',
					  queue="queue_1",
					  routing_key="receive.1.op.1")


#
# subscriber.queue_bind(exchange='topic_exchange',
#                    queue="queue_1",
#                routing_key="receive.1.op.2")


def callback(ch, method, properties, body):
	print(" [x] Received %r:%r" % (body, method.routing_key))


subscriber.basic_consume(callback,
						 queue='queue_1',
						 no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
subscriber.start_consuming()
