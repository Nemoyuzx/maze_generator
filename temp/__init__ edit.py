from PyQt5 .QtCore import *#line:1
from PyQt5 .QtGui import *#line:2
from PyQt5 .QtWidgets import *#line:3
import sys #line:4
import os #line:5
import json #line:6
import pygame #line:7
import time #line:8
import random #line:9
import math #line:10
import requests #line:11
parwidth =600 #line:13
flg =0 #line:15
fff =0 #line:16
f =0 #line:17
border =0 #line:18
borderr =0 #line:19
angle =1 #line:20
direction =1 #line:21
ipStr ='http://jiaoxue.vipcode.cn/ti/findById.do'#line:23
global filename #line:25
filename =""#line:26
class PyQt5_QDialog (QDialog ):#line:29
    def __init__ (O0000O0O00OOOOOOO ):#line:30
        super ().__init__ ()#line:31
        O0000O0O00OOOOOOO .setObjectName ("dialog")#line:32
        global parwidth #line:33
        parwidth =O0000O0O00OOOOOOO .width ()+200 #line:34
    def setBackgroundColor (OOOOO0O0O00O00OOO ,OOO00OOOO00OO0OO0 ):#line:35
        OOOOO0O0O00O00OOO .setStyleSheet ("#dialog{background-color:"+OOO00OOOO00OO0OO0 +"}")#line:36
    def setBackground (O000OO0000000O000 ,O0OOO000O00O0OOOO ):#line:37
        O000OO0000000O000 .setStyleSheet ("#dialog{border-image:url(RESOURCE/drawable/"+O0OOO000O00O0OOOO +")}")#line:38
    def setResize (O0OO0OOO0O0OO0OO0 ,OO0OO000OOOO0000O ,OOO0OO000000O0OOO ):#line:40
        O0OO0OOO0O0OO0OO0 .resize (OO0OO000OOOO0000O ,OOO0OO000000O0OOO )#line:41
    def addBodyButton (OOO0OO0OOOOO0O0O0 ,O0OOO00OOO0O0000O ):#line:43
        OOO0OO0OOOOO0O0O0 .bodylabel =O0OOO00OOO0O0000O #line:44
        OOO0OO0OOOOO0O0O0 .head =PyQt5_QPushButton (OOO0OO0OOOOO0O0O0 ,400 ,300 ,160 ,130 )#line:45
        OOO0OO0OOOOO0O0O0 .head .setBackgroundColor ("rgba(100,0, 200, 0)")#line:46
        OOO0OO0OOOOO0O0O0 .body =PyQt5_QPushButton (OOO0OO0OOOOO0O0O0 ,445 ,430 ,70 ,80 )#line:48
        OOO0OO0OOOOO0O0O0 .body .setBackgroundColor ("rgba(100,0, 200, 0)")#line:49
        OOO0OO0OOOOO0O0O0 .leftArm =PyQt5_QPushButton (OOO0OO0OOOOO0O0O0 ,420 ,430 ,40 ,30 )#line:51
        OOO0OO0OOOOO0O0O0 .leftArm .setBackgroundColor ("rgba(0,0, 0, 0)")#line:52
        OOO0OO0OOOOO0O0O0 .rightArm =PyQt5_QPushButton (OOO0OO0OOOOO0O0O0 ,505 ,430 ,50 ,30 )#line:54
        OOO0OO0OOOOO0O0O0 .rightArm .setBackgroundColor ("rgba(0,0, 0, 0)")#line:55
        OOO0OO0OOOOO0O0O0 .leftFoot =PyQt5_QPushButton (OOO0OO0OOOOO0O0O0 ,440 ,500 ,30 ,30 )#line:57
        OOO0OO0OOOOO0O0O0 .leftFoot .setBackgroundColor ("rgba(0,0, 0, 0)")#line:58
        OOO0OO0OOOOO0O0O0 .rightFoot =PyQt5_QPushButton (OOO0OO0OOOOO0O0O0 ,500 ,500 ,30 ,30 )#line:60
        OOO0OO0OOOOO0O0O0 .rightFoot .setBackgroundColor ("rgba(0,0, 0, 0)")#line:61
        OOO0OO0OOOOO0O0O0 .head .clicked .connect (OOO0OO0OOOOO0O0O0 .headClicked )#line:63
        OOO0OO0OOOOO0O0O0 .leftArm .clicked .connect (OOO0OO0OOOOO0O0O0 .armClicked )#line:64
        OOO0OO0OOOOO0O0O0 .rightArm .clicked .connect (OOO0OO0OOOOO0O0O0 .armClicked )#line:65
        OOO0OO0OOOOO0O0O0 .rightFoot .clicked .connect (OOO0OO0OOOOO0O0O0 .rightFootClicked )#line:66
        OOO0OO0OOOOO0O0O0 .leftFoot .clicked .connect (OOO0OO0OOOOO0O0O0 .leftFootClicked )#line:67
        OOO0OO0OOOOO0O0O0 .body .clicked .connect (OOO0OO0OOOOO0O0O0 .bodyClicked )#line:68
    def armClicked (O00OO0O00OO00000O ):#line:69
        O00OO0O00OO00000O .neibu2 ('main_arm')#line:70
        O00OO0O00OO00000O .neibu1 ('main_arm')#line:75
    def leftFootClicked (OOOO000OOO0000000 ):#line:76
        OOOO000OOO0000000 .neibu2 ('main_leftFoot')#line:77
        OOOO000OOO0000000 .neibu1 ('main_leftFoot')#line:78
    def rightFootClicked (OO0O000O00O00OOO0 ):#line:79
        OO0O000O00O00OOO0 .neibu2 ('main_rightFoot')#line:80
        OO0O000O00O00OOO0 .neibu1 ('main_rightFoot')#line:81
    def bodyClicked (OO0OO0OO000O0OOOO ):#line:82
        OO0OO0OO000O0OOOO .neibu2 ('main_body')#line:83
        OO0OO0OO000O0OOOO .neibu1 ('main_body')#line:84
    def headClicked (OOOO00O0O0O0OOO0O ):#line:85
        OOOO00O0O0O0OOO0O .neibu2 ('main_head')#line:86
        OOOO00O0O0O0OOO0O .neibu1 ('main_head')#line:87
    def neibu2 (O00O0OOO0O00000O0 ,O0O0O00OO0OO0O000 ):#line:89
        O00O0OOO0O00000O0 .neigif =PyQt5_QMovie (O0O0O00OO0OO0O000 +'.gif')#line:91
        O00O0OOO0O00000O0 .neigif .setScaledSize (O00O0OOO0O00000O0 .bodylabel .size ())#line:93
        O00O0OOO0O00000O0 .bodylabel .setMovie (O00O0OOO0O00000O0 .neigif )#line:95
        O00O0OOO0O00000O0 .neigif .start ()#line:97
        O00O0OOO0O00000O0 .frameCount =O00O0OOO0O00000O0 .neigif .frameCount ()#line:98
        O00O0OOO0O00000O0 .neigif .frameChanged .connect (O00O0OOO0O00000O0 .neibu3 )#line:100
    def neibu3 (OO000O0OO0000O0OO ):#line:101
        OO000O0OO0000O0OO .frameCount -=1 #line:103
        if OO000O0OO0000O0OO .frameCount ==0 :#line:105
            OO000O0OO0000O0OO .neigif .stop ()#line:107
            OO000O0OO0000O0OO .neigif =PyQt5_QMovie ('main_lion.gif')#line:109
            OO000O0OO0000O0OO .neigif .setScaledSize (OO000O0OO0000O0OO .bodylabel .size ())#line:110
            OO000O0OO0000O0OO .bodylabel .setMovie (OO000O0OO0000O0OO .neigif )#line:112
            OO000O0OO0000O0OO .neigif .start ()#line:114
    def neibu1 (O0OO00OO0O00OO000 ,OOOO00000OO0OO00O ):#line:116
        OOOO00O0OO00OO0OO =PyQt5_QMediaPlayer ()#line:118
        OOOO00O0OO00OO0OO .prepare_audio (OOOO00000OO0OO00O +'.wav')#line:120
        OOOO00O0OO00OO0OO .play ()#line:122
