
import lab4
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
#visited=[]
# from pygame.locals import *
# PyQt5-Qt5, PyQt5-sip, pyqt5
# C:\Users\Nadda\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts
graph = {'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
'Zerind': {'Oradea': 71, 'Arad': 75},
'Timisoara': {'Arad': 118, 'Lugoj': 111},
'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimniciu Vilcea': 80},
'Oradea': {'Zerind': 71, 'Sibiu': 151},
'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Rimniciu Vilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Mehadia': {'Lugoj': 70, 'Dobreta': 75},
    'Craiova': {'Dobreta': 120, 'Rimniciu Vilcea': 146, 'Pitesti': 138},
    'Pitesti': {'Rimniciu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni':{'Vaslui':142,'Hirsova':98,'Bucharest':85},
         'Vaslui':{'Lasi':92,'Urziceni':142},
         'Lasi':{'Neamt':87,'Vaslui':92},
         'Neamt':{'Lasi':87},
         'Hirsova':{'Eforie':86,'Urziceni':98},
         'Eforie':{'Hirsova':86}}
GRAPH = {'Arad':[['Zerind',374],['Timisoara',329],['Sibiu',253]],
         'Zerind':[['Oradea',380],['Arad',366]],
         'Oradea':[['Sibiu',253]],
         'Sibiu':[['Rimniciu Vilcea',193],['Fagaras',178],['Arad',366]],
         'Fagaras':[['Sibiu',253],['Bucharest',0]],
         'Rimniciu Vilcea':[['Pitesti',98],['Craiova',160],['Sibiu',253]],
         'Timisoara':[['Lugoj',244],['Arad',366]], 
         'Lugoj':[['Mehadia',241]],
         'Mehadia':[['Lugoj',244],['Dorbeta',242]],
         'Dobreta':[['Mehadia',241],['Craiova',160]],
         'Pitesti':[['Craiova',160],['Bucharest',0]],
         'Craiova':[['Pitesti',98],['Dobreta',242],['Rimniciu Vilcea',193]],
         'Bucharest':[['Giurgiu',77],['Urziceni',80],['Fagaras',178],['Pitesti',98]],
         'Giurgiu': [['Bucharest',0]],
         'Urziceni':[['Vaslui',199],['Hirsova',151],['Bucharest',0]],
         'Vaslui':[['Lasi',226],['Urziceni',80]],
         'Lasi':[['Neamt',234],['Vaslui',199]],
         'Neamt':[['Lasi',226]],
         'Hirsova':[['Eforie',161],['Urziceni',80]],
         'Eforie':[['Hirsova',151]]
}
straight_line ={
            'Arad': 366,'Zerind': 374,'Oradea': 380,'Sibiu':  253,'Fagaras':176,'Rimniciu Vilcea': 193,
            'Timisoara': 329,'Lugoj': 244,'Mehadia': 241,'Dobreta': 242,'Pitesti':100,'Craiova':160,
            'Bucharest':0,'Giurgiu':77,'Urziceni': 80,'Vaslui':199,'Lasi':226,'Neamt':234,'Hirsova':151,
            'Eforie':161
                        }

