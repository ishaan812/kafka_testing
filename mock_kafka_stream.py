# from kafka import KafkaProducer
# from kafka.errors import KafkaError
# import random

# # Set up a Kafka producer
# producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# # Produce a message to the topic
# topic = 'test123'
# key = '0'
# for(day) in range(10, 31):
#     for(user) in range(0, random.randint(1, 100)):
#         value = r'2023-03-'+str(day)+r' 10:30:15\tlocalhost\tGET\t200\thttps://example.com\tMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36\t{\"schema\":\"sdk/onclick\",\"data\":{\"user_id\":\"1234'+str(user)+r'\",\"flow_id\":\"'+str(random.randint(0,300))+r'\",\"email\":\"johndoe@example.com\",\"cohort_id\": \"314\"}}'
#         future = producer.send(topic, key=key.encode('utf-8'), value=value.encode('utf-8'))
#         print(value)

# value = r'2023-03-14 10:30:15\tlocalhost\tGET\t200\thttps://example.com\tMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36\t{\"schema\":\"sdk/onclick\",\"data\":{\"user_id\":\"12347\",\"flow_id\":\"311\",\"email\":\"johndoe@example.com\",\"cohort_id\": \"314\"}}'
# future = producer.send(topic, key=key.encode('utf-8'), value=value.encode('utf-8'))
# print(value)

# # Wait for the message to be sent and check for errors
# try:
#     record_metadata = future.get(timeout=10)
#     print('Message sent to partition %d, offset %d' % (record_metadata.partition, record_metadata.offset))
# except KafkaError as e:
#     print('Failed to send message: %s' % e)
# finally:
#     # Clean up the Kafka producer
#     producer.close()

import csv

with open('output.tsv', 'r') as tsvfile:
    tsvfile = tsvfile.read().replace(' ', '\t')
    reader = csv.DictReader(tsvfile, delimiter='\t')
    data = [row for row in reader]
    
print(data)