class PyQt5_QPushButton (QPushButton ):#line:125
    def __init__ (O0O000OO00OO0OOO0 ,O0O000OOOOOOOOO0O ,x =0 ,y =0 ,width =113 ,height =32 ):#line:126
        super ().__init__ (O0O000OOOOOOOOO0O )#line:127
        O0O000OO00OO0OOO0 .setGeometry (x ,y ,width ,height )#line:128
    def setBackground (OOOOOO0O000O00O0O ,OOO000OO0OO00OO0O ):#line:130
        OOOOOO0O000O00O0O .setStyleSheet (OOOOOO0O000O00O0O .styleSheet ()+"QPushButton{border-image:url(RESOURCE/drawable/"+OOO000OO0OO00OO0O +")}")#line:132
    def setPressedBackground (OOOOO0000OO0OO0OO ,O0O00O0OOO0OO0OOO ):#line:134
        OOOOO0000OO0OO0OO .setStyleSheet (OOOOO0000OO0OO0OO .styleSheet ()+"QPushButton:pressed{border-image:url(RESOURCE/drawable/"+O0O00O0OOO0OO0OOO +")}")#line:136
    def setBackgroundColor (O0OO000OOOOOOO0O0 ,O000OO0OOO0000000 ):#line:138
        O0OO000OOOOOOO0O0 .setStyleSheet (O0OO000OOOOOOO0O0 .styleSheet ()+"QPushButton{background-color:"+O000OO0OOO0000000 +"}")#line:139
    def setTextColor (OO00O0OOOOO0OOOOO ,OOOO00OOO0OOO0OOO ):#line:141
        OO00O0OOOOO0OOOOO .setStyleSheet (OO00O0OOOOO0OOOOO .styleSheet ()+"QPushButton{color:"+OOOO00OOO0OOO0OOO +"}")#line:142
    def setPressedTextColor (O00OO0OOO0O0OOOOO ,O0OOO000OOOO0O00O ):#line:144
        O00OO0OOO0O0OOOOO .setStyleSheet (O00OO0OOO0O0OOOOO .styleSheet ()+"QPushButton:pressed{color:"+O0OOO000OOOO0O00O +"}")#line:145
    def setFontSize (O00OO0OOO00000OOO ,OOOOOOOO0O0OOOOOO ):#line:147
        OO00OO0OO00O0OOOO =QFont ()#line:148
        OO00OO0OO00O0OOOO .setPixelSize (OOOOOOOO0O0OOOOOO )#line:149
        O00OO0OOO00000OOO .setFont (OO00OO0OO00O0OOOO )#line:150
