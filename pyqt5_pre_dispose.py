from PyQt5.QtCore import pyqtSignal #line:1
from PyQt5.QtGui import QFont,QMouseEvent
from PyQt5.QtWidgets import QDialog,QLabel,QPushButton,QGroupBox,QApplication#line:3

parwidth =600 #line:13

class PyQt5_QDialog (QDialog):#line:29
    def __init__ (self):#line:30
        super().__init__ ()#line:31
        self.setObjectName ("dialog")#line:32
        global parwidth #line:33
        parwidth = self.width()#+200 
    def setBackgroundColor (self,file_name ):#line:35
        self.setStyleSheet ("#dialog{background-color:"+file_name +"}")#line:36
    def setBackground (self ,file_name ):#line:37
        self .setStyleSheet ("#dialog{border-image:url(RESOURCE/drawable/"+file_name +")}")#line:38


class PyQt5_QLabel(QLabel):#line:190
    clicked = pyqtSignal(QMouseEvent )#line:191
    def __init__(self,object,x,y,width,height):#line:192
        super ().__init__(object)#line:193
        self .widget = object #line:194
        self .zeze = True #line:195
        self .setGeometry (int(x),int(y) ,int(width) ,int(height) )#line:196
    def setBackground (self ,file_name ):#line:205
        self .setStyleSheet (self .styleSheet ()+"border-image:url(RESOURCE/drawable/"+file_name +");")#line:206
    def setBackgroundColor (self ,file_name ):#line:208
        self .setStyleSheet (self .styleSheet ()+"background-color:"+file_name +";")#line:209
    def setTextColor (self ,file_name ):#line:211
        self .setStyleSheet (self .styleSheet ()+"color:"+file_name +";")#line:212

    

class PyQt5_QPushButton (QPushButton ):#line:125
    def __init__ (self,object,x ,y ,width ,height ):#line:126
        super ().__init__ (object )#line:127
        self .setGeometry (int(x),int(y),int(width),int(height))#line:128
    def setBackground (self ,file_name ):#line:130
        self .setStyleSheet (self .styleSheet ()+"QPushButton{border-image:url(RESOURCE/drawable/"+file_name +")}")#line:132
    def setPressedBackground (self ,file_name ):#line:134
        self .setStyleSheet (self .styleSheet ()+"QPushButton:pressed{border-image:url(RESOURCE/drawable/"+file_name +")}")#line:136
    def setBackgroundColor (self ,file_name ):#line:138
        self .setStyleSheet (self .styleSheet ()+"QPushButton{background-color:"+file_name +"}")#line:139
    def setTextColor (self ,file_name ):#line:141
        self .setStyleSheet (self .styleSheet ()+"QPushButton{color:"+file_name +"}")#line:142
    def setPressedTextColor (self ,file_name ):#line:144
        self .setStyleSheet (self .styleSheet ()+"QPushButton:pressed{color:"+file_name +"}")#line:145


class PyQt5_QGroupBox (QGroupBox ):#line:366
    def __init__ (self ,object ,x,y,width,height):#line:367
        super ().__init__ (object )#line:368
        self .setGeometry (x ,y ,width ,height )#line:369
        self .setObjectName ("groupbox")#line:370
    def setBackground (self ,file_name ):#line:372
        self .setStyleSheet ("#groupbox{border-image:url(RESOURCE/drawable/"+file_name +")}")#line:373
    def setBackgroundColor (self ,file_name ):#line:375
        self .setStyleSheet ("#groupbox{background-color:"+file_name +"}")#line:376


