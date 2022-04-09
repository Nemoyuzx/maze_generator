from VipCode import *
from maze_generator_V1_2_2 import data_exchange

global_list = []
False_and_True = []
label_sit_TRUE_or_FALSE_floor1 = []  #储存第一层地图墙壁单块信息
label_sit_TRUE_or_FALSE_floor2 = []  #储存第二层地图墙壁单块信息
label_sit_TRUE_or_FALSE_floor3 = []  #储存第三层地图墙壁单块信息

class Compute_13time13():
    num = 0
    def dispose(self):
        front_give = data_exchange()
        front_give.list_give_13(global_list)
        Compute_13time13.num += 1
        self.label_sit_TRUE_or_FALSE()
        self.label_choise_enter_and_exit()
        self.label_sit_TRUE_or_FALSE_floor1_and_floor2_and_floor3()
        #print(False_and_True)
        
    def label_sit_TRUE_or_FALSE(self):
        #print('测试点1 = ',global_list)
        for x in range(169):
            if global_list[x] == 1:
                False_and_True.append(True)
            if global_list[x] == 0:
                False_and_True.append(False)
        #print(False_and_True)

    def label_choise_enter_and_exit(self):
        enter_sit = random.randint(0,1)
        #enter_sit = 1
        if enter_sit == 0:
            False_and_True[1] = False
        if enter_sit == 1:
            False_and_True[13] = False
        out_sit = random.randint(0,1)
        if out_sit == 0:
            False_and_True[167] = False
        if out_sit == 1:
            False_and_True[155] = False

    def label_sit_TRUE_or_FALSE_floor1_and_floor2_and_floor3(self):
        for x in range(169):
            b = random.randint(0,2)
            if False_and_True[x] == False:
                label_sit_TRUE_or_FALSE_floor1.append(False)
                label_sit_TRUE_or_FALSE_floor2.append(False)
                label_sit_TRUE_or_FALSE_floor3.append(False)
            if False_and_True[x] == True:
                if b == 0:
                    label_sit_TRUE_or_FALSE_floor1.append(True)
                    label_sit_TRUE_or_FALSE_floor2.append(False)
                    label_sit_TRUE_or_FALSE_floor3.append(False)
                if b == 1:
                    label_sit_TRUE_or_FALSE_floor1.append(False)
                    label_sit_TRUE_or_FALSE_floor2.append(True)
                    label_sit_TRUE_or_FALSE_floor3.append(False)
                if b == 2:
                    label_sit_TRUE_or_FALSE_floor1.append(False)
                    label_sit_TRUE_or_FALSE_floor2.append(False)
                    label_sit_TRUE_or_FALSE_floor3.append(True)


class UI_show_map(PyQt5_QDialog):    #题目层
    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(2600,600)
        self.setWindowTitle("三层13×13迷宫生成器   第%s个"%Compute_13time13.num)
        #---------------------------------------------------二步----------------
        self.what1=PyQt5_Qlabel(self,50,30,502,501)
        self.what1.setBackground('合成迷宫底_13乘13.jpg')
        self.what2=PyQt5_Qlabel(self,50,30,502,501)
        self.what2.setBackground('问号.png')
        #---------------------------------------------------三部--1--------------
        self.group2=PyQt5_QGroupBox(self,650,30,502,501)
        self.group2.setBackground('合成迷宫底_13乘13.jpg')
        self.word_label1 = PyQt5_Qlabel(self,830,551,250,30)
        self.word_label1.setText('第一层迷宫')
        for y in range(169):
            self.a = y
            self.add_label_2(y)
        #---------------------------------------------------三部--2--------------
        self.group3=PyQt5_QGroupBox(self,1250,30,502,501)
        self.group3.setBackground('合成迷宫底_13乘13.jpg')
        self.word_label1 = PyQt5_Qlabel(self,1440,551,250,30)
        self.word_label1.setText('第二层迷宫')
        for z in range(169):
            self.a = z
            self.add_label_3(z)
        #---------------------------------------------------三部--3--------------
        self.group4=PyQt5_QGroupBox(self,1850,30,502,501)
        self.group4.setBackground('合成迷宫底_13乘13.jpg')
        self.word_label1 = PyQt5_Qlabel(self,2040,551,250,30)
        self.word_label1.setText('第三层迷宫')
        for w in range(169):
            self.a = w
            self.add_label_4(w)
        #-------------------------------------------------------------------

    def add_label_2(self,y):#55.56
        self.label = PyQt5_Qlabel(self.group2,3+(y//13)*38,2+(y%13)*38,40.4,40.4)
        self.label.setBackground('墙壁第一层单块.png')
        self.label.setVisible(label_sit_TRUE_or_FALSE_floor1[y])

    def add_label_3(self,z):#55.56
        self.label = PyQt5_Qlabel(self.group3,3+(z//13)*38,2+(z%13)*38,40.4,40.4)
        self.label.setBackground('墙壁第二层单块.png')
        self.label.setVisible(label_sit_TRUE_or_FALSE_floor2[z])
    
    def add_label_4(self,w):#55.56
        self.label = PyQt5_Qlabel(self.group4,3.5+(w//13)*38,3+(w%13)*38,41,40.4)
        self.label.setBackground('墙壁第三层单块.png')
        self.label.setVisible(label_sit_TRUE_or_FALSE_floor3[w])
        

class answer(PyQt5_QDialog):   #答案层

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(1200,600)
        self.setWindowTitle("三层13×13迷宫生成器-答案界面   第%s个"%Compute_13time13.num)

        self.group1=PyQt5_QGroupBox(self,50,30,502,501)
        self.group1.setBackground('合成迷宫底_13乘13.jpg')
        self.word_label1 = PyQt5_Qlabel(self,250,551,250,30)
        self.word_label1.setText('原迷宫')
        for x in range(169):
            self.a = x
            self.add_label_1(x)

        self.group5=PyQt5_QGroupBox(self,650,30,502,501)
        self.group5.setBackground('合成迷宫底_13乘13.jpg')
        self.word_label1 = PyQt5_Qlabel(self,830,551,250,30)
        self.word_label1.setText('合成迷宫')
        for y in range(169):
            self.a = y
            self.add_label_5(y)

        False_and_True.clear()
        global_list.clear()
        label_sit_TRUE_or_FALSE_floor1.clear()
        label_sit_TRUE_or_FALSE_floor2.clear()
        label_sit_TRUE_or_FALSE_floor3.clear()

    def add_label_1(self,x):#55.56
        self.label = PyQt5_Qlabel(self.group1,3+(x//13)*38,2+(x%13)*38,40.4,40.4)
        self.label.setBackground('墙壁合成单块.png')
        self.label.setVisible(False_and_True[x])

    def add_label_5(self,x):#55.56
        self.label1 = PyQt5_Qlabel(self.group5,3+(x//13)*38,2+(x%13)*38,40.4,40.4)
        self.label1.setBackground('墙壁第一层单块.png')
        self.label1.setVisible(label_sit_TRUE_or_FALSE_floor1[x])
        self.label2 = PyQt5_Qlabel(self.group5,3+(x//13)*38,2+(x%13)*38,40.4,40.4)
        self.label2.setBackground('墙壁第二层单块.png')
        self.label2.setVisible(label_sit_TRUE_or_FALSE_floor2[x])
        self.label3 = PyQt5_Qlabel(self.group5,3+(x//13)*38,2+(x%13)*38,40.4,40.4)
        self.label3.setBackground('墙壁第三层单块.png')
        self.label3.setVisible(label_sit_TRUE_or_FALSE_floor3[x])
