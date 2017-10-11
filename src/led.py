import RPi.GPIO as GPIO
LED_PIN = 25

class Led:
  def __init__(self):
    self.channel = LED_PIN
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.channel, GPIO.OUT)
    self.pwm = GPIO.PWM(self.channel, 100)
    self.pwm.start(0)

  def switch_on(self):
    self.pwm.ChangeDutyCycle(100)

  def switch_off(self):
    self.pwm.ChangeDutyCycle(0)

  def __del__(self):
    GPIO.cleanup()
