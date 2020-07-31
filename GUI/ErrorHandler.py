import tkinter as tk

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QLabel


class ErrorHandler:
    def __init__(self,parent):
        self.parent=parent


    def create_error(self,message):
        window=QWidget()
        window.setWindowTitle("Error")
        layout=QHBoxLayout()
        label=QLabel(text=message)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.parent.setLayout(layout)
        self.parent.setWindowTitle("ERROR")