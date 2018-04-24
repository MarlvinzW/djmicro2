from pika_config import channel as publisher

publisher.exchange_declare(exchange='topic_exchange',
                         exchange_type='topic')

publisher.basic_publish(exchange="topic_exchange",
                 routing_key="receive.1.op.1",
                 body="Queue 1 Op 1")

