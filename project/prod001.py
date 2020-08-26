from pykafka import KafkaClient
from datetime import datetime
import json
import uuid # for generating random ids

input_name = 'coordinates.json'
host = 'localhost:9092'
topic_name = 'webTest'

# unique id = unique producer
producer_id = '001'

def generate_random_id():
    return uuid.uuid4()

def print_info():
    print('Producer ' + producer_id + ' is sending messages to kafka broker: ' + host + ' on topic: ' + topic_name )

def read_json_data():
    input = open(input_name)
    json_input = json.load(input)
    coordinates = json_input['features'][0]['geometry']['coordinates']
    return coordinates

def create_producer():
    client = KafkaClient(hosts=host)
    topic = client.topics[topic_name]
    producer = topic.get_sync_producer()
    return producer

def generate_messages(coordinates, producer):
    data = {}
    data['line'] = producer_id
    i = 0
    coords_amount = len(coordinates)

    while i < coords_amount:

        data['id'] = data['line'] + '-' + str(generate_random_id())
        data['timestamp'] = str(datetime.utcnow())
        data['x'] = coordinates[i][1]
        data['y'] = coordinates[i][0]

        message = json.dumps(data)
        producer.produce(message.encode('ascii'))

        if i == coords_amount - 1:
            i = 0
        else:
            i += 1

def main():

    print_info()
    coordinates = read_json_data()
    producer = create_producer()
    generate_messages(coordinates, producer)

if __name__ == '__main__':
    main()
