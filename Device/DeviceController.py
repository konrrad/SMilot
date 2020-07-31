class DeviceController:
    def __init__(self, device):
        self.device = device

    def set_device_widget(self, device_frame):
        self.device_widget = device_frame

    def get_device_name(self):
        return self.device.get_name()

    def update_value_from_view(self, value):
        self.observer.notify(self.device.get_coordinates(),value)

    def update_value_and_view(self, value):
        self.device.update_value(value)
        self.device_widget.outer_value_changed(value)

    def has_range(self):
        return self.device.has_range()

    def get_value(self):
        return self.device.get_value()

    def set_observer(self,observer):
        self.observer=observer

    def get_widget(self):
        return self.device_widget

    def get_coords(self):
        return self.device.get_coordinates()


