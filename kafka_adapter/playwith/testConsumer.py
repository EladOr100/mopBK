from classes import kafkaAdp
from classes import kafkaProd

if __name__ == "__main__":
    # ad = kafkaAdp.KafkaAdapter()
    # ad.latest_message()
    pro = kafkaProd.KafkaProduce()
    con = kafkaAdp.KafkaAdapter()
    pro.send_message('hello1')
    con.latest_message()
    # print (con.contain_message('hello'))
    # con.from_top()

    # print (con.print_consumer().metrics())
