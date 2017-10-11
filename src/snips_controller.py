from mqtt_controller import MqttController
from led import Led
import time

class SnipsController(MqttController):
  def __init__(self, config, home_assistant):
    MqttController.__init__(self, config)
    self.led = Led()
    self.home_assistant = home_assistant

  def push_tts(self, topic, payload):
    print('[Forwarding {}]: {}'.format(topic, payload))
    self.client.publish(topic=topic, payload=payload, qos=1)

  def on_connect(self, client, userdata, flags, rc):
    print("Connected to snips")
    for topic in ['hermes/asr/toggleOn', 'hermes/hotword/toggleOn', 'hermes/nlu/intentParsed']:
      self.client.subscribe(topic)

  def on_message(self, client, userdata, msg):
    if msg.topic == 'hermes/asr/toggleOn':
      self.led.switch_on()
      print('Switch on led')
    elif msg.topic == 'hermes/hotword/toggleOn':
      self.led.switch_off()
      print('Switch off led')
    elif msg.topic == 'hermes/nlu/intentParsed':
      self.home_assistant.push_intent(msg)
