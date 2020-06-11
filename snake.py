# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pygame
import random
import time
from pygame.locals import *
snake_speed=15
windows_width=800
windows_height=600
cell_size=20
map_width=int(windows_width/cell_size)
map_height=int(windows_height/cell_size)
white=(255,255,255)
black = (0, 0, 0)
gray = (230, 230, 230)
dark_gray = (40, 40, 40)
DARKGreen = (0, 155, 0)
Green = (0, 255, 0)
Red = (255, 0, 0)
blue = (0, 0, 255)
dark_blue =(0,0, 139)
BG_COLOR = black
UP=1
DOWN=2
LEFT=3
RIGHT=4
HEAD=0
q=[blue]
sni=0
class obstacle():     #障碍类
    def __init__(self,screen):
        self.color=(255,193,203)             #障碍的颜色
        self.screen=screen             #障碍屏幕初始化
        self.cell_size=20    #障碍组成方块大小
        self.draw_obstacle1(screen)          #画障碍一
        self.draw_obstacle2(screen)#画障碍二
        self.draw_obstacle3(screen)#画障碍三
    def draw_obstacle1(self,screen):        #画障碍一   两条横杆
        for location in range(4,36):
            x=location*self.cell_size
            y=60
            w = pygame.Rect(x, y, self.cell_size, self.cell_size)
            pygame.draw.rect(screen, self.color, w)
        for location in range(4,36):
            x = location * self.cell_size
            y = 520
            w = pygame.Rect(x, y, self.cell_size, self.cell_size)
            pygame.draw.rect(screen, self.color, w)
        return True          #返回值TRUE 表明已经实现
    def draw_obstacle2(self,screen):        #画障碍二   

        for location in range(4,15):
            x = 280
            y = location * self.cell_size
            w = pygame.Rect(x, y, self.cell_size, self.cell_size)
            pygame.draw.rect(screen, self.color, w)
        for location in range(4,15):
            x = 460
            y = location * self.cell_size
            w = pygame.Rect(x, y, self.cell_size, self.cell_size)
            pygame.draw.rect(screen, self.color, w)
        return True          #返回值TRUE 表明已经实现
    def draw_obstacle3(self,screen):         #画障碍三  四块矩形
        for locationx in range(4,9):
            for locationy in range(4,7):
                x = locationx * self.cell_size
                y = locationy * self.cell_size
                w=pygame.Rect(x,y,self.cell_size,self.cell_size)
                pygame.draw.rect(screen,self.color,w)
        for locationx in range(4,9):
            for locationy in range(22, 26):
                x = locationx * self.cell_size
                y = locationy * self.cell_size
                w = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, self.color, w)
        for locationx in range(31,36):
            for locationy in range(4, 7):
                x = locationx * self.cell_size
                y = locationy * self.cell_size
                w = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, self.color, w)
        for locationx in range(31, 36):
            for locationy in range(22, 26):
                x = locationx * self.cell_size
                y = locationy * self.cell_size
                w = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, self.color, w)
        return True             #返回值TRUE 表明已经实现

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(834, 584)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(5)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_3.addWidget(self.spinBox)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(198, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.pushButton.clicked.connect(self.qi)
        self.pushButton_2.clicked.connect(self.tui)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "贪吃蛇"))
        self.label_2.setText(_translate("Form", "   难度(1-5)"))
        self.pushButton.setText(_translate("Form", "开始"))
        self.pushButton_2.setText(_translate("Form", "退出"))
    def qi(self):
        global snake_speed
        global ti
        global sni
        ti=0
        snake_speed=self.spinBox.value()*5
        sni=snake_speed
        pygame.mixer.init()
        pygame.mixer.music.load("Leandro Aconcha - The Entertainer.ogg")
        pygame.mixer.music.play()
        qidong()
    def tui(self):
        terminate()
        sys.exit()

def terminate():
    global ti
    pygame.quit()
    sys.exit()
def draw_grid(screen):
    for x in range(0, windows_width, cell_size):
        pygame.draw.line(screen, dark_gray, (x, 0), (x, windows_height))
    for y in range(0, windows_height, cell_size):
        pygame.draw.line(screen, dark_gray, (0, y), (windows_width, y))
