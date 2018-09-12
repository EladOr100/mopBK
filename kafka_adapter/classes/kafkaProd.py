from kafka import KafkaProducer
import config

class KafkaProduce:

    def __init__(self):
        self._producer = KafkaProducer(bootstrap_servers=config.CONFIG['kafka_broker']+":" + config.CONFIG['port'])

    def send_message(self, text_to_send):
        try:
            self._producer.send('test', text_to_send)
            self._producer.flush(60)
        except KafkaProducer.KafkaTimeoutError , e:
            print ("cant send the message", e)
