from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QMouseEvent, QFont
from PyQt6.QtWidgets import QDialog, QLabel, QPushButton, QGroupBox

class PyQt6_QDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("dialog")
        self.setFixedSize(600, 400)  # 设置固定的对话框大小
    def setBackgroundColor(self, file_name):
        self.setStyleSheet("#dialog{background-color:" + file_name + "}")
    def setBackground(self, file_name):
        self.setStyleSheet("#dialog{border-image:url(RESOURCE/drawable/" + file_name + ")}")

class PyQt6_QLabel(QLabel):
    clicked = pyqtSignal(QMouseEvent)
    def __init__(self, parent, x, y, width, height):
        super().__init__(parent)
        self.widget = parent
        self.setGeometry(int(x), int(y), int(width), int(height))
    def setBackground(self, file_name):
        self.setStyleSheet(self.styleSheet() + "border-image:url(RESOURCE/drawable/" + file_name + ");")
    def setBackgroundColor(self, file_name):
        self.setStyleSheet(self.styleSheet() + "background-color:" + file_name + ";")
    def setTextColor(self, file_name):
        self.setStyleSheet(self.styleSheet() + "color:" + file_name + ";")
    def setFrameSizeStyleColor(self, file_name):
        self.setStyleSheet(self.styleSheet() + "border:" + file_name + ";")
    def setFontSize(self, Size):
        font = QFont()
        font.setPointSize(Size)  # 设置字体大小为20
        self.setFont(font)
    
class PyQt6_QPushButton(QPushButton):
    def __init__(self, parent, x, y, width, height):
        super().__init__(parent)
        self.setGeometry(int(x), int(y), int(width), int(height))
    def setBackgroundimg(self, file_name):
        self.setStyleSheet(self.styleSheet() + "QPushButton{border-image:url(RESOURCE/drawable/" + file_name + ")}")
    def setPressedBackgroundimg(self, file_name):
        self.setStyleSheet(self.styleSheet() + "QPushButton:pressed{border-image:url(RESOURCE/drawable/" + file_name + ")}")
    def setBackgroundColor(self, file_name):
        self.setStyleSheet(self.styleSheet() + "QPushButton{background-color:" + file_name + "}")
    def setPressedBackgroundColor(self, file_name):
        self.setStyleSheet(self.styleSheet() + "QPushButton:pressed{background-color:" + file_name + "}")
    def setTextColor(self, file_name):
        self.setStyleSheet(self.styleSheet() + "QPushButton{color:" + file_name + "}")
    def setPressedTextColor(self, file_name):
        self.setStyleSheet(self.styleSheet() + "QPushButton:pressed{color:" + file_name + "}")

class PyQt6_QGroupBox(QGroupBox):
    def __init__(self, parent, x, y, width, height):
        super().__init__(parent)
        self.setGeometry(x, y, width, height)
        self.setObjectName("groupbox")
    def setBackground(self, file_name):
        self.setStyleSheet("#groupbox{border-image:url(RESOURCE/drawable/" + file_name + ")}")
    def setBackgroundColor(self, file_name):
        self.setStyleSheet("#groupbox{background-color:" + file_name + "}")