class PyQt5_QLineEdit (QLineEdit ):#line:153
    Password =QLineEdit .Password #line:154
    Normal =QLineEdit .Normal #line:155
    NoEcho =QLineEdit .NoEcho #line:156
    PasswordEchoOnEdit =QLineEdit .PasswordEchoOnEdit #line:157
    def __init__ (OO00O0O0O000O0O0O ,O00OO0OO0OO0OO0OO ,x =0 ,y =0 ,width =113 ,height =21 ):#line:159
        super ().__init__ (O00OO0OO0OO0OO0OO )#line:160
        OO00O0O0O000O0O0O .setGeometry (x ,y ,width ,height )#line:161
        OO00O0O0O000O0O0O .setFontSize (14 )#line:162
        OO00O0O0O000O0O0O .setAlignment (Qt .AlignVCenter )#line:163
    def setFontSize (OOOOOO0OO0O0O0OO0 ,O00OOO0O000O0O0OO ):#line:165
        OOOOO00O0OO00OOO0 =QFont ()#line:166
        OOOOO00O0OO00OOO0 .setPixelSize (O00OOO0O000O0O0OO )#line:167
        OOOOOO0OO0O0O0OO0 .setFont (OOOOO00O0OO00OOO0 )#line:168
    def setBackground (OOO0OOO00O0OOO000 ,OO0O0000000O0O00O ):#line:170
        OOO0OOO00O0OOO000 .setStyleSheet (OOO0OOO00O0OOO000 .styleSheet ()+"border-image:url(RESOURCE/drawable/"+OO0O0000000O0O00O +");")#line:171
    def setBackgroundColor (O00OO00O0OOO00OOO ,OOOO000OO0O00O000 ):#line:173
        O00OO00O0OOO00OOO .setStyleSheet (O00OO00O0OOO00OOO .styleSheet ()+"background-color:"+OOOO000OO0O00O000 +";")#line:174
    def setTextColor (OOOO00O0OOO000OOO ,O0OOOOO0OO0O0OO0O ):#line:176
        OOOO00O0OOO000OOO .setStyleSheet (OOOO00O0OOO000OOO .styleSheet ()+"color:"+O0OOOOO0OO0O0OO0O +";")#line:177
    def setDisplayMode (OOOO0O000O0OO0O0O ,OO0O0OOOO0OO000OO ):#line:179
        if OO0O0OOOO0OO000OO ==PyQt5_QLineEdit .Password :#line:180
            OOOO0O000O0OO0O0O .setEchoMode (OO0O0OOOO0OO000OO )#line:181
        elif OO0O0OOOO0OO000OO ==PyQt5_QLineEdit .Normal :#line:182
            OOOO0O000O0OO0O0O .setEchoMode (OO0O0OOOO0OO000OO )#line:183
        elif OO0O0OOOO0OO000OO ==PyQt5_QLineEdit .NoEcho :#line:184
            OOOO0O000O0OO0O0O .setEchoMode (OO0O0OOOO0OO000OO )#line:185
        elif OO0O0OOOO0OO000OO ==PyQt5_QLineEdit .PasswordEchoOnEdit :#line:186
            OOOO0O000O0OO0O0O .setEchoMode (OO0O0OOOO0OO000OO )#line:187
class PyQt5_Qlabel (QLabel ):#line:190
    clicked =pyqtSignal (QMouseEvent )#line:191
    def __init__ (O0000O0OOOOO00O00 ,O0000O0O000000OO0 ,x =0 ,y =0 ,width =60 ,height =16 ):#line:192
        super ().__init__ (O0000O0O000000OO0 )#line:193
        O0000O0OOOOO00O00 .widget =O0000O0O000000OO0 #line:194
        O0000O0OOOOO00O00 .zeze =True #line:195
        O0000O0OOOOO00O00 .setGeometry (x ,y ,width ,height )#line:196
    def setFontSize (OOO00O0OOO00000O0 ,O0O000OO0O0O00000 ):#line:197
        OOO00OOO000O0O000 =QFont ()#line:198
        OOO00OOO000O0O000 .setPixelSize (O0O000OO0O0O00000 )#line:199
        OOO00O0OOO00000O0 .setFont (OOO00OOO000O0O000 )#line:200
    def setFontFitSize (O0000OOO00OO0OOOO ,O000OOOO000000O0O ):#line:201
        OO00OO00000OO0O00 =QFont ()#line:202
        OO00OO00000OO0O00 .setPointSize (O000OOOO000000O0O )#line:203
        O0000OOO00OO0OOOO .setFont (OO00OO00000OO0O00 )#line:204
    def setBackground (O0000OO00O0OOO0O0 ,O00OOOOOOO0OOO00O ):#line:205
        O0000OO00O0OOO0O0 .setStyleSheet (O0000OO00O0OOO0O0 .styleSheet ()+"border-image:url(RESOURCE/drawable/"+O00OOOOOOO0OOO00O +");")#line:206
    def setBackgroundColor (O0OO0OOO0OOOO00OO ,O00OO000O00OO0O0O ):#line:208
        O0OO0OOO0OOOO00OO .setStyleSheet (O0OO0OOO0OOOO00OO .styleSheet ()+"background-color:"+O00OO000O00OO0O0O +";")#line:209
    def setTextColor (OOO0000OOO0OO00OO ,OO0O00O0OO0O00OOO ):#line:211
        OOO0000OOO0OO00OO .setStyleSheet (OOO0000OOO0OO00OO .styleSheet ()+"color:"+OO0O00O0OO0O00OOO +";")#line:212
    def mouseReleaseEvent (OOO00OO00O00O00OO ,OO0O00000O0OO0000 ):#line:213
        OOO00OO00O00O00OO .released .emit (OO0O00000O0OO0000 )#line:214
    released =pyqtSignal (QMouseEvent )#line:215
    pressed =pyqtSignal (QEvent )#line:216
    def mousePressEvent (O00O0OOO0OOOOOOO0 ,O0000OO0O00OO0OOO ):#line:217
        O00O0OOO0OOOOOOO0 .pressed .emit (O0000OO0O00OO0OOO )#line:218
        if O0000OO0O00OO0OOO .buttons ()==Qt .LeftButton :#line:219
            O00O0OOO0OOOOOOO0 .clicked .emit (O0000OO0O00OO0OOO )#line:220
    moved =pyqtSignal (QMouseEvent )#line:221
    def mouseMoveEvent (OO00OO0OO0OO000O0 ,O00O00000OO000O00 ):#line:222
        OO00OO0OO0OO000O0 .moved .emit (O00O00000OO000O00 )#line:223
    doubleclicked =pyqtSignal (QMouseEvent )#line:224
    def mouseDoubleClickEvent (OOOOOO000OO00O00O ,OO0OOO00OOO0O00O0 ):#line:225
        if OO0OOO00OOO0O00O0 .buttons ()==Qt .LeftButton :#line:226
            OOOOOO000OO00O00O .doubleclicked .emit (OO0OOO00OOO0O00O0 )#line:227
    entered =pyqtSignal (QEnterEvent )#line:228
    def enterEvent (OOO00O00O0OOO0000 ,O0O00O0OO000OOO00 ):#line:229
        OOO00O00O0OOO0000 .entered .emit (O0O00O0OO000OOO00 )#line:230
    leaved =pyqtSignal (QEvent )#line:232
    def leaveEvent (OO0000OOOO00OOO00 ,O0O000OOO0O0OOOO0 ):#line:233
        OO0000OOOO00OOO00 .leaved .emit (O0O000OOO0O0OOOO0 )#line:234
    def setSize (OOO00OO00O00OOO00 ,O000O00OO0OOOO000 ):#line:237
        OOO00OO00O00OOO00 .setFixedSize (O000O00OO0OOOO000 )#line:238
    def refresh (OO0OO0OOO0O0O00OO ):#line:239
        if OO0OO0OOO0O0O00OO .zeze :#line:240
            OO0OO0OOO0O0O00OO .widget .resize (OO0OO0OOO0O0O00OO .widget .width ()+1 ,OO0OO0OOO0O0O00OO .widget .height ()+1 )#line:241
            OO0OO0OOO0O0O00OO .zeze =False #line:242
        else :#line:243
            OO0OO0OOO0O0O00OO .widget .resize (OO0OO0OOO0O0O00OO .widget .width ()-1 ,OO0OO0OOO0O0O00OO .widget .height ()-1 )#line:244
            OO0OO0OOO0O0O00OO .zeze =True #line:245
