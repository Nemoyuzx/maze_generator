from pyqt6_pre_dispose import *
from maze_gener_Core import run
from random import randint

Maze_Side_length = 13
Maze_divi_layers = 3
layer1_color = 'blue'
layer2_color = 'red'
layer3_color = 'yellow'
NoneWall_color = 'grey'

F_a_T = []
label_sit_T_or_F_floor1 = []  #储存第一层地图墙壁单块信息
label_sit_T_or_F_floor2 = []  #储存第二层地图墙壁单块信息
label_sit_T_or_F_floor3 = []  #储存第三层地图墙壁单块信息

class Compute_13time13():
    num = 0
    def __init__(self):
        super().__init__()
        run(Maze_Side_length,Maze_Side_length)
        global map_deliever
        from maze_gener_Core import map_deliever
        
    def dispose(self):
        Compute_13time13.num += 1
        self.label_sit_TRUE_or_FALSE()
        self.label_choise_enter_and_exit()
        self.label_sit_T_or_F_floor1_and_floor2_and_floor3()
        #print(F_a_T)
        
    def label_sit_TRUE_or_FALSE(self):
        #print('测试点1 = ',map_deliever)
        for x in range(Maze_Side_length):
            for y in range(Maze_Side_length):
                if map_deliever[x][y] == 1:
                    F_a_T.append(True)
                elif map_deliever[x][y] == 0:
                    F_a_T.append(False)
        #print(F_a_T)

    def label_choise_enter_and_exit(self):
        enter_sit = randint(0,1)
        #enter_sit = 1
        if enter_sit == 0:
            F_a_T[1] = False
        if enter_sit == 1:
            F_a_T[13] = False
        out_sit = randint(0,1)
        if out_sit == 0:
            F_a_T[167] = False
        if out_sit == 1:
            F_a_T[155] = False

    def label_sit_T_or_F_floor1_and_floor2_and_floor3(self):
        for x in range(Maze_Side_length**2):
            b = randint(0,2)
            if F_a_T[x] == False:
                label_sit_T_or_F_floor1.append(False)
                label_sit_T_or_F_floor2.append(False)
                label_sit_T_or_F_floor3.append(False)
            if F_a_T[x] == True:
                if b == 0:
                    label_sit_T_or_F_floor1.append(True)
                    label_sit_T_or_F_floor2.append(False)
                    label_sit_T_or_F_floor3.append(False)
                if b == 1:
                    label_sit_T_or_F_floor1.append(False)
                    label_sit_T_or_F_floor2.append(True)
                    label_sit_T_or_F_floor3.append(False)
                if b == 2:
                    label_sit_T_or_F_floor1.append(False)
                    label_sit_T_or_F_floor2.append(False)
                    label_sit_T_or_F_floor3.append(True)

class UI_show_map(PyQt6_QDialog):    #题目层
    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(2400,600)
        self.setWindowTitle("三层13×13迷宫生成器   第%s个"%Compute_13time13.num)
        #---------------------------------------------------二步----------------
        self.group1=PyQt6_QGroupBox(self,50,30,13*40,13*40)
        LabelAdding.add_label_NoneWall(self,Maze_Side_length,self.group1) 
        self.what=PyQt6_QLabel(self.group1,0,0,13*40,13*40)
        self.what.setText('?')
        self.what.setFontSize(130)
        self.what.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #---------------------------------------------------三部--1--------------
        self.word_label2 = PyQt6_QLabel(self,50+13*40+50,550,520,40)
        self.word_label2.setText('第一层迷宫')
        self.word_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.group2=PyQt6_QGroupBox(self,50+13*40+50,30,13*40,13*40)
        LabelAdding.add_label(self,self.group2,layer1_color,Maze_Side_length,label_sit_T_or_F_floor1)
        #---------------------------------------------------三部--2--------------
        self.word_label3 = PyQt6_QLabel(self,1190,550,520,40)
        self.word_label3.setText('第二层迷宫')
        self.word_label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.group3=PyQt6_QGroupBox(self,1190,30,13*40,13*40)
        LabelAdding.add_label(self,self.group3,layer2_color,Maze_Side_length,label_sit_T_or_F_floor2)
        #---------------------------------------------------三部--3--------------
        self.word_label4 = PyQt6_QLabel(self,1760,550,520,40)
        self.word_label4.setText('第三层迷宫')
        self.word_label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.group4=PyQt6_QGroupBox(self,1760,30,13*40,13*40)
        LabelAdding.add_label(self,self.group4,layer3_color,Maze_Side_length,label_sit_T_or_F_floor3)

