import pygame as pg
import random
import queue as Q
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QTextBrowser
from random import randint
import time

# from lab4 import bfs
class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        x = "test"
        #app1 = QtWidgets.QApplication(sys.argv)
        super().__init__()
        layout = QVBoxLayout()
        self.resize(600,400)
        self.setStyleSheet("background-color:rgb(181,126,220)")
        #self.label = QLabel("Another Window % d" % randint(0,100))
        #self.label_1 = QLabel("Another Window % d" % randint(0,100))
        # self.label = QtWidgets.QLabel(self.centralwidget)
        self.label = QLabel()
        self.label_1 = QLabel()
        self.label.setGeometry(QtCore.QRect(165, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Path: "+str(Game.Path))
        self.label_1.setGeometry(QtCore.QRect(165, 40, 191, 31))
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.label_1.setText("Cost: "+str(Game.Cost))
        self.label_2 = QLabel()
        self.label_2.setGeometry(QtCore.QRect(165, 40, 191, 31))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Time: "+Game.Time+" Ms")
        self.label_3 = QLabel()
        self.label_3.setGeometry(QtCore.QRect(165, 40, 191, 31))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Expanded nodes: "+Game.Time)

        self.button = QPushButton()
        self.button.setGeometry(QtCore.QRect(165, 40, 191, 31))
        self.button.setObjectName("button")
        self.button.setText("Quit")
        self.button.setStyleSheet("background-color:rgb(116,77,169)")
        self.button.pressed.connect(self.exit)
        # self.label_1.move(60,-20)
        # self.box = QTextBrowser(self)
        # self.box.setText(str(Game.Path))
        # self.textbox = QLineEdit(self)
        # self.textbox.move(20, 20)
        # self.textbox.resize(400,280)
        # self.textbox.setText(str(Game.Path))
        # self.box.setWordWrapMode(True)
        # self.box.setLineWrapMode(True)
        layout.addWidget(self.label)
        layout.addWidget(self.label_1)
        layout.addWidget(self.label_2)
        layout.addWidget(self.label_3)
        layout.addWidget(self.button)
        # layout.addWidget(self.box)
        self.setLayout(layout)
    def exit(self):
        sys.exit()

class Ui_OutWindow(object):
    def setupUi(self, outWindow):
        outWindow.setObjectName("outWindow")
        outWindow.resize(477, 231)
        self.centralwidget = QtWidgets.QWidget(outWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(165, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Please choose an algorithm:")

        outWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(outWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 477, 21))
        self.menubar.setObjectName("menubar")
        outWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(outWindow)
        self.statusbar.setObjectName("statusbar")
        outWindow.setStatusBar(self.statusbar)

        self.retranslateUi(outWindow)
        QtCore.QMetaObject.connectSlotsByName(outWindow)

    def retranslateUi(self, outWindow):
        _translate = QtCore.QCoreApplication.translate
        outWindow.setWindowTitle(_translate("OutPut", "OutPut"))
    

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(477, 231)
        MainWindow.setStyleSheet("background-color:rgb(181,126,220)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(165, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setText("Please choose an algorithm:")

        #Combo Box List
        comboList = ["BFS", "DFS", "UCS", "GBFS", "A*"]

        #Combo Box
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 70, 211, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(comboList)

        #Button
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(160, 132, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button.setFont(font)
        self.button.setObjectName("button")
        self.button.pressed.connect(self.find)
        self.button.setStyleSheet("background-color:rgb(116,77,169)")
        #self.button.setStyleSheet("background-color:purple")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 477, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setPlaceholderText(_translate("MainWindow", "Choose algorithm"))
        self.button.setText(_translate("MainWindow", "Start"))

    def find(self):

        # finding the content of current item in combo box
        contentCombo = self.comboBox.currentText()
        # showing content on the screen though label
        print(contentCombo)
        pg.init()
        screen = pg.display.set_mode((402, 402))
        pg.display.set_caption("maze Generator")
        game = Game(screen)
        Game.algorithm = contentCombo    
        game.main_loop()
        # game.output()
        self.w = None
        self.show_new_window()
    def show_new_window(self):
        if self.w is None:
            self.w = AnotherWindow()
        self.w.show()

class Root():
    def __init__(self, value, cost, parent = None):
    # def __init__(self, value, parent = None):
        self.value = value
        self.child = []
        self.parent = parent
        self.cost=cost

    def addChild(self, value):
        self.child.append(Root(value, 1,self))
        # self.child.append(Root(value,self))
        return self.child[-1]

    def children(self):
        return self.child

    def parents(self):
        return self.parent


class Game():
    Cost = 0
    Path = []
    Time = 0
    algorithm = "test_1"
    ismaze = False
    endPoint = 399
    rows, cols = 20, 20
    def __init__(self, screen):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.drawcan()
        self.generate_maze()
        self.ismaze = True

    def drawcan(self):
        self.start, self.end = None, None
        self.solveCan = None
        self.canvas = pg.Surface((402, 402))
        self.canvas.fill("#000000")
        for i in range(21):
            pg.draw.line(self.canvas, "#ffffff", (i * 20, 0), (i * 20, 400), 2)
            pg.draw.line(self.canvas, "#ffffff", (0, i*20), (400, i*20), 2)


    def drawloop(self):
        self.screen.fill("#200000")
        self.screen.blit(self.canvas, (0, 0))
        if self.solveCan is not None:
            self.screen.blit(self.solveCan, (0, 0))
        if self.start is not None:
            pg.draw.circle(self.screen, "#ffffff", ((self.start%self.cols) * 20 + 10, (self.start//self.cols) * 20 + 10)
                           , 5)
        if self.end is not None:
            pg.draw.rect(self.screen, "#ffffff", ((self.end % self.cols) * 20 + 5, (self.end // self.cols) * 20 + 5,
                                                 10, 10))
        pg.display.update()

    def main_loop(self):
        self.running = True
        while self.running:
            self.clock.tick(60)
            for eve in pg.event.get():
                if eve.type == pg.QUIT:
                    self.running = False
                    # pg.quit()
                    # self.output()
                if eve.type == pg.MOUSEBUTTONDOWN:
                    pos = self.cursor_grid(eve.pos[0], eve.pos[1])
                    if pos != -1:
                        if eve.button == 1:
                            if self.start == pos:
                                self.start = None
                            else:
                                self.start = pos
                            if self.start == self.end:
                                self.end = None
                        if eve.button == 3:
                            if self.end == pos:
                                self.end = None
                            else:
                                self.end = pos
                            if self.end == self.start:
                                self.start = None
                if eve.type == pg.KEYDOWN:
                    if eve.key == pg.K_SPACE:
                        self.drawcan()
                        self.generate_maze()
                        self.ismaze = True
                    if eve.key == pg.K_RETURN:
                        if self.start is None or self.end is None:
                            self.solve_maze()
                        else:
                            self.find_path(self.start, self.end)
            self.drawloop()

    def cursor_grid(self, mx, my):
        col, row = mx//20, my//20
        if col >= self.cols or row >= self.rows:
            return -1
        else:
            return row * self.cols + col

    def find_path(self, start, end):
        if not self.ismaze:
            return
        if Game.algorithm == "DFS":
            t1 = time.time()
            toStart = self.find_solution(self.maze, start, "0")
            toEnd = self.find_solution(self.maze, end, "0")
            t2 = time.time()
            Game.Time = str((t2-t1)*10000000)
            print(Game.algorithm)

        elif Game.algorithm == "BFS":
            t1 = time.time()
            toStart = self.bfs(self.maze, start, "0")
            toEnd = self.bfs(self.maze, end, "0")
            t2 = time.time()
            Game.Time = str((t2-t1)*1000)
            print(Game.algorithm)

        elif Game.algorithm == "UCS":
            # setup ='''
            # '''
            # code= '''
            # toStart,cost1 = self.ucs(self.maze, start, "0")
            # toEnd,cost2 = self.ucs(self.maze, end, "0")'''
            t1 = time.time()
            toStart,cost1 = self.ucs(self.maze, start, "0")
            toEnd,cost2 = self.ucs(self.maze, end, "0")
            t2 = time.time()
            Game.Time = str((t2-t1)*1000)
            cost=abs(cost1-cost2)
            Game.Cost = cost
            #Time = Timer(setup, code).timeit()
            print(Game.algorithm)

        elif Game.algorithm == "GBFS":
            print(Game.algorithm)
            t1 = time.time()
            toStart = self.GBFS(self.maze, start, "0")
            toEnd= self.GBFS(self.maze, end, "0")
            t2 = time.time()
            Game.Time = str((t2-t1)*1000)

        elif Game.algorithm == "A*":
            print(Game.algorithm)
            t1 = time.time()
            toStart = self.astar(self.maze, start, "0")
            toEnd= self.astar(self.maze, end, "0")
            t2 = time.time()
            Game.Time = str((t2-t1)*1000)

        if toStart is False or toEnd is False:
            return
        print("start= ",start)
        print("end= ",end)
        toStart = toStart.split("/")
        toEnd = toEnd.split("/")
        i = 0
        while (i < len(toStart) and i < len(toEnd)) and toStart[i] == toEnd[i]:
            i += 1
        path = []
        ii = len(toStart) - 1
        while ii >= i:
            path.append(toStart[ii])
            ii -= 1
        path.append(toStart[i-1])
        ii = i
        while ii < len(toEnd):
            path.append(toEnd[ii])
            ii += 1
        self.solveCan = pg.Surface((402, 402), pg.SRCALPHA)

        Game.Path = path
        for ind in path:
            # pg.time.delay(10)
            # pg.display.update()
            # pg.time.Clock().tick(300)
            pg.draw.circle(self.solveCan, "#ffffff", ((int(ind)%20) * 20 + 10, (int(ind)//20) * 20 + 10), 3)
        # for i in range(len(path)-1):
        #     s, e = int(path[i]), int(path[i+1])
        #     pg.draw.line(self.solveCan, "#ffffff", ((s%20) * 20 + 10, (s//20) * 20 + 10),
        #                  ((e%20) * 20 + 10, (e//20) * 20 + 10), 1)

    def surroundings(self, ind):
        res = []
        for i in (ind + 1, ind - 1):
            if i//20 == ind//20:
                res.append(i)
        for i in (ind + 20, ind - 20):
            if 0 <= i < 400:
                res.append(i)
        return res

    def generate_maze(self):
        self.maze = Root(0,1)
        # self.maze = Root(0)
        # (value, 1,self)
        self.build_tree(0, [], self.maze)

    def build_tree(self, parent, closed, parentTree):
        closed.append(parent)
        children = self.surroundings(parent)
        random.shuffle(children)
        for child in children:
            if child not in closed:
                row = parent // 20
                col = parent % 20
                if abs(parent - child) == 1:
                    pg.draw.line(self.canvas, "#000000", ((col + 1 * (child > parent)) * 20, row*20 + 2),
                                 ((col + 1 * (child>parent)) * 20, (row+1)*20-1), 2)
                else:
                    pg.draw.line(self.canvas, "#000000", (col * 20 + 2, (row + 1 * (child > parent)) * 20),
                                 ((col + 1) * 20 - 1, (row + 1 * (child > parent)) * 20), 2)
                self.drawloop()
                #pg.time.delay(10)
                childTree = parentTree.addChild(child)
                self.build_tree(child, closed, childTree)

    def find_solution(self, root, endpoint, path):
        if root.value == endpoint:
            return path
        children = root.children()
        for child in children:
            result = self.find_solution(child, endpoint, path + f"/{child.value}")
            if result is not False:
                return result
        return False
    def bfs(self,root,endpoint,path):
        v=[]
        q=[]
        c=[]
        v.append(root.value)
        q.append(root.value)
        children = root.children()
        c.append(children)
        # path + f"/{child.value}"
        while q:
            # if q[0] is path:
            #     return v
            ver=q.pop(0)
            # if ver == path:
            #     return v
            # if ver not in v:
            #     v.append(ver)
            if ver == endpoint:
                return path
            
            children=c.pop(0)

            for child in children:
                if child.value not in v:
                    path=path+ f"/{child.value}"
                    v.append(child.value)
                    q.append(child.value)
                    c.append(child.children())
    def ucs(self,root,endpoint,path):
        q=Q.PriorityQueue()
        v=[]
        c=[]
        q.put((0,[root.value]))
        v.append(root.value)
        children = root.children()
        c.append(children)
        while q:
            n=q.get()
            curr=n[1][len(n[1])-1]
            
            
            if endpoint in n[1]:
                # return n[1],n[0]
                return path,n[0]
                # print("path: "+str(n[1])+" cost: "+str(n[0]))
                # break
            for i in c:
                for r in i:
                    if r.value==curr:
                        path=path+ f"/{r.value}"
                        children=r.children()
                        break
            if endpoint in n[1]:
                print("cost= ",n[0]) 
                return path
            cost=n[0]
            # children=c.pop(0)
            for child in children:
                if child.value not in v:
                    v.append(child.value)
                    c.append(child.children())
                    temp=n[1][:]
                    temp.append(child.value)
                    q.put((cost+child.cost,temp))

    def GBFS(self,root, endpoint, path):
        priorityQueue = Q.PriorityQueue()
        h=self.heuristic(root,endpoint)
        priorityQueue.put((h, root.value))
        v=[]
        v.append(root.value)
        c=[]
        children = root.children()
        c.append(children)

        while priorityQueue.empty() == False:


            current = priorityQueue.get()[1]

            for i in c:
                for r in i:
                    if r.value==current:
                        path=path+ f"/{r.value}"
                        children=r.children()
                        break
            # path=path+ f"/{current}"
            # path.append(current)

            if current == endpoint:
                # print("goal reached")
                return path
                # break

            # priorityQueue = Q.PriorityQueue()

            for child in children:
                if child.value not in v:
                    v.append(child.value)
                    c.append(child.children())
                    priorityQueue.put((self.heuristic(child,endpoint), child.value))
                    
    def astar(self,root,endpoint, path):
        p_q,visited=Q.PriorityQueue(),[]
        p_q.put((self.heuristic(root,endpoint),0,root.value,[root.value]))
        visited.append(root.value)
        c=[]
        children = root.children()
        c.append(children)
        while not p_q.empty():
            (h,cost,vertex,p)=p_q.get()
            for i in c:
                for r in i:
                    if r.value==vertex:
                        path=path+ f"/{r.value}"
                        children=r.children()
                        break
            if vertex==endpoint:
                return path
                      
            for child in children:
                curr=cost+child.cost
                h=curr+self.heuristic(child,endpoint)
                if not (child.value in visited ):
                    visited.append(child.value)
                    c.append(child.children())
                    p_q.put((h,curr,child.value,p+[child.value]))

    def solve_maze(self):
        if not self.ismaze:
            return
        self.solveCan = pg.Surface((402, 402), pg.SRCALPHA)
        path = self.find_solution(self.maze, self.endPoint, "0")
        if path is False:
            return
        path = path.split("/")
        for ind in path:
            pg.draw.circle(self.solveCan, "#ffffff", ((int(ind)%20) * 20 + 10, (int(ind)//20) * 20 + 10), 3)
        for i in range(len(path)-1):
            s, e = int(path[i]), int(path[i+1])
            pg.draw.line(self.solveCan, "#ffffff", ((s%20) * 20 + 10, (s//20) * 20 + 10),
                         ((e%20) * 20 + 10, (e//20) * 20 + 10), 1)

    def output(self):
        appout = QtWidgets.QApplication(sys.argv)
        outputWindow = QtWidgets.QMainWindow()
        outui = Ui_OutWindow()
        outui.setupUi(outputWindow)
        outputWindow.show()
        sys.exit(appout.exec_())
        # return outputWindow

    def heuristic(self,node,endpoint):
        return abs(node.value-endpoint)




# pg.init()
# screen = pg.display.set_mode((402, 402))
# pg.display.set_caption("maze Generator")
# game = Game(screen)
# game.main_loop()
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())


# appout = QtWidgets.QApplication(sys.argv)
# outputWindow = QtWidgets.QMainWindow()
# outui = Ui_OutWindow()
# outui.setupUi(outputWindow)
# outputWindow.show()
# sys.exit(appout.exec_())