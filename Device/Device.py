class Device:
    def __init__(self,id,name,range,value,coordinates):
        self.id=id
        self.name=name
        self.range=range
        self.value=value
        self.coordinates=coordinates

    def update_value(self,value):
        self.value=value

    def get_value(self):
        return self.value

    def get_coordinates(self):
        return self.coordinates

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def has_range(self):
        return self.range