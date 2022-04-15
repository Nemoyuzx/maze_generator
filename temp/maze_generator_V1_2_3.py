from pyqt5_pre_dispose import *
import sys
from random import randint, choice
from enum import Enum

map_deliever = 0

class entrance_UI(PyQt5_QDialog):
    def showDialog(self):
        self.show()
    
    def setupUI(self):  #设置窗口
        self.dialog_size_long = 800
        self.dialog_size_wide = 500
        self.button_size_long = self.dialog_size_long/2
        self.button_size_wide = 60

        self.setFixedSize(self.dialog_size_long,self.dialog_size_wide)           #设置窗口大小
        setBackground(self,"QDialog",'background.png')
        self.setWindowTitle('迷宫生成器 V1.2.2')           #设置窗口标题
        #self.setWindowIcon(QIcon('RESOURSE/drawable/program_Icon.png'))

        self.name_dialog = PyQt5_QLabel(self,self.dialog_size_long/4-25,30,600,200) #UI内标题
        self.name_dialog.setFont(QFont('宋体',20))
        setTextColor(self.name_dialog,"QLable",'white')
        self.name_dialog.setText('迷宫生成器 V1.2.2')


        self.enter_buttom_9_9 = PyQt5_QPushButton(self,self.dialog_size_long/4,self.button_size_long/3*2-self.button_size_wide,self.button_size_long,self.button_size_wide)   #按钮组件（左，上，宽，高）
        setBackground(self.enter_buttom_9_9,"QPushButton",'simple_buttom_#03A89E.png')  #设置按钮的背景图片
        setPressedBackground(self.enter_buttom_9_9,"QPushButton",'simple_buttom_#03A89E_dark.png')  #设置按钮被按压时的背景图片
        self.enter_buttom_9_9.setText('迷宫 9×9 双层')
        self.enter_buttom_9_9.clicked.connect(lambda:self.map_dispose_and_show(9))   #设置按钮的点击事件


        self.enter_buttom_13_13 = PyQt5_QPushButton(self,self.dialog_size_long/4,self.button_size_long/3*2+10+self.button_size_wide,self.button_size_long,self.button_size_wide)   #按钮组件（左，上，宽，高）
        setBackground(self.enter_buttom_13_13,"QPushButton","simple_buttom_#03A89E.png")  
        setPressedBackground(self.enter_buttom_13_13,"QPushButton","simple_buttom_#03A89E_dark.png")  
        self.enter_buttom_13_13.setText('迷宫 13×13 三层')
        self.enter_buttom_13_13.clicked.connect(lambda:self.map_dispose_and_show(13))  

    def map_dispose_and_show(self,size):
        if size == 9:
            from maze_generator_9time9_dispose_V1_2_3 import Compute_9time9,UI_show_map,answer
            Dispose = Compute_9time9()
            Dispose.dispose()
        if size == 13:
            from maze_generator_13time13_dispose_V1_2_3 import Compute_13time13,UI_show_map,answer
            Dispose = Compute_13time13()
            Dispose.dispose()
        dialog_Q = UI_show_map()
        dialog_Q.setupUI()
        dialog_A = answer()
        dialog_A.setupUI()
        dialog_A.showDialog()
        dialog_Q.showDialog()
    
class MAP_ENTRY_TYPE(Enum):
    MAP_EMPTY = 0,
    MAP_BLOCK = 1,

class WALL_DIRECTION(Enum):
    WALL_LEFT = 0,
    WALL_UP = 1,
    WALL_RIGHT = 2,
    WALL_DOWN = 3,

class Map():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]
    
    def resetMap(self, value):
        for y in range(self.height):
            for x in range(self.width):
                self.setMap(x, y, value)
    
    def setMap(self, x, y, value):
        if value == MAP_ENTRY_TYPE.MAP_EMPTY:
            self.map[y][x] = 0
        elif value == MAP_ENTRY_TYPE.MAP_BLOCK:
            self.map[y][x] = 1
    
    def isVisited(self, x, y):
        return self.map[y][x] != 1

    def showMap(self):
        for row in self.map:
            s = ''
            for entry in row:
                if entry == 0:
                    s += ' 0'
                elif entry == 1:
                    s += ' #'
                else:
                    s += ' X'
        global map_deliever
        map_deliever = self.map
        #print('map_deliever = ',map_deliever)
        #print(id(map_deliever))

