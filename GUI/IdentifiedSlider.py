from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt

class IdentifiedSlider(QSlider):
    def __init__(self,observer,range,value=0):
        super().__init__()
        self.observer=observer
        self.setOrientation(Qt.Horizontal)
        self.setMinimum(0)
        self.setMaximum(100 if range else 1)
        self.setValue(value)
        self.valueChanged.connect(self._value_changed_by_user)


    def _value_changed_by_user(self):
        self.observer.notify(self.value())

    def change_value(self,value):
        self.blockSignals(True)
        self.setValue(value)
        self.blockSignals(False)
