# Snap MQTT bridge

Package to send MQTT messages from Snap (https://snap.berkeley.edu/).

Objective: enable the Snap programming system to send  messages to a MQTT broker.

What you need:
* Internet connection (to use Snap).
* Python 3.x
* paho-mqtt library in Python (`pip3 install paho-mqtt`)
* A MQTT broker (mosquitto or a online server)

How to use?
1. Configure Snap-MQTT.py with your broker addresses (in the line: `client.connect("localhost",1883,60)`).
2. Run `python3 Snap-MQTT.py`.
3. Start Snap.
4. Import `Snap-MQTT.xlm`.
5. Send MQTT message using the imported block (in 'Variables' menu).

Todo (help!):

Receive MQTT messages:
* Block to suscribe to a topic (run only once).
* Receive messages and keep them in the python server.
* Block to read actual values (last received).
