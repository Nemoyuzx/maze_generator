from pyqt6_pre_dispose import *
from maze_gener_Core import run
from random import randint

Maze_Side_length = 9
Maze_divi_layers = 2
layer1_color = 'blue'
layer2_color = 'red'
NoneWall_color = 'grey'

label_block_side_long = 55

dialog_size_long = 50*4+Maze_Side_length*label_block_side_long*3
dialog_size_wide = 600

False_and_True = []
label_sit_T_or_F_floor1 = []  #储存第一层地图墙壁单块信息
label_sit_T_or_F_floor2 = []  #储存第二层地图墙壁单块信息

class Compute_9time9():
    num = 0
    def __init__(self):
        super().__init__()
        run(Maze_Side_length,Maze_Side_length)
        global map_deliever
        from maze_gener_Core import map_deliever
        
    def dispose(self):
        Compute_9time9.num += 1
        self.label_sit_TRUE_or_FALSE()
        self.label_choise_enter_and_exit()
        self.label_sit_T_or_F_floor1_and_floor2()
        #print(False_and_True)
        
    def label_sit_TRUE_or_FALSE(self): #将map_deliever中的列表嵌套形式改为按顺序填充
        #print('测试点1 = ',map_deliever)
        for x in range(Maze_Side_length):
            for y in range(Maze_Side_length):
                if map_deliever[x][y] == 1:
                    False_and_True.append(True)
                elif map_deliever[x][y] == 0:
                    False_and_True.append(False)
        #print(False_and_True)

    def label_choise_enter_and_exit(self): #选择迷宫出入口（两个角上随机两个）
        enter_sit = randint(0,1)  #入口随机选择
        if enter_sit == 0:
            False_and_True[1] = False
        if enter_sit == 1:
            False_and_True[9] = False

        out_sit = randint(0,1)  #出口随机选择
        if out_sit == 0:
            False_and_True[79] = False
        if out_sit == 1:
            False_and_True[71] = False  

    def label_sit_T_or_F_floor1_and_floor2(self): #迷宫拆分，墙壁单块随机分入两个列表
        for x in range(Maze_Side_length**2):
            #print(x)
            b = randint(0,Maze_divi_layers-1)
            #print(b)
            if False_and_True[x] == False:
                label_sit_T_or_F_floor1.append(False)
                label_sit_T_or_F_floor2.append(False)
            if False_and_True[x] == True:
                if b == 0:
                    label_sit_T_or_F_floor1.append(True)
                    label_sit_T_or_F_floor2.append(False)
                if b == 1:
                    label_sit_T_or_F_floor1.append(False)
                    label_sit_T_or_F_floor2.append(True)

        #print(label_sit_T_or_F_floor1)
        #print(label_sit_T_or_F_floor2)


class UI_show_map(PyQt6_QDialog):    #题目层
    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(dialog_size_long,dialog_size_wide)
        self.setWindowTitle("双层9x9迷宫生成器   第%s个"%Compute_9time9.num)
        #---------------------------------------------------二步----------------
        self.group1=PyQt6_QGroupBox(self,50,30,Maze_Side_length*label_block_side_long,Maze_Side_length*label_block_side_long)
        LabelAdding.add_label_NoneWall(self,Maze_Side_length,self.group1) 
        self.what=PyQt6_QLabel(self.group1,0,0,Maze_Side_length*label_block_side_long,Maze_Side_length*label_block_side_long)
        self.what.setText('?')
        self.what.setFontSize(130)
        self.what.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #---------------------------------------------------三部--1--------------
        self.word_label2 = PyQt6_QLabel(self,50*2+Maze_Side_length*label_block_side_long,30+Maze_Side_length*label_block_side_long,Maze_Side_length*label_block_side_long,label_block_side_long)
        self.word_label2.setText('第一层迷宫')
        self.word_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.group2=PyQt6_QGroupBox(self,50*2+Maze_Side_length*label_block_side_long,30,Maze_Side_length*label_block_side_long,Maze_Side_length*label_block_side_long)
        LabelAdding.add_label(self,self.group2,layer1_color,Maze_Side_length,label_sit_T_or_F_floor1)
        #---------------------------------------------------三部--2--------------
        self.word_label3 = PyQt6_QLabel(self,50*3+Maze_Side_length*label_block_side_long*2,30+Maze_Side_length*label_block_side_long,Maze_Side_length*label_block_side_long,label_block_side_long)
        self.word_label3.setText('第二层迷宫')
        self.word_label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.group3=PyQt6_QGroupBox(self,50*3+Maze_Side_length*label_block_side_long*2,30,Maze_Side_length*label_block_side_long,Maze_Side_length*label_block_side_long)
        LabelAdding.add_label(self,self.group3,layer2_color,Maze_Side_length,label_sit_T_or_F_floor2)

