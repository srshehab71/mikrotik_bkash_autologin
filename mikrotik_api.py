import routeros_api
import os

class MikroTikAPI:
    def __init__(self):
        self.host = os.getenv("MT_HOST")
        self.username = os.getenv("MT_USER")
        self.password = os.getenv("MT_PASS")
        self.port = int(os.getenv("MT_PORT", 8728))

    def create_hotspot_user(self, username, password, profile):
        try:
            connection = routeros_api.RouterOsApiPool(self.host, username=self.username, password=self.password, port=self.port)
            api = connection.get_api()
            user_resource = api.get_resource('/ip/hotspot/user')
            user_resource.add(name=username, password=password, profile=profile)
            connection.disconnect()
            return True
        except Exception as e:
            print("Error:", e)
            return False
