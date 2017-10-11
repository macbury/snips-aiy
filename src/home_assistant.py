from mqtt_controller import MqttController

class HomeAssistant(MqttController):
  def __init__(self, config, device_id):
    MqttController.__init__(self, config)
    self.device_id = device_id
    self.tts_topic = device_id+'/hermes/tts/say'
    self.snips = None

  def on_connect(self, client, userdata, flags, rc):
    print("Connected to home assistant broker")
    self.client.subscribe(tts_topic) # just grab when home assistant want to make tts

  def push_intent(self, msg):
    print('[Forwarding {}]: {}'.format(msg.topic, msg.payload))
    self.client.publish(topic=msg.topic, payload=msg.payload, qos=1)

  def on_message(self, client, userdata, msg):
    if msg.topic == tts_topic:
      snips.push_tts(msg.topic.lstrip(device_id+'/'), msg.payload)