class answer(PyQt6_QDialog):   #答案层
    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(1200,600)
        self.setWindowTitle("双层9x9迷宫生成器-答案界面   第%s个"%Compute_9time9.num)

        self.word_label1 = PyQt6_QLabel(self,250,551,250,30)
        self.word_label1.setText('原迷宫')
        self.group1=PyQt6_QGroupBox(self,50,30,label_block_side_long*Maze_Side_length,label_block_side_long*Maze_Side_length)
        LabelAdding.add_label(self,self.group1,'purple',Maze_Side_length,False_and_True)

        self.word_label1 = PyQt6_QLabel(self,830,551,250,30)
        self.word_label1.setText('合成迷宫')
        self.group5=PyQt6_QGroupBox(self,650,30,label_block_side_long*Maze_Side_length,label_block_side_long*Maze_Side_length)
        LabelAdding.add_label_Diff_All_Wall(self,Maze_Side_length,self.group5)

        False_and_True.clear()
        map_deliever.clear()
        label_sit_T_or_F_floor1.clear()
        label_sit_T_or_F_floor2.clear()

    def add_label_5(self,x):#55.56
        self.label1 = PyQt6_QLabel(self.group5,(x//Maze_Side_length)*label_block_side_long,(x%Maze_Side_length)*label_block_side_long,label_block_side_long,label_block_side_long)
        self.label1.setVisible(label_sit_T_or_F_floor1[x])

        self.label2 = PyQt6_QLabel(self.group5,(x//Maze_Side_length)*label_block_side_long,(x%Maze_Side_length)*label_block_side_long,label_block_side_long,label_block_side_long)
        self.label2.setVisible(label_sit_T_or_F_floor2[x])

class LabelAdding():
    def add_label(self,group_num,label_color,Side_length,label_list): #单块层显示
            print('test=',label_list)
            for x in range(Side_length**2):
                #print(x)
                self.label = PyQt6_QLabel(group_num,(x//Side_length)*label_block_side_long,(x%Side_length)*label_block_side_long,label_block_side_long,label_block_side_long)
                if label_list[x] == True :
                    self.label.setBackgroundColor(label_color)
                else:
                    self.label.setBackgroundColor(NoneWall_color)
                self.label.setFrameSizeStyleColor('1px solid black')

    def add_label_NoneWall(self,Side_length,group_num):
        for x in range(Side_length**2):
            self.what1_unit=PyQt6_QLabel(group_num,(x//Maze_Side_length)*label_block_side_long,(x%Maze_Side_length)*label_block_side_long,label_block_side_long,label_block_side_long)
            self.what1_unit.setBackgroundColor(NoneWall_color)
            self.what1_unit.setFrameSizeStyleColor('1px solid black')

    def add_label_Diff_All_Wall(self,Side_length,group_num):
        for x in range(Side_length**2):
            self.label = PyQt6_QLabel(group_num,(x//Side_length)*label_block_side_long,(x%Side_length)*label_block_side_long,label_block_side_long,label_block_side_long)
            if label_sit_T_or_F_floor1[x] == True :
                self.label.setBackgroundColor(layer1_color)
            elif label_sit_T_or_F_floor2[x] == True :
                self.label.setBackgroundColor(layer2_color)
            else:
                self.label.setBackgroundColor(NoneWall_color)
            self.label.setFrameSizeStyleColor('1px solid black')
