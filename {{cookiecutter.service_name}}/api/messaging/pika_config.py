import pika

cred = pika.PlainCredentials("guest", "aaaaa")

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost", credentials=cred))

channel = conn.channel()