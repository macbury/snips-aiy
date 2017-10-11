# snips-aiy
Use google https://aiyprojects.withgoogle.com/ hat with snips.ai and http://home-assistant.io
This script will light up led on voice input and forward intents from snips mosquitto broker to home assistant mqtt broker. Additionaly it allows you to have multiple snips devices in house and forward tts to them

# Make google voice hat work with snips
We need to clone snips aiy project repository and install all drivers:

```
cd /tmp
git clone https://github.com/google/aiyprojects-raspbian.git
cd aiyprojects-raspbian/

sudo configure-driver.sh
sudo install-alsa-config.sh
```

Now just reboot pi `sudo reboot`. After reboot we should only see one sound card device in our system:

```
run aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: sndrpigooglevoi [snd_rpi_googlevoicehat_soundcar], device 0: Google voiceHAT SoundCard HiFi voicehat-hifi-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0

```

and only one microphone device:

```
run arecord -l

**** List of CAPTURE Hardware Devices ****
card 0: sndrpigooglevoi [snd_rpi_googlevoicehat_soundcar], device 0: Google voiceHAT SoundCard HiFi voicehat-hifi-0 []
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

Finally just record few sentences for test using voice hat microphone:
```
arecord -f cd out.wav
```

And play them from speaker:

```
aplay out.wav
```

# Installation snips-aiy bridge

Clone this repository to `/home/pi` directory then run this commands:

```
cd /home/pi/snips-aiy
pip install -r requirements.txt
cp .asoundrc ~/.asoundrc
cp config/settings.yaml.example config/settings.yaml
```

Edit configuration under `/home/pi/config/settings.yaml` and after that run:

```
sudo cp systemd/snips-aiy.service /lib/systemd/system/
sudo systemctl enable snips-aiy
sudo systemctl start snips-aiy
```
