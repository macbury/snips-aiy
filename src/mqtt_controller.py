import paho.mqtt.client as mqtt

class MqttController:
  def __init__(self, config):
    self.config = config
    self.client = mqtt.Client()

    self.client.on_connect = self.on_connect
    self.client.on_message = self.on_message

    mqc = self.config['mqtt']

    if mqc.has_key('username'):
      self.client.username_pw_set(mqc['username'], mqc['password'])
    self.client.connect(mqc['host'], mqc['port'], 60)
    self.client.loop_start()

  def on_connect(self, client, userdata, flags, rc):
    print 'connect'
  def on_message(self, client, userdata, msg):
    print 'message'