def show_start_info(screen):
    while True:
        for event in pygame.event.get():
            if event.type==quit:
                terminate()
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    terminate()
                else:
                    return

def run(screen,speed):
    r1=0
    global ti
    oc=obstacle(screen)
    stx=random.randint(3,map_width-8)
    sty=random.randint(3,map_width-8)
    snake=[{'x':stx,'y':sty},
            {'x':stx-1,'y':sty},
            {'x':stx-2,'y':sty}]
    d=RIGHT
    bd=RIGHT
    food=get_random_location()
    pygame.mixer.music.load("Leandro Aconcha - The Entertainer.ogg")
    pygame.mixer.music.play()
    while True:
        for e in pygame.event.get():
            if e.type==QUIT:
                terminate()
            elif e.type==KEYDOWN:
                if (e.key==K_LEFT or e.key == K_a) and d!=RIGHT:
                    d=LEFT
                elif (e.key==K_RIGHT or e.key == K_d) and d!=LEFT:
                    d=RIGHT
                elif (e.key==K_UP or e.key==K_w) and d!=UP:
                    d=UP
                elif (e.key==K_DOWN or e.key==K_s) and d!=DOWN:
                    d=DOWN
                elif e.key==K_ESCAPE:
                    terminate()
        if (d==LEFT and bd==RIGHT)or(bd==LEFT and d==RIGHT)or(d==UP and bd==DOWN)or(bd==UP and d==DOWN):
            move(bd,snake)
        else:
            move(d,snake)
            bd=d
        r= snake_is_alive(snake)
        if not r:
            break
        se(snake,food)
        my_image = pygame.image.load(r'D:\SS\images\bgpicture5.png')
        screen.blit(my_image, (0, 0))
        #screen.fill(BG_COLOR)
        oc.draw_obstacle1(screen)
        oc.draw_obstacle2(screen)
        oc.draw_obstacle3(screen)
        draw_snake(screen,snake)
        draw_food(screen,food)
        draw_score(screen,len(snake)-3)
        pygame.display.update()
        speed.tick(snake_speed)
    pygame.mixer.music.load("gameover.wav")
    pygame.mixer.music.play()
    time.sleep(1)
def get_random_location():
    food={}
    food['x'] = random.randint(0, map_width - 1)
    food['y'] = random.randint(0, map_height - 1)
    while panduan(food)==0:
        food['x'] = random.randint(0, map_width - 1)
        food['y'] = random.randint(0, map_height - 1)
    return food
def move(direction ,snake):
    if direction == UP:
        newHead = {'x': snake[HEAD]['x'], 'y': snake[HEAD]['y'] - 1}
    elif direction == DOWN:
        newHead = {'x': snake[HEAD]['x'], 'y': snake[HEAD]['y'] + 1}
    elif direction == LEFT:
        newHead = {'x': snake[HEAD]['x'] - 1, 'y': snake[HEAD]['y']}
    elif direction == RIGHT:
        newHead = {'x': snake[HEAD]['x'] + 1, 'y': snake[HEAD]['y']}
    snake.insert(0, newHead)
def snake_is_alive(snake_coords):
    tag = True
    if snake_coords[HEAD]['x']<=-1 or snake_coords[HEAD]['x']>=map_width or snake_coords[HEAD]['y']<=-1 or snake_coords[HEAD]['y']>=map_height:
        return 0
    for snake_body in snake_coords[1:]:
        if snake_body['x'] == snake_coords[HEAD]['x'] and snake_body['y'] == snake_coords[HEAD]['y']:
            tag = False
    if snake_coords[HEAD]['y']==3:
        if snake_coords[HEAD]['x']>=4 and snake_coords[HEAD]['x']<36:
            tag=False
    if snake_coords[HEAD]['y']==26:
        if snake_coords[HEAD]['x']>=4 and snake_coords[HEAD]['x']<36:
            tag=False
    if snake_coords[HEAD]['x']==14:
        if snake_coords[HEAD]['y']>=4 and snake_coords[HEAD]['y']<15:
            tag=False
    if snake_coords[HEAD]['x']==23:
        if snake_coords[HEAD]['y']>=4 and snake_coords[HEAD]['y']<15:
            tag=False
    part=snake_coords[HEAD]
    if part['x']>=4 and part['x']<9:
        if part['y']>=4 and part['y']<7:
            tag=False
    if part['x']>=4 and part['x']<9:
        if part['y']>=22 and part['y']<26:
            tag=False
    if part['x']>=31 and part['x']<36:
        if part['y']>=4 and part['y']<7:
            tag=False
    if part['x']>=31 and part['x']<36:
        if part['y']>=22 and part['y']<26:
            tag=False
    return tag
