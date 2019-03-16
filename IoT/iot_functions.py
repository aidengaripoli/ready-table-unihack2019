
from sense_hat import SenseHat
import datetime
import time
import jwt
import paho.mqtt.client as mqtt
import re
import _thread


# Device variables

ssl_private_key_filepath = '../certs/rsa_private.pem'
ssl_algorithm = 'RS256' # Either RS256 or ES256
root_cert_filepath = '../certs/roots.pem'
project_id = 'readytable'
gcp_location = 'asia-east1'
registry_id = 'uh-registry'
device_id = 'table-device'

# end of user-variable

cur_time = datetime.datetime.utcnow()

def create_jwt():
  token = {
      'iat': cur_time,
      'exp': cur_time + datetime.timedelta(minutes=60),
      'aud': project_id
  }

  with open(ssl_private_key_filepath, 'r') as f:
    private_key = f.read()

  return jwt.encode(token, private_key, ssl_algorithm)

_CLIENT_ID = 'projects/{}/locations/{}/registries/{}/devices/{}'.format(project_id, gcp_location, registry_id, device_id)
_MQTT_TELEMETRY_TOPIC = '/devices/{}/events'.format(device_id)
_MQTT_CONFIG_TOPIC = '/devices/{}/config'.format(device_id)
_MQTT_COMMANDS_TOPIC = '/devices/{}/commands/#'.format(device_id)

client = mqtt.Client(client_id=_CLIENT_ID)
# authorization is handled purely with JWT, no user/pass, so username can be whatever
client.username_pw_set(
    username='unused',
    password=create_jwt())

regExp = re.compile('1')
sense = SenseHat()

def error_str(rc):
    return '{}: {}'.format(rc, mqtt.error_string(rc))

def on_connect(unusued_client, unused_userdata, unused_flags, rc):
    print('on_connect', error_str(rc))

def on_publish(unused_client, unused_userdata, unused_mid):
    print('on_publish')

# occasionally, some noise come through that needs to be stripped out
# This code ensures that it's stripped out properly
def message_text(orig):
    print ('matching message text: {}'.format(orig))
    ma = re.match(r'^b\'(.*)\'$', orig)
    if ma == None:
        return orig
    else:
        return ma.group(1)

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

rC = [255,0,0]
oC = [255,69,0]
yC = [255,255,0]
gC = [0,255,0]
bC = [0,0,255]
pC = [128,0,128]
wC = [255,255,255]
blC = [0,0,0]

#check for button input on py
def stick_input():
    while True:
        for event in sense.stick.get_events():

          table_number = 1
          restaurant_id = "03CBqzGzGeSqmCyPgaoP"

          if event.action == "pressed":
              payload = '{{ "ts": {}, "table_number": {}, "restaurant_id": "{}" }}'.format(int(time.time()), table_number , restaurant_id)

              # Uncomment following line when ready to publish
              client.publish(_MQTT_TELEMETRY_TOPIC, payload, qos=1)

              print("{}\n".format(payload))
              sense.clear(0, 255, 0)
          
#call button input in another thread
try:
    _thread.start_new_thread(stick_input, ())
except:
    print("Error: Unable to start new thread")

# Method which handles parsing the text message coming back from the Cloud
# This is where you could add your own messages to play with different
# actions based on messages coming back from the Cloud
def respondToMsg(msg):
    sense.low_light = True
    if msg == "reserved":  #red
        sense.clear(255,0,0)
    elif msg == "free":  #green
        sense.clear(0,255,0)
    elif msg == "preparing_food":  #blue
        sense.clear(0,0,255)
    elif msg == "food_ready":
        sense.clear(220, 66, 244)  #pink
    elif msg == "all_food_delivered":
        sense.clear(255, 124, 25)  #orange
    elif msg == "rainbow":
        rainbow = [
        rC, rC, oC, yC, gC, bC, pC, pC,
        rC, rC, oC, yC, gC, bC, pC, pC,
        rC, rC, oC, yC, gC, bC, pC, pC,
        rC, rC, oC, yC, gC, bC, pC, pC,
        rC, rC, oC, yC, gC, bC, pC, pC,
        rC, rC, oC, yC, gC, bC, pC, pC,
        rC, rC, oC, yC, gC, bC, pC, pC,
        rC, rC, oC, yC, gC, bC, pC, pC
        ]
        sense.set_pixels(rainbow)
    elif msg == "temp":
        sense.show_message(truncate((sense.get_temperature() * (9/5)) + 32, 1))
    else:
        sense.clear()

def on_message(unused_client, unused_userdata, message):
    payload = str(message.payload)
    print('Received message \'{}\' on topic \'{}\''.format(payload, message.topic))
    respondToMsg(message_text(payload))

client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message

client.tls_set(ca_certs=root_cert_filepath) # Replace this with 3rd party cert if that was used when creating registry
client.connect('mqtt.googleapis.com', 8883)
client.subscribe(_MQTT_CONFIG_TOPIC, qos=1)
client.subscribe(_MQTT_COMMANDS_TOPIC, qos=1)
client.loop_start()



# This is sleeping for an arbitrarily long time because it has to be connected
# in order to receive the command/config messages. Well, the config messages would
# come through next time the device connected, but that's not as interesting
# from a starting point
time.sleep(999)
client.loop_stop()
