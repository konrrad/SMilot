import sys
from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QApplication
from ConfigProvider import ConfigProvider
from ConfigTranslator import ConfigTranslator
from ErrorHandler import ErrorHandler
from NetworkClient import NetworkClient


class Window(QWidget):

    def __init__(self, config_filepath):
        super().__init__()
        self.setWindowTitle("PILOT")
        self.setMinimumWidth(300)
        self.setMinimumHeight(300)
        self.main_window = QTabWidget()
        self.layout=QVBoxLayout()
        self.layout.addWidget(self.main_window)
        self.setLayout(self.layout)
        self.error_handler = ErrorHandler(self.main_window)
        try:
            self.config_provider = ConfigProvider(file_path=config_filepath)

            self.network_client = NetworkClient(client_name=self.config_provider.get_client_name(),
                                            port=self.config_provider.get_port(),
                                            host=self.config_provider.get_address(),
                                            password=self.config_provider.get_password(),
                                            observer=self)

            self.config_translator = ConfigTranslator(self.config_provider, self.network_client)
            self.create_window()
            self.coords_controller_map=self.config_translator.get_coords_controller_map()

            self.network_client.estabilish_connection()
            self.subscribe_to_topics()
        except Exception as e:
            self.error_handler.create_error(str(e))


    def subscribe_to_topics(self):
        for coord in self.coords_controller_map.keys():
            self.network_client.subscribe(coord)

    def create_window(self):

        self.room_controller_map=self.config_translator.get_room_controller_map()
        for room in self.room_controller_map.keys():
            controllers=self.room_controller_map[room]
            tab_layout=QVBoxLayout()
            outer_widget = QWidget()
            outer_widget.setLayout(tab_layout)
            for controller in controllers:
                tab_layout.addWidget(controller.get_widget())

            self.main_window.addTab(outer_widget,room)


    def message_pushed(self,topic,value):
        controller=self.coords_controller_map[topic]
        controller.update_value_and_view(int(value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=Window('config.json')
    window.show()
    app.exec_()
