from flask import Flask, render_template, Response
from pykafka import KafkaClient

host = '127.0.0.1:9092'

def establish_kafka_client(hosts=host):
    return KafkaClient(hosts=host)

app = Flask(__name__)

@app.route('/test')
def index():
    return (render_template('index.html'))

@app.route('/topic/<topic_name>')
def generate_messages(topic_name):
    client = establish_kafka_client()
    def events():
        # connecting consumer to passed topic
        for i in client.topics[topic_name].get_simple_consumer():
            # consumer is listening to passed topic all the time ->> no return ->> generator
            # consumer gets response in event stream - returning response to browser continously
            yield f'data:{i.value.decode()}\n\n'
    return Response(events(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
