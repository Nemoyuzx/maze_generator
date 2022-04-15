from tokenize import group
from pyqt5_pre_dispose import *
from maze_generator_V1_2_3 import data_exchange
from random import randint

global_list = []
False_and_True = []
label_sit_TRUE_or_FALSE_floor1 = []
label_sit_TRUE_or_FALSE_floor2 = []

class Compute_9time9():
    num = 0
    def dispose(self):
        front_give = data_exchange()
        front_give.list_give_9(global_list)
        Compute_9time9.num += 1
        self.label_sit_TRUE_or_FALSE()
        self.label_choise_enter_and_exit()
        self.label_sit_TRUE_or_FALSE_floor1_and_floor2()
        print(False_and_True)
        
    def label_sit_TRUE_or_FALSE(self):
        for x in range(81):
                if global_list[x] == 1:
                    False_and_True.append(True)
                if global_list[x] == 0:
                    False_and_True.append(False)
        #print(False_and_True)

    def label_choise_enter_and_exit(self):
        enter_sit = randint(0,1)
        #enter_sit = 1
        if enter_sit == 0:
            False_and_True[1] = False
        if enter_sit == 1:
            False_and_True[9] = False
        out_sit = randint(0,1)
        if out_sit == 0:
            False_and_True[79] = False
        if out_sit == 1:
            False_and_True[71] = False   

    def label_sit_TRUE_or_FALSE_floor1_and_floor2(self):
        for self.x in range(81):
            b = randint(0,1)
            if False_and_True[self.x] == False:
                label_sit_TRUE_or_FALSE_floor1.append(False)
                label_sit_TRUE_or_FALSE_floor2.append(False)
            if False_and_True[self.x] == True:
                if b == 0:
                    label_sit_TRUE_or_FALSE_floor1.append(True)
                    label_sit_TRUE_or_FALSE_floor2.append(False)
                if b == 1:
                    label_sit_TRUE_or_FALSE_floor1.append(False)
                    label_sit_TRUE_or_FALSE_floor2.append(True)

class UI_show_map(PyQt5_QDialog):
    def showDialog(self):
        self.show()

    def setupUI(self):
        self.dialog_size_long = 1800
        self.dialog_size_wide = 600
        self.setFixedSize(self.dialog_size_long,self.dialog_size_wide)
        self.setWindowTitle("双层9×9迷宫生成器   第%s个"%Compute_9time9.num)

        self.what1=PyQt5_QLabel(self,50,30,502,501)
        setBackground(self.what1,"Lable",'合成迷宫底_9乘9.jpg')
        self.what2=PyQt5_QLabel(self,50,30,502,501)
        setBackground(self.what2,"Label",'问号.png')
        #--------------------------------------------------------------
        self.group2=PyQt5_QGroupBox(self,650,30,502,501)
        setBackground(self.group2,"GroupBox",'合成迷宫底_9乘9.jpg')
        self.word_label1 = PyQt5_QLabel(self,830,551,250,30)
        self.word_label1.setText('第一层迷宫')

        for y in range(81):
            self.a = y
            self.add_label_2(y)

        self.group3=PyQt5_QGroupBox(self,1250,30,502,501)
        setBackground(self.group3,"GroupBox",'合成迷宫底_9乘9.jpg')
        self.word_label1 = PyQt5_QLabel(self,1440,551,250,30)
        self.word_label1.setText('第二层迷宫')

        for z in range(81):
            self.a = z
            self.add_label_3(z)

    def add_label_2(self,y):#55.56
        self.label = PyQt5_QLabel(self.group2,(y//9)*55.56,-2+(y%9)*55.56,57.56,58.56)
        setBackground(self.label,"Lable",'墙壁第一层单块.png')
        self.label.setVisible(label_sit_TRUE_or_FALSE_floor1[y])

    def add_label_3(self,z):#55.56
        self.label = PyQt5_QLabel(self.group3,(z//9)*55.56,-2+(z%9)*55.56,57.56,58.56)
        setBackground(self.label,"Lable",'墙壁第二层单块.png')
        self.label.setVisible(label_sit_TRUE_or_FALSE_floor2[z])
        


class answer(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(600,600)
        self.setWindowTitle("双层9×9迷宫生成器-答案界面  第%s个"%Compute_9time9.num)

        self.group1=PyQt5_QGroupBox(self,50,30,502,501)
        setBackground(self.group1,"GroupBox",'合成迷宫底_9乘9.jpg')
        self.word_label1 = PyQt5_QLabel(self,250,551,250,30)
        self.word_label1.setText('合成迷宫')

        for x in range(81):
            self.a = x
            self.add_label_1(x)

        False_and_True.clear()
        global_list.clear()
        label_sit_TRUE_or_FALSE_floor1.clear()
        label_sit_TRUE_or_FALSE_floor2.clear()

    def add_label_1(self,x):#55.56
        self.label = PyQt5_QLabel(self.group1,(x//9)*55.56,-2+(x%9)*55.56,57.56,58.56)
        setBackground(self.label,"Lable",'墙壁合成单块.png')
        self.label.setVisible(False_and_True[x])