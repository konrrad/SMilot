from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt

from GUI.IdentifiedSlider import IdentifiedSlider


class DeviceQWidget(QWidget):
    btn_stylesheet="font: bold 20px; background: blue; color: white"
    def __init__(self, controller):
        super().__init__()
        self.outer_layout = QVBoxLayout()
        self.upper_layout = QHBoxLayout()
        self.lower_layout = QHBoxLayout()
        self.controller = controller

        self.slider = IdentifiedSlider(self, controller.has_range(), controller.get_value())

        self._set_plus_btn()

        self._set_minus_btn()

        self._set_name_label()

        self._set_name_label()

        self.value_label = QLabel(str(controller.get_value()))

        self.upper_layout.addWidget(self.name_label)

        for widget in [self.minus_btn, self.slider, self.plus_btn, self.value_label]:
            self.lower_layout.addWidget(widget)

        self.outer_layout.addLayout(self.upper_layout)
        self.outer_layout.addLayout(self.lower_layout)
        self.setLayout(self.outer_layout)

    def _set_plus_btn(self):
        self.plus_btn = self._create_button("+")
        self.plus_btn.clicked.connect(self._plus_pushed)

    def _set_minus_btn(self):
        self.minus_btn = self._create_button("-")
        self.minus_btn.clicked.connect(self._minus_pushed)

    def _set_name_label(self):
        self.name_label = QLabel(text=self.controller.get_device_name())
        self.name_label.setFont(QFont("arial", 15))
        self.name_label.setAlignment(Qt.AlignCenter)

    def _create_button(self, text):
        btn=QPushButton(text=text)
        btn.setStyleSheet(self.btn_stylesheet)
        return btn

    def _minus_pushed(self):
        current = self.slider.value()
        next = current - 1
        self._change_slider_value(next)

    def _plus_pushed(self):
        current = self.slider.value()
        next = current + 1
        self._change_slider_value(next)

    def _change_slider_value(self, value):
        if self._is_in_range(value):
            self.slider.change_value(value)
            self.notify(value)
            self.value_label.setText(str(value))

    def notify(self, value):
        self.controller.update_value_from_view(value)

    def outer_value_changed(self, value):
        if self._is_in_range(value):
            self.slider.change_value(value)
            self._change_label_value(value)

    def _is_in_range(self, value):
        if self.controller.has_range():
            if -1 < value < 101:
                return True
        if value == 1 or value == 0:
            return True
        return False

    def _change_label_value(self, value):
        self.value_label.setText(str(value))