class PyQt5_QMovie (QMovie ):#line:247
    def __init__ (O000OO000O00OOOO0 ,OOO0OO0O0OOOOOOOO ):#line:248
        super ().__init__ ("RESOURCE/gif/"+OOO0OO0O0OOOOOOOO )#line:249
class PyQt5_QMediaPlayer ():#line:251
    def __init__ (O000000000O0O0OO0 ):#line:252
        pygame .mixer .init ()#line:253
        O000000000O0O0OO0 .music =pygame .mixer .music #line:254
    def prepare_audio (OOOOOOO00O0O0O0O0 ,O0O0OOO000OOOOOOO ):#line:255
        OOOOOOO00O0O0O0O0 .music .load ("RESOURCE/audio/"+O0O0OOO000OOOOOOO )#line:256
    def prepare_voice (O00000O0O00O00OOO ,O00000O0OOOO0000O ):#line:257
        O00000O0O00O00OOO .music .load ("RESOURCE/voice/"+O00000O0OOOO0000O )#line:258
    def play (OOO00O00000O00O0O ,loops =1 ,start =0.0 ):#line:259
        if loops ==0 :#line:260
            OOO00O00000O00O0O .music .play (-1 ,start )#line:261
        elif loops <0 :#line:262
            pass #line:263
        elif loops >0 :#line:264
            OOO00O00000O00O0O .music .play (loops -1 ,start )#line:265
    def stop (O000OOOO0O0OO0O00 ):#line:266
        O000OOOO0O0OO0O00 .music .stop ()#line:267
    def pause (O000O0OO00000O00O ):#line:268
        O000O0OO00000O00O .music .pause ()#line:269
    def setVolume (OOOOOOOOOOOO00OOO ,OOOOOOOOO00OO00O0 ):#line:270
        OOOOOOOOOOOO00OOO .music .set_volume (OOOOOOOOO00OO00O0 )#line:271
    def isPlaying (OOOOOOO0OO0000OO0 ):#line:272
        if OOOOOOO0OO0000OO0 .music .get_busy ()==1 :#line:273
            return True #line:274
        else :#line:275
            return False #line:276
