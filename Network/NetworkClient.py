import paho.mqtt.client as mqtt

class NetworkClient:
    def __init__(self, client_name, port, host, password,observer):
        self.CLIENT_NAME = client_name
        self.PORT = port
        self.HOST = host
        self.PASSWORD = password
        self.observer=observer
        self._init_client()

    def _init_client(self):
        self.client = mqtt.Client(self.CLIENT_NAME, False)
        self.client.on_connect = self.on_connect
        self.client.on_message=self.on_message
        self.client.username_pw_set(self.CLIENT_NAME, self.PASSWORD)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connection successful")
        else:
            raise RuntimeError("Connection failed.")

    def estabilish_connection(self):
        self.client.connect(self.HOST)
        self.client.loop_start()

    def subscribe(self, topic):
        self.client.subscribe(topic,qos=2)

    def on_message(self,client,userdata,message):
        self.observer.message_pushed(message.topic,str(message.payload.decode("utf-8")))

    def notify(self, coords, value):
        self.client.publish(coords,value,qos=2)

    def shut_connection(self):
        self.client.loop_stop()