visited=[]
# print('BFS result: ')
# print(lab4.bfs(graph, 'Arad', 'Bucharest'))
# print('DFS result: ')
# print(lab4.dfs(graph, 'Arad', 'Bucharest'))
# # print('DFS2 result: ')
# # print(lab4.dfs2(visited, graph, 'Arad', 'Bucharest'))
# print('Uniform Cost Search result: ')
# print(lab4.ucs(graph, 'Arad', 'Bucharest'))
# # print('Uniform Cost Search result: ')
# # print(lab4.ucs2(graph, 'Arad', 'Dobreta'))
# print('Greedy Best First Search result: ')
# print(lab4.GBFS(GRAPH, 'Arad', 'Bucharest'))
# # print('A Star Search result: ')
# # print(lab4.Astar(graph,straight_line, 'Zerind', 'Bucharest'))
# print('A Star Search result: ')
# print(lab4.astar(graph,straight_line, 'Arad', 'Bucharest'))

 
# initiate pygame and give permission
# to use pygame's functionality.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 451)
        MainWindow.setStyleSheet("background-color: gray;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Radio Buttons
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(40, 90, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        #self.radioButton.clicked.connect(self.find)

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 110, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
       # self.radioButton_2.clicked.connect(self.find)

        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 130, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
       # self.radioButton_3.clicked.connect(self.find)

        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(40, 150, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        #self.radioButton_4.clicked.connect(self.find)

        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(40, 170, 82, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        #self.radioButton_5.clicked.connect(self.find)
        
        #Combo Box List
        comboList = ["Arad", "Zerind", "Timisoara", "Sibiu", "Oradea", "Lugoj", "Rimnicu Vilcea", "Mehadia", "Craiova", "Pitesti", "Fagaras", "Dobreta", "Bucharest", "Giurgiu", "Urziceni", "Vaslui", "Lasi", "Neamt", "Hirsova", "Eforie"]

        #Combo Boxes
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(320, 60, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(comboList)

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(530, 60, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(comboList)

        #Start Button
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(280, 340, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.startButton.pressed.connect(self.find)
        #labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 35, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 40, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(530, 40, 47, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        #Line
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(263, 30, 20, 251))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        #Menu Bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        #Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "BFS"))
        self.radioButton_2.setText(_translate("MainWindow", "DFS"))
        self.radioButton_3.setText(_translate("MainWindow", "UCS"))
        self.radioButton_4.setText(_translate("MainWindow", "GBFS"))
        self.radioButton_5.setText(_translate("MainWindow", "A*"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "Please select an algorithm:"))
        self.label_2.setText(_translate("MainWindow", "Start"))
        self.label_3.setText(_translate("MainWindow", "Goal"))
    
    def find(self):
        contentRadio = ""
        

        # finding the content of current item in combo box
        contentCombo_1 = self.comboBox.currentText()
        contentCombo_2 = self.comboBox_2.currentText()

        if self.radioButton.isChecked():
            contentRadio = self.radioButton.text()
            print('BFS result: ')
            path=lab4.bfs(graph, contentCombo_1, contentCombo_2)
            print(path)

        elif self.radioButton_2.isChecked():
            contentRadio = self.radioButton_2.text()
            print('DFS result: ')
            path=lab4.dfs(graph, contentCombo_1, contentCombo_2)
            print(path)
            

        elif self.radioButton_3.isChecked():
            contentRadio = self.radioButton_3.text()
            print('Uniform Cost Search result: ')
            path,cost=lab4.ucs(graph, contentCombo_1, contentCombo_2)
            print(path,cost)

        elif self.radioButton_4.isChecked():
            contentRadio = self.radioButton_4.text()
            print('Greedy Best First Search result: ')
            path=lab4.GBFS(GRAPH, contentCombo_1, contentCombo_2)
            print(path)

        elif self.radioButton_5.isChecked():
            contentRadio = self.radioButton_5.text()
            print('A Star Search result: ')
            cost,path=lab4.astar(graph,straight_line, contentCombo_1, contentCombo_2)
            print(path,cost)

        # showing content on the screen though label
        print(contentCombo_1)
        print(contentCombo_2)
        print(contentRadio)
        pygame.init()
  
        # Initializing surface
        surface = pygame.display.set_mode((1250,650))
        # Initialing Color
        color = (255,0,0)
        font = pygame.font.SysFont(None, 30)

        # arad
        pygame.draw.circle(surface, color, (150,150), 15)
        img = font.render("Arad", True, color)
        surface.blit(img, (95, 162))
        img = font.render("75", True, color)
        surface.blit(img, (200, 140))
        img = font.render("366", True, color)
        surface.blit(img, (133, 115))
        pygame.draw.line(surface,color,(150,150),(250,100),5)

        # zerind
        pygame.draw.circle(surface, color, (250,100), 15)
        img = font.render("Zerind", True, color)
        surface.blit(img, (227, 120))
        img = font.render("71", True, color)
        surface.blit(img, (270, 85))
        img = font.render("374", True, color)
        surface.blit(img, (230, 60))
        pygame.draw.line(surface,color,(250,100),(300,50),5)

        # oradea
        pygame.draw.circle(surface, color, (300,50), 15)
        img = font.render("Oradea", True, color)
        surface.blit(img, (322, 43))
        img = font.render("151", True, color)
        surface.blit(img, (330, 140))
        img = font.render("380", True, color)
        surface.blit(img, (282, 12))
        pygame.draw.line(surface,color,(300,50),(350,250),5)
        # pygame.display.flip()

        # sibiu
        pygame.draw.circle(surface, color, (350,250), 15)
        img = font.render("Sibiu", True, color)
        surface.blit(img, (365, 220))
        img = font.render("140", True, color)
        surface.blit(img, (235, 215))
        img = font.render("253", True, color)
        surface.blit(img, (350, 198))
        img = font.render("99", True, color)
        surface.blit(img, (410, 255))
        img = font.render("80", True, color)
        surface.blit(img, (350, 300))
        pygame.draw.line(surface,color,(350,250),(150,150),5)
        pygame.draw.line(surface,color,(350,250),(500,250),5)
        pygame.draw.line(surface,color,(350,250),(400,350),5)

        # fagaras
        pygame.draw.circle(surface, color, (500,250), 15)
        img = font.render("Fagaras", True, color)
        surface.blit(img, (475, 210))
        img = font.render("176", True, color)
        surface.blit(img, (480, 187))
        img = font.render("211", True, color)
        surface.blit(img, (620, 300))
        pygame.draw.line(surface,color,(500,250),(750,400),5)


        # rimnicu
        pygame.draw.circle(surface, color, (400,350), 15)
        img = font.render("Rimnicu Vilcea", True, color)
        surface.blit(img, (400, 310))
        img = font.render("193", True, color)
        surface.blit(img, (342, 343))
        pygame.draw.line(surface,color,(400,350),(550,400),5)
        pygame.draw.line(surface,color,(400,350),(420,600),5)

        # pitesti
        pygame.draw.circle(surface, color, (550,400), 15)
        img = font.render("Pitesti", True, color)
        surface.blit(img, (552, 368))
        img = font.render("100", True, color)
        surface.blit(img, (497, 395))
        img = font.render("97", True, color)
        surface.blit(img, (475, 352))
        img = font.render("101", True, color)
        surface.blit(img, (630, 410))
        pygame.draw.line(surface,color,(550,400),(750,400),5)
        pygame.draw.line(surface,color,(550,400),(420,600),5)

        # bucharest
        pygame.draw.circle(surface, color, (750,400), 15)
        img = font.render("Bucharest", True, color)
        surface.blit(img, (760, 420))
        img = font.render("90", True, color)
        surface.blit(img, (723, 450))
        img = font.render("0", True, color)
        surface.blit(img, (745, 360))
        img = font.render("85", True, color)
        surface.blit(img, (835, 345))
        pygame.draw.line(surface,color,(750,400),(950,350),5)
        pygame.draw.line(surface,color,(750,400),(675,500),5)

        # criova
        pygame.draw.circle(surface, color, (420,600), 15)
        img = font.render("Craiova", True, color)
        surface.blit(img, (400, 620))
        img = font.render("160", True, color)
        surface.blit(img, (440, 592))
        img = font.render("120", True, color)
        surface.blit(img, (335, 570))
        img = font.render("146", True, color)
        surface.blit(img, (420, 460))
        img = font.render("138", True, color)
        surface.blit(img, (488, 500))
        pygame.draw.line(surface,color,(420,600),(280,590),5)

        # giurgiu
        pygame.draw.circle(surface, color, (675,500), 15)
        img = font.render("Giurgiu", True, color)
        surface.blit(img, (640, 520))
        img = font.render("77", True, color)
        surface.blit(img, (659, 540))

        # dobreta
        pygame.draw.circle(surface, color, (280,590), 15)
        img = font.render("Dobreta", True, color)
        surface.blit(img, (210, 610))
        img = font.render("242", True, color)
        surface.blit(img, (225, 582))
        img = font.render("75", True, color)
        surface.blit(img, (250, 530))
        pygame.draw.line(surface,color,(280,590),(280,490),5)

        # mehadia
        pygame.draw.circle(surface, color, (280,490), 15)
        img = font.render("Mehadia", True, color)
        surface.blit(img, (178, 488))
        img = font.render("241", True, color)
        surface.blit(img, (300, 480))
        img = font.render("70", True, color)
        surface.blit(img, (250, 430))
        pygame.draw.line(surface,color,(280,490),(280,390),5)

        # lugoj
        pygame.draw.circle(surface, color, (280,390), 15)
        img = font.render("Lugoj", True, color)
        surface.blit(img, (202, 388))
        img = font.render("244", True, color)
        surface.blit(img, (298, 380))
        img = font.render("111", True, color)
        surface.blit(img, (200, 352))
        pygame.draw.line(surface,color,(280,390),(180,290),5)

        # timisoara
        pygame.draw.circle(surface, color, (180,290), 15)
        img = font.render("Timisoara", True, color)
        surface.blit(img, (61, 288))
        img = font.render("329", True, color)
        surface.blit(img, (205, 280))
        img = font.render("118", True, color)
        surface.blit(img, (120, 225))
        pygame.draw.line(surface,color,(180,290),(150,150),5)

        # urziceni
        pygame.draw.circle(surface, color, (950,350), 15)
        img = font.render("Urziceni", True, color)
        surface.blit(img, (900, 370))
        img = font.render("80", True, color)
        surface.blit(img, (930, 315))
        img = font.render("98", True, color)
        surface.blit(img, (1020, 325))
        img = font.render("142", True, color)
        surface.blit(img, (945, 250))
        pygame.draw.line(surface,color,(950,350),(1100,350),5)
        pygame.draw.line(surface,color,(950,350),(1025,200),5)

        # hirsova
        pygame.draw.circle(surface, color, (1100,350), 15)
        img = font.render("Hirsova", True, color)
        surface.blit(img, (1125, 350))
        img = font.render("86", True, color)
        surface.blit(img, (1080, 425))
        img = font.render("151", True, color)
        surface.blit(img, (1120, 330))
        pygame.draw.line(surface,color,(1100,350),(1150,500),5)

        # eforie
        pygame.draw.circle(surface, color, (1150,500), 15)
        img = font.render("Eforie", True, color)
        surface.blit(img, (1130, 520))
        img = font.render("161", True, color)
        surface.blit(img, (1140, 540))

        # vaslui
        pygame.draw.circle(surface, color, (1025,200), 15)
        img = font.render("Vaslui", True, color)
        surface.blit(img, (1050, 190))
        img = font.render("199", True, color)
        surface.blit(img, (965, 190))
        img = font.render("92", True, color)
        surface.blit(img, (995, 135))
        pygame.draw.line(surface,color,(1025,200),(950,100),5)

        # iasi
        pygame.draw.circle(surface, color, (950,100), 15)
        img = font.render("Iasi", True, color)
        surface.blit(img, (975, 90))
        img = font.render("226", True, color)
        surface.blit(img, (965, 65))
        img = font.render("87", True, color)
        surface.blit(img, (895, 60))
        pygame.draw.line(surface,color,(950,100),(850,70),5)

        # neamt
        pygame.draw.circle(surface, color, (850,70), 15)
        img = font.render("Neamt", True, color)
        surface.blit(img, (800, 85))
        img = font.render("234", True, color)
        surface.blit(img, (795, 60))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
