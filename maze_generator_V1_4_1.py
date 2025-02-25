import sys
from pyqt6_pre_dispose import *
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont

dialog_backGround_color = "#082E54"
dialog_buttom_color = "#03A89E"
dialog_buttomPUSHED_color = "#028077"


class entrance_UI(PyQt6_QDialog):
    def showDialog(self):
        self.show()
    
    def setupUI(self):  #设置窗口
        self.dialog_size_long = 800
        self.dialog_size_wide = 500
        self.button_size_long = self.dialog_size_long/2
        self.button_size_wide = 60

        self.setFixedSize(self.dialog_size_long,self.dialog_size_wide)           #设置窗口大小
        self.setBackgroundColor(dialog_backGround_color)
        self.setWindowTitle('迷宫生成器 V1.2.2')           #设置窗口标题

        self.name_dialog = PyQt6_QLabel(self,self.dialog_size_long/4-25,30,600,200) #UI内标题
        self.name_dialog.setFont(QFont('宋体',20))
        self.name_dialog.setTextColor('#FFFFFF')
        self.name_dialog.setText('迷宫生成器 V1.2.2')

        self.enter_buttom_9_9 = PyQt6_QPushButton(self,self.dialog_size_long/4,self.button_size_long/3*2-self.button_size_wide,self.button_size_long,self.button_size_wide)   #按钮组件（左，上，宽，高）
        self.enter_buttom_9_9.setBackgroundColor(dialog_buttom_color) 
        self.enter_buttom_9_9.setPressedBackgroundColor(dialog_buttomPUSHED_color)  #设置按钮被按压时的背景图片
        self.enter_buttom_9_9.setText('迷宫 9 × 9 双层')
        self.enter_buttom_9_9.clicked.connect(lambda:self.map_dispose_and_show(9))   #设置按钮的点击事件

        self.enter_buttom_13_13 = PyQt6_QPushButton(self,self.dialog_size_long/4,self.button_size_long/3*2+10+self.button_size_wide,self.button_size_long,self.button_size_wide)   #按钮组件（左，上，宽，高）
        self.enter_buttom_13_13.setBackgroundColor(dialog_buttom_color)  
        self.enter_buttom_13_13.setPressedBackgroundColor(dialog_buttomPUSHED_color)  
        self.enter_buttom_13_13.setText('迷宫 13 × 13 三层')
        self.enter_buttom_13_13.clicked.connect(lambda:self.map_dispose_and_show(13))  

    def map_dispose_and_show(self,size):
        if size == 9:
            from maze_generator_9time9_dispose_V1_4_1 import Compute_9time9,UI_show_map,answer
            dialog = Compute_9time9()
            dialog.dispose()
        if size == 13:
            from maze_generator_13time13_dispose_V1_4_1 import Compute_13time13,UI_show_map,answer
            dialog = Compute_13time13()
            dialog.dispose()

        dialog_Q = UI_show_map() #问题和答案界面设置UI
        dialog_Q.setupUI()
        dialog_A = answer()
        dialog_A.setupUI()

        dialog_A.showDialog() #显示问题和答案界面
        dialog_Q.showDialog()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = entrance_UI()
    dialog.setupUI()
    dialog.showDialog()
    app.exec()