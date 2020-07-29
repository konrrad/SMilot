from DeviceController import DeviceController


class ControllerCreator:
    def create_controller(self, device):
        controller = DeviceController(device)
        return controller