class answer(PyQt6_QDialog):   #答案层
    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(1200,600)
        self.setWindowTitle("三层13×13迷宫生成器-答案界面   第%s个"%Compute_13time13.num)

        self.word_label1 = PyQt6_QLabel(self,250,551,250,30)
        self.word_label1.setText('原迷宫')
        self.group1=PyQt6_QGroupBox(self,50,30,40*Maze_Side_length,40*Maze_Side_length)
        LabelAdding.add_label(self,self.group1,'purple',13,F_a_T)

        self.word_label1 = PyQt6_QLabel(self,830,551,250,30)
        self.word_label1.setText('合成迷宫')
        self.group5=PyQt6_QGroupBox(self,650,30,40*Maze_Side_length,40*Maze_Side_length)
        LabelAdding.add_label_Diff_All_Wall(self,Maze_Side_length,self.group5)

        F_a_T.clear()
        map_deliever.clear()
        label_sit_T_or_F_floor1.clear()
        label_sit_T_or_F_floor2.clear()
        label_sit_T_or_F_floor3.clear()

    def add_label_5(self,x):#55.56
        self.label1 = PyQt6_QLabel(self.group5,(x//13)*40,(x%13)*40,40,40)
        self.label1.setVisible(label_sit_T_or_F_floor1[x])

        self.label2 = PyQt6_QLabel(self.group5,(x//13)*40,(x%13)*40,40,40)
        self.label2.setVisible(label_sit_T_or_F_floor2[x])

        self.label3 = PyQt6_QLabel(self.group5,(x//13)*40,(x%13)*40,40,40)
        self.label3.setVisible(label_sit_T_or_F_floor3[x])

class LabelAdding():
    def add_label(self,group_num,label_color,Side_length,label_list): #单块层显示
            for x in range(Side_length**2):
                self.label = PyQt6_QLabel(group_num,(x//Side_length)*40,(x%Side_length)*40,40,40)
                if label_list[x] == True :
                    self.label.setBackgroundColor(label_color)
                else:
                    self.label.setBackgroundColor(NoneWall_color)
                self.label.setFrameSizeStyleColor('1px solid black')

    def add_label_NoneWall(self,Side_length,group_num):
        for x in range(Side_length**2):
            self.what1_unit=PyQt6_QLabel(group_num,(x//13)*40,(x%13)*40,40,40)
            self.what1_unit.setBackgroundColor(NoneWall_color)
            self.what1_unit.setFrameSizeStyleColor('1px solid black')

    def add_label_Diff_All_Wall(self,Side_length,group_num):
        for x in range(Side_length**2):
            self.label = PyQt6_QLabel(group_num,(x//Side_length)*40,(x%Side_length)*40,40,40)
            if label_sit_T_or_F_floor1[x] == True :
                self.label.setBackgroundColor(layer1_color)
            elif label_sit_T_or_F_floor2[x] == True :
                self.label.setBackgroundColor(layer2_color)
            elif label_sit_T_or_F_floor3[x] == True :
                self.label.setBackgroundColor(layer3_color)
            else:
                self.label.setBackgroundColor(NoneWall_color)
            self.label.setFrameSizeStyleColor('1px solid black')
