
import http.server
import paho.mqtt.client as mqtt

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    #def send_head(self):
    def do_GET(self):
        path = self.path[1:]
        topic, msg = path.split("?")
        print(topic, " - ", msg)
        client.publish(topic, msg, qos=1)
        self.send_response(204)
        self.end_headers()

def on_connect(client, userdata, flags, rc):
    pass

def on_message(client, userdata, msg):
    print("connected")
    pass

if __name__ == "__main__":
    print("Snap-MQTT")
    import re
    import socketserver

    client = mqtt.Client()
    client.connect("localhost",1883,60)

    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_start()

    port = 1330 

    handler = RequestHandler

    httpd = socketserver.TCPServer(("", port), handler)

    httpd.serve_forever()

