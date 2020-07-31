from Device import Device


class DeviceBuilder:
    @staticmethod
    def create_device(parameters_map):
        return Device(id=parameters_map["id"],
                      name=parameters_map["name"],
                      range=parameters_map["range"],
                      value=parameters_map["value"],
                      coordinates=parameters_map["coordinates"])
