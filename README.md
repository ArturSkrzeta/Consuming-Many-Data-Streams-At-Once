<h2>Apache Kafka for Event Driven Architecture</h2>
<p>Step by step Apache Kafka implementation and application creation.</p>
<h3>Kafka for Microservices</h3>
<ul>
  <li>Breaking a monolithic system of subsequent programs down into independent microservices.</li>
  <li>Kafka as messaging central bus bonds all independent microservices.</li>
  <li>Kafka decreases costs of microservices integration.</li>
  <br>
  <img src="images/microservices.JPG"?
</ul>
<h3>Kafka</h3>
<ul>
  <li>Data streaming technology.</li>
  <li>For event driven architecture.</li>
  <li>Kafka is distributed horizontally.</li>
  <li>Kafka is redundant backuping itself up.</li>
  <li>There is need for zookeper to run first.</li>
</ul>
  

More:
+ messaging and streaming applications
+ takes data from different sources and makes it available for different applications
+ helps to eliminate daily batch jobs
+ important role for CDC - chagne data capture and in the world of microservices
+ data streaming: continuously generated, small size events, low latency required
+ even when the destination system (consumer)  is not available it can pick up and process the message later
+ instead of one system talking directl to another system, now a system is talking to a middle layer - kafka - procduer sends messages or events to kafka
+ then kafka as middle layer needs to ensure high availability
+ new consumers can be added without any changes in system
+ kafka can be treated as a data stores - messages are kept forever
+ log is an another word for a stream
+ when producer sends an event it's appended at the end of message queue -- it doesn't matter how much data is already stored in the topic, it's not getting more costly for a producer to san a message
+ different consumers can read from different positions of the log
+ consumer reads the message but the message is still in the log (as opposed to sqs for example)  - different consumers can reread the same message
+ default expiry of a message is 7 days but it can be set to unlimited
+ topics are partitioned accros different brokers that make a cluster
+ state and config is being kept in the zookeeper
+ we use partitions to spread the data across the brokers for more throughut and more concurrency
+ replication replicates a partition from one broker to another - more availability and backup in case of borker's failure
+ on AWS : Amazon Managed Streaming for Kafka - MSK - zookeeper runs under the hood 
+ we can encrypt data in transit or data at rest in AWS

<h3>Installation</h3>
<ol>
  <li>Install Java.</li>
  <li>Add Java to environment variables
      <ul>
        <li>My java directory: C:\Program Files\Java\jdk-14.0.2.</li>
        <li>C:\Program Files\Java\jdk-14.0.2\bin as PATH to User variables.</li>
        <li>C:\Program Files\Java\jdk-14.0.2 as JAVA_HOME to System variables.</li>
      </ul>
  </li>
  <li>We can check if java installation successful:</li>
  <br>
  <img src="images/java.JPG">
  <li>Install Kafka from https://kafka.apache.org/downloads</li>
  <li>Add Kafka to environment variables
       <ul>
        <li>My kafka directory: C:\kafka\bin\windows.</li>
        <li>C:\kafka\bin\windows as PATH to User variables.</li>
      </ul>
  </li>
  <li>Start Kafka in console:</li>
  <br>
  <img src="images/kafka.JPG">
</ol>
<h3>Configuration</h3>
<ol>
  <li>Crete additional folders in Kafka directory:</li>
  <br>
  <img src="images/data_dir.JPG">
  <li>Edit files: zookeeper.properties and server.properties in kafka/config directory</li>
  <br>
  <img src="images/properties.JPG">
  <li>Edit file: server.properties in kafka/config directory</li>
  <br>
  <img src="images/listeners.JPG">
</ol>
<h3>Running zookeper and kafka</h3>
<ol>
  <li>zookeeper first - runs on localhost:2181 <br><b>C:\kafka\bin\windows>zookeeper-server-start.bat ../../config/zookeeper.properties <br> [2020-08-25 14:17:57,974] INFO binding to port 0.0.0.0/0.0.0.0:2181 (org.apache.zookeeper.server.NIOServerCnxnFactory)</b></li>
  <br>
  <img src="images/zookeeper_start.JPG">
  <li>kafka second - runs on localhost:9092 <br><b>C:\kafka\bin\windows>kafka-server-start.bat ../../config/server.properties <br> once conntecte: [2020-08-25 14:19:03,357] INFO [KafkaServer id=0] started (kafka.server.KafkaServer)</b></li>
  <br>
  <img src="images/kafka_start.JPG">
</ol>
<h3>Topics on kafka broker</h3>
<ul>
  <li>Creating new one: <br> <b>C:\kafka\bin\windows>kafka-topics.bat --zookeeper localhost:2181 --topic test2 --create --partitions 1 --replication-factor 1 </b> </li>
  <br>
  <img src="images/topic.JPG">
  <li>Listing all topics: <br> <b>C:\kafka\bin\windows>kafka-topics.bat --zookeeper localhost:2181 --topic test_topic --describe </b> </li>
  <br>
  <img src="images/topic_list.JPG">
</ul>
<h3>Kafka Producer</h3>
<ul>
  <li>Producing messages to kafka broker: <br> <b>C:\kafka\bin\windows>kafka-console-producer.bat --broker-list localhost:9092 --topic test2 </b> </li>
  <br>
  <img src="images/messages.JPG">
</ul>
<h3>Kafka Consumer</h3>
<ul>
  <li>Establishing consumer to topic: <br> <b>C:\kafka\bin\windows>kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test2 --from-beginning </b> </li>
  <br>
  <img src="images/consumer-connected.JPG">
</ul>
<h3>Producer -> Message -> Consumer</h3>
<ul>
  <img src="images/prod_cons.gif">
</ul>
<h3>Python Producer</h3>
<ul>
  <li>Pykafka installation: pip install pykafka</li>
  <li>Importing: from pykafka import KafkaClient.</li>
  <li>Creating instance of KafkaCleint
    <ul>
      <li>client = KafkaClient(hosts="localhost:9092")</li>
    </ul>
  </li>
  <br>
  <img src="images/pykafka.gif">
</ul>
<h3>Multiple Python Producers</h3>
<ul>
  <img src="images/multiple_producers.gif">
</ul>  
<h3>Python Flask Consumer</h3>
<ul>
  <img src="images/flask_consumer.gif">
</ul>  
<h3>Flask-Consumer and Python-Producer</h3>
<ul>
  <img src="images/flask-consumer-python-producer.JPG">
</ul>


