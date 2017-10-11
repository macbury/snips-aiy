#!/usr/bin/env python
from src import HomeAssistant, SnipsController

from ruamel.yaml import YAML
import time

config = YAML(typ='safe').load(open('config/settings.yaml'))

print 'Booting...'

home_assistant = HomeAssistant(config['home_assistant'], config['device_id'])
snips = SnipsController(config['snips'], home_assistant)
home_assistant.snips = snips
while True:
  time.sleep(5)