class PyQt5_QCheckBox (QCheckBox ):#line:280
    def __init__ (O0000000OO00000OO ,OO000O00OOOO000O0 ,x =0 ,y =0 ,width =20 ,height =20 ):#line:281
        super ().__init__ (OO000O00OOOO000O0 )#line:282
        O0000000OO00000OO .setGeometry (x ,y ,width ,height )#line:283
        O0000000OO00000OO .isIndicator =True #line:284
        O0000000OO00000OO .image_name_normal =""#line:285
        O0000000OO00000OO .image_name_pressed =""#line:286
    def setIndicator (OO0O00O0O00OOO0OO ,O0O0000000O000OOO ):#line:288
        OO0O00O0O00OOO0OO .isIndicator =O0O0000000O000OOO #line:289
        OO0O00O0O00OOO0OO .setStyleSheet ("")#line:290
        if OO0O00O0O00OOO0OO .image_name_normal !="":#line:291
            OO0O00O0O00OOO0OO .setUncheckedBackground (OO0O00O0O00OOO0OO .image_name_normal )#line:292
        if OO0O00O0O00OOO0OO .image_name_pressed !="":#line:293
            OO0O00O0O00OOO0OO .setCheckedBackground (OO0O00O0O00OOO0OO .image_name_pressed )#line:294
    def setUncheckedBackground (O0OO0OOOO0OOOO0OO ,O0OO00OO000OOOO0O ):#line:296
        if O0OO0OOOO0OOOO0OO .isIndicator :#line:297
            O0OO0OOOO0OOOO0OO .setStyleSheet (O0OO0OOOO0OOOO0OO .styleSheet ()+"QCheckBox:unchecked{width:"+str (O0OO0OOOO0OOOO0OO .width ())+"px;height:"+str (O0OO0OOOO0OOOO0OO .height ())+"px;border-image:url(RESOURCE/drawable/"+O0OO00OO000OOOO0O +")}")#line:300
        else :#line:301
            O0OO0OOOO0OOOO0OO .setStyleSheet (O0OO0OOOO0OOOO0OO .styleSheet ()+"QCheckBox:indicator:unchecked{width:"+str (O0OO0OOOO0OOOO0OO .width ())+"px;height:"+str (O0OO0OOOO0OOOO0OO .height ())+"px;border-image:url(RESOURCE/drawable/"+O0OO00OO000OOOO0O +")}")#line:304
        O0OO0OOOO0OOOO0OO .image_name_normal =O0OO00OO000OOOO0O #line:305
    def setCheckedBackground (O000O0OOOO00OO0O0 ,OOO0O0O0OOOO0O000 ):#line:307
        if O000O0OOOO00OO0O0 .isIndicator :#line:308
            O000O0OOOO00OO0O0 .setStyleSheet (O000O0OOOO00OO0O0 .styleSheet ()+"QCheckBox:checked{width:"+str (O000O0OOOO00OO0O0 .width ())+"px;height:"+str (O000O0OOOO00OO0O0 .height ())+"px;border-image:url(RESOURCE/drawable/"+OOO0O0O0OOOO0O000 +")}")#line:311
        else :#line:312
            O000O0OOOO00OO0O0 .setStyleSheet (O000O0OOOO00OO0O0 .styleSheet ()+"QCheckBox:indicator:checked{width:"+str (O000O0OOOO00OO0O0 .width ())+"px;height:"+str (O000O0OOOO00OO0O0 .height ())+"px;border-image:url(RESOURCE/drawable/"+OOO0O0O0OOOO0O000 +")}")#line:315
        O000O0OOOO00OO0O0 .image_name_pressed =OOO0O0O0OOOO0O000 #line:316
class PyQt5_QRadioButton (QRadioButton ):#line:319
    def __init__ (O0OO0OO0OO0OO0OO0 ,OO000000O0000O000 ,x =0 ,y =0 ,width =20 ,height =20 ):#line:320
        super ().__init__ (OO000000O0000O000 )#line:321
        O0OO0OO0OO0OO0OO0 .setGeometry (x ,y ,width ,height )#line:322
        O0OO0OO0OO0OO0OO0 .isIndicator =True #line:323
        O0OO0OO0OO0OO0OO0 .image_name_normal =""#line:324
        O0OO0OO0OO0OO0OO0 .image_name_pressed =""#line:325
    def setFontSize (OOO0O0OOO00000O0O ,OO0000OO0OOO00O0O ):#line:327
        OOOOOO0OOO0OOO0O0 =QFont ()#line:328
        OOOOOO0OOO0OOO0O0 .setPixelSize (OO0000OO0OOO00O0O )#line:329
        OOO0O0OOO00000O0O .setFont (OOOOOO0OOO0OOO0O0 )#line:330
    def setTextColor (O000O0O0OO000OO00 ,OO00O000O0OOOO000 ):#line:332
        O000O0O0OO000OO00 .setStyleSheet (O000O0O0OO000OO00 .styleSheet ()+"color:"+OO00O000O0OOOO000 +";")#line:333
    def setIndicator (O0OO0OOOOOO00O00O ,O00OOO0O0OOOOO00O ):#line:335
        O0OO0OOOOOO00O00O .isIndicator =O00OOO0O0OOOOO00O #line:336
        O0OO0OOOOOO00O00O .setStyleSheet ("")#line:337
        if O0OO0OOOOOO00O00O .image_name_normal !="":#line:338
            O0OO0OOOOOO00O00O .setUncheckedBackground (O0OO0OOOOOO00O00O .image_name_normal )#line:339
        if O0OO0OOOOOO00O00O .image_name_pressed !="":#line:340
            O0OO0OOOOOO00O00O .setCheckedBackground (O0OO0OOOOOO00O00O .image_name_pressed )#line:341
    def setUncheckedBackground (O000OOOOOOO000O00 ,O0OO00OOOO00O0O0O ):#line:343
        if O000OOOOOOO000O00 .isIndicator :#line:344
            O000OOOOOOO000O00 .setStyleSheet (O000OOOOOOO000O00 .styleSheet ()+"QRadioButton:unchecked{width:"+str (O000OOOOOOO000O00 .width ())+"px;height:"+str (O000OOOOOOO000O00 .height ())+"px;border-image:url(RESOURCE/drawable/"+O0OO00OOOO00O0O0O +")}")#line:347
        else :#line:348
            O000OOOOOOO000O00 .setStyleSheet (O000OOOOOOO000O00 .styleSheet ()+"QRadioButton:indicator:unchecked{width:"+str (O000OOOOOOO000O00 .width ())+"px;height:"+str (O000OOOOOOO000O00 .height ())+"px;border-image:url(RESOURCE/drawable/"+O0OO00OOOO00O0O0O +")}")#line:351
        O000OOOOOOO000O00 .image_name_normal =O0OO00OOOO00O0O0O #line:352
    def setCheckedBackground (O0O00OO0O000OOO0O ,OO0OO0O0O0O00O0O0 ):#line:354
        if O0O00OO0O000OOO0O .isIndicator :#line:355
            O0O00OO0O000OOO0O .setStyleSheet (O0O00OO0O000OOO0O .styleSheet ()+"QRadioButton:checked{width:"+str (O0O00OO0O000OOO0O .width ())+"px;height:"+str (O0O00OO0O000OOO0O .height ())+"px;border-image:url(RESOURCE/drawable/"+OO0OO0O0O0O00O0O0 +")}")#line:358
        else :#line:359
            O0O00OO0O000OOO0O .setStyleSheet (O0O00OO0O000OOO0O .styleSheet ()+"QRadioButton:indicator:checked{width:"+str (O0O00OO0O000OOO0O .width ())+"px;height:"+str (O0O00OO0O000OOO0O .height ())+"px;border-image:url(RESOURCE/drawable/"+OO0OO0O0O0O00O0O0 +")}")#line:362
        O0O00OO0O000OOO0O .image_name_pressed =OO0OO0O0O0O00O0O0 #line:363