# find unvisited adjacent entries of four possible entris
# then add random one of them to checklist and mark it as visited
def checkAdjacentPos(map, x, y, width, height, checklist):
    directions = []
    if x > 0:
        if not map.isVisited(2*(x-1)+1, 2*y+1):
            directions.append(WALL_DIRECTION.WALL_LEFT)
                
    if y > 0:
        if not map.isVisited(2*x+1, 2*(y-1)+1):
            directions.append(WALL_DIRECTION.WALL_UP)

    if x < width -1:
        if not map.isVisited(2*(x+1)+1, 2*y+1):
            directions.append(WALL_DIRECTION.WALL_RIGHT)
        
    if y < height -1:
        if not map.isVisited(2*x+1, 2*(y+1)+1):
            directions.append(WALL_DIRECTION.WALL_DOWN)
        
    if len(directions):
        direction = choice(directions)
        #print("(%d, %d) => %s" % (x, y, str(direction)))
        if direction == WALL_DIRECTION.WALL_LEFT:
                map.setMap(2*(x-1)+1, 2*y+1, MAP_ENTRY_TYPE.MAP_EMPTY)
                map.setMap(2*x, 2*y+1, MAP_ENTRY_TYPE.MAP_EMPTY)
                checklist.append((x-1, y))
        elif direction == WALL_DIRECTION.WALL_UP:
                map.setMap(2*x+1, 2*(y-1)+1, MAP_ENTRY_TYPE.MAP_EMPTY)
                map.setMap(2*x+1, 2*y, MAP_ENTRY_TYPE.MAP_EMPTY)
                checklist.append((x, y-1))
        elif direction == WALL_DIRECTION.WALL_RIGHT:
                map.setMap(2*(x+1)+1, 2*y+1, MAP_ENTRY_TYPE.MAP_EMPTY)
                map.setMap(2*x+2, 2*y+1, MAP_ENTRY_TYPE.MAP_EMPTY)
                checklist.append((x+1, y))
        elif direction == WALL_DIRECTION.WALL_DOWN:
            map.setMap(2*x+1, 2*(y+1)+1, MAP_ENTRY_TYPE.MAP_EMPTY)
            map.setMap(2*x+1, 2*y+2, MAP_ENTRY_TYPE.MAP_EMPTY)
            checklist.append((x, y+1))
        return True
    else:
        # if not find any unvisited adjacent entry
        return False
            
# recursive backtracker algorithm
def recursiveBacktracker(map, width, height):
    startX, startY =(randint(0, width-1), randint(0, height-1))
    print("start(%d, %d)" % (startX, startY))
    map.setMap(2*startX+1, 2*startY+1, MAP_ENTRY_TYPE.MAP_EMPTY)
    checklist = [] 
    checklist.append((startX, startY))
    while len(checklist):
        # use checklist as a stack, get entry from the top of stack 
        entry = checklist[-1]
        if not checkAdjacentPos(map, entry[0], entry[1], width, height, checklist):
            # the entry has no unvisited adjacent entry, so remove it from checklist
            checklist.remove(entry)
            
def doRecursiveBacktracker(map):
    # set all entries of map to wall
    map.resetMap(MAP_ENTRY_TYPE.MAP_BLOCK)
    recursiveBacktracker(map, (map.width-1)//2, (map.height-1)//2)

def run(map_weight,map_hight):
    WIDTH = map_weight        #迷宫的长度（格子数——注意两边的）
    HEIGHT = map_hight       #迷宫的高度（格子数——注意两边的）
    map = Map(WIDTH, HEIGHT)
    doRecursiveBacktracker(map)
    map.showMap()    

class data_exchange():
    def list_give_9(self,global_list):
        run(9,9)
        for x in range(9):
            for y in range(9):
                global_list.append(map_deliever[x][y])
        #global_list.clear()

    def list_give_13(self,global_list):
        run(13,13)
        for x in range(13):
            for y in range(13):
                global_list.append(map_deliever[x][y])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = entrance_UI()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()