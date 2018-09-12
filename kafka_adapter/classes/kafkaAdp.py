from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
import config


class KafkaAdapter:
    def __init__(self):
        try:
            self._consumer_all = KafkaConsumer(auto_offset_reset='earliest')
            self._consumer_last = KafkaConsumer(auto_offset_reset="latest")
            topics = config.CONFIG['topics']
            self._consumer_all.subscribe(topics)
            self._consumer_last.subscribe(topics)
            self._internal = []
        except NoBrokersAvailable:
            print ('hey, make sure the kafka brokers are up')

    def latest_message(self):
        try:
            for msg in self._consumer_last:
                if msg.value == '':
                    print ('empty line')
                else:
                    print (msg.value)
        except KeyboardInterrupt:
            print('you stopped me')

    def from_top(self):
        try:
            for msg in self._consumer_all:
                if msg.value == '':
                    print ('empty line')
                else:
                    print (msg.value)
            pass
        except KeyboardInterrupt:
            print('you stopped me')

    def p(self):
        self._consumer_all.max_poll_records()
    # def contain_message(self, text):
    #     return text in self._internal


if __name__ == "__main__":
    adp = KafkaAdapter()
    print (adp.p)

#     ad = KafkaAdapter()
#     ad.latest_message()
