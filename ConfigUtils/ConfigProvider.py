import json


class ConfigProvider:
    def __init__(self, file_path):
        self.file_path = file_path
        self._load_data()

    def _load_data(self):
        with open(self.file_path) as f:
            self.data = json.load(f)

    def get_port(self):
        return self.data["port"]

    def get_password(self):
        return self.data["password"]

    def get_address(self):
        return self.data["address"]

    def get_client_name(self):
        return self.data["client_name"]

    def get_rooms_params(self):
        return self.data["rooms"]

    def save_rooms(self,rooms):
        self.data["rooms"]=rooms
        with open(self.file_path,'w') as config:
            json.dump(self.data,config)