class PyQt5_QGroupBox (QGroupBox ):#line:366
    def __init__ (OOOOOOOO00O00O0O0 ,O0O0OO000000O0OO0 ,x =0 ,y =0 ,width =120 ,height =80 ):#line:367
        super ().__init__ (O0O0OO000000O0OO0 )#line:368
        OOOOOOOO00O00O0O0 .setGeometry (x ,y ,width ,height )#line:369
        OOOOOOOO00O00O0O0 .setObjectName ("groupbox")#line:370
    def setBackground (O0OO0OO0O00000000 ,O0000O000O0O0O00O ):#line:372
        O0OO0OO0O00000000 .setStyleSheet ("#groupbox{border-image:url(RESOURCE/drawable/"+O0000O000O0O0O00O +")}")#line:373
    def setBackgroundColor (OO0OOO0O0O000O000 ,OO0O0OOOO00OO0000 ):#line:375
        OO0OOO0O0O000O000 .setStyleSheet ("#groupbox{background-color:"+OO0O0OOOO00OO0000 +"}")#line:376
    def setBorderWidth (OO0OOOO00OOOO0OOO ,O0OOOOOOO0O000OO0 ):#line:378
        OO0OOOO00OOOO0OOO .setStyleSheet (OO0OOOO00OOOO0OOO .styleSheet ()+"border-width:"+str (O0OOOOOOO0O000OO0 )+"px;border-style:solid;")#line:379
def getQuestion (OOO0O0OOO0OOOOO0O ):#line:382
    try :#line:383
        OO0OOO0O0OO0O0000 =requests .post (ipStr ,data ={'id':OOO0O0OOO0OOOOO0O })#line:384
        OOOOO0O0OOOO00000 =json .loads (OO0OOO0O0OO0O0000 .text )#line:385
    except :#line:387
        OOOOO0O0OOOO00000 ={"id":1 ,"wenti":"由于网络问题未找到所需内容，请检查您的网络","daan":"0","jiexi":"  ","a":" ","b":" ","c":" ","d":" "}#line:388
        return OOOOO0O0OOOO00000 #line:389
    if OOOOO0O0OOOO00000 :#line:391
        if OOOOO0O0OOOO00000 ["state"]!=0 :#line:392
            return {"id":1 ,"wenti":info ["message"],"daan":"0","jiexi":"  ","a":" ","b":" ","c":" ","d":" "}#line:393
        else :#line:394
            return OOOOO0O0OOOO00000 ["data"]#line:395
def reductionRadioBtn (O0000000000OO000O ):#line:396
    for OOO0OO0000000OOO0 in range (len (O0000000000OO000O )):#line:397
        O0000000000OO000O [OOO0OO0000000OOO0 ].setCheckable (False )#line:398
        O0000000000OO000O [OOO0OO0000000OOO0 ].setCheckable (True )#line:399
class PyQt5_QSystemTrayIcon (QSystemTrayIcon ):#line:400
    def __init__ (O00O00OOO0O0000O0 ,parent =None ):#line:401
        super (PyQt5_QSystemTrayIcon ,O00O00OOO0O0000O0 ).__init__ (parent )#line:402
        O00O00OOO0O0000O0 .menu =QMenu ()#line:403
        O00O00OOO0O0000O0 .setContextMenu (O00O00OOO0O0000O0 .menu )#line:404
    def addMenu (O00O0OO0OOO0OO0O0 ,O0O0OOO00OO0OO000 ):#line:405
        O00O0OO0OOO0OO0O0 .menuAction =QAction (O0O0OOO00OO0OO000 ,O00O0OO0OOO0OO0O0 )#line:406
        O00O0OO0OOO0OO0O0 .menu .addAction (O00O0OO0OOO0OO0O0 .menuAction )#line:407
        return O00O0OO0OOO0OO0O0 .menuAction #line:408
    def _setIcon (O0O00OO00O0O0O0O0 ,O0O0O0O00OOOO0OO0 ):#line:409
        O0O00OO00O0O0O0O0 .setIcon (QIcon ("RESOURCE/drawable/"+O0O0O0O00OOOO0OO0 ))#line:410
