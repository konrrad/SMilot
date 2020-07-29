from ControllerCreator import ControllerCreator
from DeviceBuilder import DeviceBuilder
from DeviceQWidget import DeviceQWidget


class ConfigTranslator:

    def __init__(self, config_provider, observer):
        self.observer = observer
        self.config_provider = config_provider
        self.controller_creator = ControllerCreator()
        self.room_devices_map = self._create_room_devices_map()
        self.room_controller_map = self._create_room_controller_map()

    def _create_room_devices_map(self):
        result = {}
        for room in self.config_provider.get_rooms_params():
            result[room["name"]] = self._get_devices_list(room)

        return result

    def _create_room_controller_map(self):
        result = {}

        for room in self.room_devices_map:
            result[room] = [self._create_controller(device) for device in self.room_devices_map[room]]

        return result

    def _get_devices_list(self, room):
        devices_from_file = room["devices"]
        result = []
        for device_parameters in devices_from_file:
            result.append(DeviceBuilder.create_device(device_parameters))
        return result

    def _create_controller(self, device):
        controller = self.controller_creator.create_controller(device)
        widget = DeviceQWidget(controller)
        controller.set_device_widget(widget)
        controller.set_observer(self.observer)
        return controller

    def get_room_controller_map(self):
        return self.room_controller_map

    def get_coords_controller_map(self):
        result = {}
        controllers = self._get_controllers_list()
        for controller in controllers:
            result[controller.get_coords()] = controller
        return result

    def _get_controllers_list(self):
        result = []
        for controllers in self.room_controller_map.values():
            for controller in controllers:
                result.append(controller)
        return result


    def save_state(self,rooms_controller_map):
        r=self.room_devices_map
        print(r)
        # for room in rooms:
        #     devices_in_config=room["devices"]
        #     devices_in_memory=self.room_devices_map[room]
        #     for device_in_memory in devices_in_memory:
        #         for device_in_config in devices_in_config:
        #             if device_in_memory.get_name()==device_in_config["name"]:
        #                 device_in_config["value"]=device_in_memory.get_value()
        for room_in_memory_name in r.keys():
            for room_in_config in self.config_provider.get_rooms_params():
                if room_in_memory_name==room_in_config["name"]:
                    devices_in_config=room_in_config["devices"]
                    devices_in_memory=r[room_in_memory_name]
                    for in_config in devices_in_config:
                        for in_memory in devices_in_memory:
                            if in_memory.get_name()==in_config["name"]:
                                in_config["value"]=in_memory.get_value()

        self.config_provider.save_rooms(self.config_provider.get_rooms_params())