def panduan(snake_coords):
    tag=True
    if snake_coords['y']==3:
        if snake_coords['x']>=4 and snake_coords['x']<36:
            tag=False
    if snake_coords['y']==26:
        if snake_coords['x']>=4 and snake_coords['x']<36:
            tag=False
    if snake_coords['x']==14:
        if snake_coords['y']>=4 and snake_coords['y']<15:
            tag=False
    if snake_coords['x']==23:
        if snake_coords['y']>=4 and snake_coords['y']<15:
            tag=False
    part=snake_coords
    if part['x']>=4 and part['x']<9:
        if part['y']>=4 and part['y']<7:
            tag=False
    if part['x']>=4 and part['x']<9:
        if part['y']>=22 and part['y']<26:
            tag=False
    if part['x']>=31 and part['x']<36:
        if part['y']>=4 and part['y']<7:
            tag=False
    if part['x']>=31 and part['x']<36:
        if part['y']>=22 and part['y']<26:
            tag=False
    return tag
def se(snake,food):
    if snake[HEAD]['x']==food['x'] and snake[HEAD]['y']==food['y']:
        goal_sound = pygame.mixer.Sound("goal_1.wav")
        goal_sound.play()
        food['x'] = random.randint(0, map_width - 1)
        food['y'] = random.randint(0, map_height - 1)
        while panduan(food)==0:
            food['x'] = random.randint(0, map_width - 1)
            food['y'] = random.randint(0, map_height - 1)
    else:
        del snake[-1]

def draw_snake(screen,snake):
    p=1
    for c in snake:
        x=c['x']* cell_size
        y=c['y']* cell_size
        if len(q)>p:
            now=q[p]
        else:
            now=(random.randint(max(0,q[-1][0]-35),min(255,q[-1][0]+35)),random.randint(max(0,q[-1][1]-35),min(255,q[-1][1]+35)),random.randint(max(0,q[-1][2]-35),min(255,q[-1][2]+35)))
            q.append(now)
        w=pygame.Rect(x,y,cell_size,cell_size)
        pygame.draw.rect(screen,now,w)
        ww=pygame.Rect((x+4),(y+4),cell_size-8,cell_size-8)
        pygame.draw.rect(screen,now,ww)
        p+=1
def draw_food(screen,food):
    x=food['x']*cell_size
    y=food['y']*cell_size
    w=pygame.Rect(x,y,cell_size,cell_size)
    pygame.draw.rect(screen,Red,w)
#
def draw_score(screen,score):
    global snake_speed,sni
    snake_speed=sni+score/5
    font=pygame.font.Font(r'C:\Windows\Fonts\simsunb.ttf',30)
    ss=font.render(u'score:%s' %score,True,Green)
    sr=ss.get_rect()
    sr.topleft=(windows_width-120,10)
    screen.blit(ss,sr)
def qidong(): 
    pygame.init()
    speed=pygame.time.Clock()
    screen=pygame.display.set_mode((windows_width,windows_height))
    my_image = pygame.image.load(r'D:\SS\images\bgpicture5.png')
    screen.blit(my_image, (0, 0))
    pygame.display.update()
    pygame.display.set_caption("贪吃蛇")
    show_start_info(screen)
    while True:
        q=[]
        run(screen,speed)
        show_gameover(screen)
        if ti:
            return 
def show_gameover(screen):
      while True: 
        for event in pygame.event.get():  
            if event.type == QUIT:
                terminate()    
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_q: 
                    terminate() 
                else:
                    return 
if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    form =QtWidgets.QWidget()
    w = Ui_Form()                  
    w.setupUi(form)
    form.show()
    sys.exit(app.exec_())