class PyQt5_Animation (QPropertyAnimation ):#line:413
    animFinished =pyqtSignal ()#line:414
    def __init__ (OOOOO00O0O0OOO0OO ,QWidget =None ):#line:415
        super (PyQt5_Animation ,OOOOO00O0O0OOO0OO ).__init__ ()#line:416
        OOOOO00O0O0OOO0OO .setPropertyName (b"geometry")#line:417
        OOOOO00O0O0OOO0OO .setTargetObject (QWidget )#line:418
        OOOOO00O0O0OOO0OO .finished .connect (OOOOO00O0O0OOO0OO .aFinished )#line:419
        OOOOO00O0O0OOO0OO .widget =QWidget #line:420
        OOOOO00O0O0OOO0OO .valueChanged .connect (OOOOO00O0O0OOO0OO .up )#line:421
        OOOOO00O0O0OOO0OO .ze =True #line:422
    def up (OOO000OO0O0O00OO0 ):#line:423
        if OOO000OO0O0O00OO0 .ze :#line:424
            OOO000OO0O0O00OO0 .widget .resize (OOO000OO0O0O00OO0 .widget .width ()+1 ,OOO000OO0O0O00OO0 .widget .height ()+1 )#line:425
            OOO000OO0O0O00OO0 .ze =False #line:426
        else :#line:427
            OOO000OO0O0O00OO0 .widget .resize (OOO000OO0O0O00OO0 .widget .width ()-1 ,OOO000OO0O0O00OO0 .widget .height ()-1 )#line:428
            OOO000OO0O0O00OO0 .ze =True #line:429
    def setStartValues (OOO00OOOOO00O000O ,O0O0O0000OOOOO0OO ,O0OOO0000000OOOOO ,OO0OOO0000O0O00O0 ,OOOOOOO0OOO000OO0 ):#line:431
        OOO00OOOOO00O000O .setStartValue (QRect (O0O0O0000OOOOO0OO ,O0OOO0000000OOOOO ,OO0OOO0000O0O00O0 ,OOOOOOO0OOO000OO0 ))#line:432
    def setEndValues (OO0O000O0OO00O0O0 ,OOO0000OO0O0OOOO0 ,OO0OOOO0O0O000000 ,OO00O000OO0OO0O0O ,OOOO0O0O0OOO0000O ):#line:433
        OO0O000O0OO00O0O0 .setEndValue (QRect (OOO0000OO0O0OOOO0 ,OO0OOOO0O0O000000 ,OO00O000OO0OO0O0O ,OOOO0O0O0OOO0000O ))#line:434
    def setMode (O000OO0O00O0O0O00 ,OOO00000OO00OOOO0 ):#line:435
        O000OO0O00O0O0O00 .setEasingCurve (OOO00000OO00OOOO0 )#line:436
    def aFinished (O0O00O000O0O0OOOO ):#line:437
        O0O00O000O0O0OOOO .animFinished .emit ()#line:438
class Mode ():#line:440
    InOut =QEasingCurve .InOutBack #line:442
    OutIn =QEasingCurve .OutInBack #line:443
    InZero =QEasingCurve .InQuart #line:445
    OutZero =QEasingCurve .OutQuart #line:446
    InElastic =QEasingCurve .InElastic #line:448
    OutElastic =QEasingCurve .OutElastic #line:449
    InBounce =QEasingCurve .InBounce #line:451
    OutBounce =QEasingCurve .OutBounce #line:452
class PyQt5_FramelessBox (QDialog ):#line:454
    def __init__ (O0000OOOOOO0O0000 ):#line:455
        super ().__init__ ()#line:456
        O0000OOOOOO0O0000 .resize (340 ,340 )#line:457
        O0000OOOOOO0O0000 .setObjectName ("FramelessBox")#line:458
        O0000OOOOOO0O0000 .setWindowFlags (O0000OOOOOO0O0000 .windowFlags ()|Qt .FramelessWindowHint )#line:459
    def setWindowsTop (OOO0OO0OO00OOOOOO ,O0OOOOO0OO0000OOO ):#line:461
        if O0OOOOO0OO0000OOO :#line:462
            OOO0OO0OO00OOOOOO .setWindowFlags (OOO0OO0OO00OOOOOO .windowFlags ()|Qt .WindowStaysOnTopHint )#line:463
    def setResize (O00O0000O00OO0OO0 ,O0000OO0O0O0OO000 ,OO000O00OOOOOOOO0 ):#line:464
        O00O0000O00OO0OO0 .resize (O0000OO0O0O0OO000 ,OO000O00OOOOOOOO0 )#line:465
    def setWindowsTransparent (O0OO00OOO00000000 ,OO0000O00O0O0O000 ):#line:466
        if OO0000O00O0O0O000 :#line:467
            O0OO00OOO00000000 .setAttribute (Qt .WA_TranslucentBackground ,True )#line:468
def getDesktopWidth ():#line:470
    return QApplication .desktop ().width ()#line:471
def getDesktopHeight ():#line:473
    return QApplication .desktop ().height ()#line:474
def rock (OO0O0O00O00OOOO0O ,OOO0O000OO00O0O00 ):#line:476
    global angle ,direction #line:477
    OOO0OOO0OOO00000O =OOO0O000OO00O0O00 *math .sin (angle )#line:478
    O0000OOO00OOO00OO =OOO0O000OO00O0O00 *math .cos (angle )#line:479
    if direction ==1 :#line:480
        if angle <=1 :#line:481
            angle +=0.15 #line:482
        else :#line:483
            direction =-1 #line:484
    if direction ==-1 :#line:485
        if angle >=-1 :#line:486
            angle -=0.15 #line:487
        else :#line:488
            direction =1 #line:489
    OO0O0O00O00OOOO0O .finalX =OOO0OOO0OOO00000O #line:490
    OO0O0O00O00OOOO0O .finalY =O0000OOO00OOO00OO #line:491
def refresh (OOO00OOO00O0O0OO0 ,O00O0O0O0O000O00O ):#line:493
    for OOOOOO0000OO0OOOO in range (O00O0O0O0O000O00O ):#line:494
        OOO00OOO00O0O0OO0 .update ()#line:495
        time .sleep (0.01 )#line:496
