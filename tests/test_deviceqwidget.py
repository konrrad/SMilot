import unittest
import sys
from unittest import mock

from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout

from ControllerCreator import ControllerCreator
from DeviceBuilder import DeviceBuilder
from DeviceQWidget import DeviceQWidget


class DeviceQWidgetTest(unittest.TestCase):
    def test_one_widget_creation(self):
        app = QApplication(sys.argv)
        device = DeviceBuilder().create_device({'id': 1,
                                                'name': 'name',
                                                'range': False,
                                                'value': 10,
                                                'coordinates': '/coords/'})
        controller = ControllerCreator().create_controller(device)
        device_widget = DeviceQWidget(controller)
        controller.set_device_widget(device_widget)

        device_widget.show()
        app.exec_()

    def test_multiple_widget_creation(self):
        app = QApplication(sys.argv)
        device1 = DeviceBuilder().create_device({'id': 1,
                                                 'name': 'name',
                                                 'range': False,
                                                 'value': 1,
                                                 'coordinates': '/coords/'})
        device2 = DeviceBuilder().create_device({'id': 1,
                                                 'name': 'name',
                                                 'range': True,
                                                 'value': 10,
                                                 'coordinates': '/coords/'})
        controller1 = ControllerCreator().create_controller(device1)
        controller2 = ControllerCreator().create_controller(device2)
        device_widget1 = DeviceQWidget(controller1)
        device_widget2 = DeviceQWidget(controller2)
        controller1.set_device_widget(device_widget1)
        controller2.set_device_widget(device_widget2)

        outer = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(device_widget1)
        layout.addWidget(device_widget2)
        outer.setLayout(layout)
        outer.show()
        app.exec_()


if __name__ == '__main__':
    unittest.main()
