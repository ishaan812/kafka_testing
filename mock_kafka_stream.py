from kafka import KafkaProducer
from kafka.errors import KafkaError
import random

# Set up a Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

# Produce a message to the topic
topic = 'test'
key = '0'
for(day) in range(10, 31):
    for(user) in range(0, random.randint(1, 100)):
        rng= str(random.randint(100000, 999999))
        daytimestamp= (1676543492+(86400*day))
        value = r'website	web	2023-02-24 09:59:34.701	2023-02-24 09:59:34.429	2022-10-10 10:42:34.151	unstruct	82dbf502-5731-4423-8eae-7090b78338a8		biz1	js-3.5.0	ssc-2.8.2-kafka	snowplow-enrich-kafka-3.7.0		127.0.0.1		85094061-f702-4b62-a46d-20f7226b4741	29	c29840a5-25b0-430c-8eb3-bfcb4ecd1431												https://snowplow.io/			https	snowplow.io	443	/																							{"schema":"iglu:com.snowplowanalytics.snowplow/unstruct_event/jsonschema/1-0-0","data":{"schema":"iglu:com.nitiai/node_events_public/jsonschema/1-0-0","data":{"eventId":"4cdf6a87-d6e3-45bd-9fa6-22bbd'+rng+r'","timestamp":"'+str(daytimestamp)+r'","eventType":"VIEWED","source":"SDK","userId":"b8243e0e-a025-4c15-918b-bc4cee'+rng+r'","flowId":"3b478ac6-a687-47c7-99ca-45a008'+rng+r'","nodeId":"56dceccf-9ddd-4505-93b3-44548a'+rng+r'","nodeLevel":"'+str(random.randint(1,6))+r'","nodeOrder":"'+str(random.randint(1,3))+r'","nodeName":"Stash Create Success","podId":"491807c9-1f4b-4bb1-8a5a-ba1575'+rng+r'","cohortId":"8baa9da3-04df-4a21-b9f5-76ed4e'+rng+r'"}}}																			curl/7.79.1						en-GB										1	30	693	1302				Europe/London			3440	1440	UTF-8	678	9015												2022-10-10 10:42:34.153				be9520e7-16a5-4d4e-afa1-8e269f99a1cf	2023-02-24 09:59:34.427	com.nitiai	node_events_public	jsonschema	1-0-0		'
        future = producer.send(topic, key=key.encode('utf-8'), value=value.encode('utf-8'))
        print(value)

# value = r'2023-03-14 10:30:15\tlocalhost\tGET\t200\thttps://example.com\tMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36\t{\"schema\":\"sdk/onclick\",\"data\":{\"user_id\":\"12347\",\"flow_id\":\"311\",\"email\":\"johndoe@example.com\",\"cohort_id\": \"314\"}}'
# future = producer.send(topic, key=key.encode('utf-8'), value=value.encode('utf-8'))
# print(value)

# Wait for the message to be sent and check for errors
# try:
#     record_metadata = future.get(timeout=10)
#     print('Message sent to partition %d, offset %d' % (record_metadata.partition, record_metadata.offset))
# except KafkaError as e:
#     print('Failed to send message: %s' % e)
# finally:
#     # Clean up the Kafka producer
#     producer.close()