def judge (OOOOO0OOO0000OO00 ,OOO0OO0OO00OOOOO0 ,O0OOO00OOO00O00O0 ,OO0O0OO000O000OO0 ,OOOO000000O00O0OO ,OO0OO0OOOO00OO00O ,O00OOOO000O0OOO0O ,OOOO00OOO0000000O ,O0OOOOOO000O00O0O ):#line:498
    global flg ,fff ,f ,border ,borderr #line:499
    if f ==1 :#line:500
        flg =1 #line:501
    for O0O00OO0O0OO00000 in range (len (OOOOO0OOO0000OO00 .listXY )):#line:502
        if OOOOO0OOO0000OO00 .namelist [O0O00OO0O0OO00000 ][1 ]==OO0O0OO000O000OO0 :#line:503
            border =O00OOOO000O0OOO0O #line:504
        elif OOOOO0OOO0000OO00 .namelist [O0O00OO0O0OO00000 ][1 ]==OOOO000000O00O0OO :#line:505
            border =OOOO00OOO0000000O #line:506
        elif OOOOO0OOO0000OO00 .namelist [O0O00OO0O0OO00000 ][1 ]==OO0OO0OOOO00OO00O :#line:507
            border =O0OOOOOO000O00O0O #line:508
        if OOO0OO0OO00OOOOO0 >=OOOOO0OOO0000OO00 .listXY [O0O00OO0O0OO00000 ][0 ]-5 and OOO0OO0OO00OOOOO0 <=OOOOO0OOO0000OO00 .listXY [O0O00OO0O0OO00000 ][0 ]+border +5 :#line:509
            if O0OOO00OOO00O00O0 >=OOOOO0OOO0000OO00 .listXY [O0O00OO0O0OO00000 ][1 ]and O0OOO00OOO00O00O0 <=OOOOO0OOO0000OO00 .listXY [O0O00OO0O0OO00000 ][1 ]+border :#line:510
                borderr =border #line:511
                OOOOO0OOO0000OO00 .index =O0O00OO0O0OO00000 #line:512
                print ("碰到了")#line:513
                flg =1 #line:514
    if OOOOO0OOO0000OO00 .distanceY >300 :#line:515
        fff =1 #line:516
        flg =1 #line:517
def lengths (O000O00O00OO00O00 ,OO0O000OO0OOOO000 ):#line:519
    O000O00O00OO00O00 .distanceY +=OO0O000OO0OOOO000 #line:520
    O000O00O00OO00O00 .distanceX +=(OO0O000OO0OOOO000 *O000O00O00OO00O00 .finalX )/O000O00O00OO00O00 .finalY #line:521
def YesOrNo (O0O00OO000O00O00O ):#line:523
    global flg ,fff ,f #line:524
    if flg !=1 and O0O00OO000O00O00O .distanceY >=0 and O0O00OO000O00O00O .distanceY <=300 :#line:525
        lengths (O0O00OO000O00O00O ,2 )#line:526
        O0O00OO000O00O00O .hook .move (290 +O0O00OO000O00O00O .finalX +O0O00OO000O00O00O .distanceX ,58 +O0O00OO000O00O00O .finalY +O0O00OO000O00O00O .distanceY )#line:527
        return 0 ,0 #line:528
    elif flg ==1 and O0O00OO000O00O00O .distanceY >=0 and fff !=1 :#line:529
        f =1 #line:530
        lengths (O0O00OO000O00O00O ,-2 )#line:531
        return 1 ,0 #line:532
    elif flg ==1 and fff ==1 and O0O00OO000O00O00O .distanceY >=0 :#line:533
        f =1 #line:534
        lengths (O0O00OO000O00O00O ,-2 )#line:535
        O0O00OO000O00O00O .hook .move (290 +O0O00OO000O00O00O .finalX +O0O00OO000O00O00O .distanceX ,58 +O0O00OO000O00O00O .finalY +O0O00OO000O00O00O .distanceY )#line:536
        return 0 ,0 #line:537
    else :#line:538
        if fff !=1 :#line:539
            O0O00OO000O00O00O .distanceY =0 #line:540
            flg ,f ,fff ,O0O00OO000O00O00O .isdo =0 ,0 ,0 ,0 #line:541
            return 1 ,1 #line:542
        O0O00OO000O00O00O .distanceY =0 #line:543
        flg ,f ,fff ,O0O00OO000O00O00O .isdo =0 ,0 ,0 ,0 #line:544
        try :#line:545
            O0O00OO000O00O00O .elderGif .stop ()#line:546
            return 0 ,0 #line:547
        except AttributeError :#line:548
            return 0 ,0 #line:549
def playAudio (O0OOO000O000OO00O ):#line:551
    OOOOOOOOOOOOOO000 =PyQt5_QMediaPlayer ()#line:552
    OOOOOOOOOOOOOO000 .prepare_audio (O0OOO000O000OO00O )#line:553
    OOOOOOOOOOOOOO000 .play ()#line:554
def change_img (O0OOO0O00O00O0OO0 ,OO0000OO0O0OO0O00 ,OO0OO000O0000OOOO ,OOO0OOOOO0O0000OO ):#line:556
    if O0OOO0O00O00O0OO0 .namelist [O0OOO0O00O00O0OO0 .index ][1 ]==OO0000OO0O0OO0O00 :#line:557
        O0OOO0O00O00O0OO0 .namelist [O0OOO0O00O00O0OO0 .index ][0 ].setBackground ("hook_gold.png")#line:558
    elif O0OOO0O00O00O0OO0 .namelist [O0OOO0O00O00O0OO0 .index ][1 ]==OO0OO000O0000OOOO :#line:559
        O0OOO0O00O00O0OO0 .namelist [O0OOO0O00O00O0OO0 .index ][0 ].setBackground ("hook_diamond.png")#line:560
    else :#line:561
        O0OOO0O00O00O0OO0 .namelist [O0OOO0O00O00O0OO0 .index ][0 ].setBackground ("hook_stone.png")#line:562
def getBorder ():#line:564
    return borderr #line:565

name="VipCode"