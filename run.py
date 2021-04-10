import json

import paho.mqtt.client as mqtt
import structlog

from app import config
from app.accessory.screen import Screen

logger = structlog.getLogger(__name__)

# The callback for when the client receives a CONNACK response from the server.
logger.info("Starting screen-handler")
screen = Screen(name="raspi-touchscreen")

if not config.TOPIC_NAME:
    raise ValueError("The environment variable 'TOPIC_NAME' needs to be set.")


def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    topic = f"commands/{config.TOPIC_NAME}/#"
    logger.info("Subscribing", topic=topic)
    client.subscribe(topic)
    logger.info("Connected", rc=str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    payload = str(message.payload.decode("utf-8")).strip()
    logger.info("Handling message", topic=message.topic, payload=payload)

    screen.handle(payload=json.loads(payload))

    publish_topic = f"events/{config.TOPIC_NAME}"
    logger.info("Publishing state update message", topic=publish_topic, payload=payload)
    client.publish(topic=publish_topic, payload=payload, retain=True)


logger.info("Connecting to MQTT")
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(config.BROKER, 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
