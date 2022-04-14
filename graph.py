
import lab4
from PyQt5 import QtCore, QtGui, QtWidgets
import pygame
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
print('BFS result: ')
print(lab4.bfs(graph, 'Zerind', 'Dobreta'))
print('DFS result: ')
print(lab4.dfs(graph, 'Zerind', 'Dobreta'))
print('DFS2 result: ')
print(lab4.dfs2(visited,graph, 'Zerind', 'Dobreta'))
print('Uniform Cost Search result: ')
print(lab4.ucs(graph, 'Arad', 'Dobreta'))
# print('Uniform Cost Search result: ')
# print(lab4.ucs2(graph, 'Arad', 'Dobreta'))
print('Greedy Best First Search result: ')
print(lab4.GBFS(GRAPH, 'Zerind', 'Bucharest'))
# print('A Star Search result: ')
# print(lab4.Astar(graph,straight_line, 'Zerind', 'Bucharest'))
print('A Star Search result: ')
print(lab4.astar(graph,straight_line, 'Arad', 'Bucharest'))

 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
  
# Initializing surface
surface = pygame.display.set_mode((1250,650))
# Initialing Color
color = (255,0,0)
font = pygame.font.SysFont(None, 30)

# arad
pygame.draw.circle(surface, color, (150,150), 15)
img = font.render("Arad", True, color)
surface.blit(img, (100, 167))
img = font.render("75", True, color)
surface.blit(img, (200, 140))
img = font.render("366", True, color)
surface.blit(img, (133, 115))
pygame.draw.line(surface,color,(150,150),(250,100),5)

# zerind
pygame.draw.circle(surface, color, (250,100), 15)
img = font.render("Zerind", True, color)
surface.blit(img, (225, 120))
img = font.render("71", True, color)
surface.blit(img, (270, 85))
img = font.render("374", True, color)
surface.blit(img, (230, 60))
pygame.draw.line(surface,color,(250,100),(300,50),5)

# oradea
pygame.draw.circle(surface, color, (300,50), 15)
img = font.render("Oradea", True, color)
surface.blit(img, (322, 45))
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
surface.blit(img, (550, 370))
pygame.draw.line(surface,color,(550,400),(750,400),5)
pygame.draw.line(surface,color,(550,400),(420,600),5)

# bucharest
pygame.draw.circle(surface, color, (750,400), 15)
img = font.render("Bucharest", True, color)
surface.blit(img, (760, 420))
pygame.draw.line(surface,color,(750,400),(950,350),5)
pygame.draw.line(surface,color,(750,400),(675,500),5)

# criova
pygame.draw.circle(surface, color, (420,600), 15)
img = font.render("Craiova", True, color)
surface.blit(img, (410, 620))
pygame.draw.line(surface,color,(420,600),(280,590),5)

# giurgiu
pygame.draw.circle(surface, color, (675,500), 15)
img = font.render("Giurgiu", True, color)
surface.blit(img, (675, 520))

# dobreta
pygame.draw.circle(surface, color, (280,590), 15)
img = font.render("Dobreta", True, color)
surface.blit(img, (210, 610))
pygame.draw.line(surface,color,(280,590),(280,490),5)

# mehadia
pygame.draw.circle(surface, color, (280,490), 15)
img = font.render("Mehadia", True, color)
surface.blit(img, (180, 490))
pygame.draw.line(surface,color,(280,490),(280,390),5)

# lugoj
pygame.draw.circle(surface, color, (280,390), 15)
img = font.render("Lugoj", True, color)
surface.blit(img, (200, 390))
pygame.draw.line(surface,color,(280,390),(180,290),5)

# timisoara
pygame.draw.circle(surface, color, (180,290), 15)
img = font.render("Timisoara", True, color)
surface.blit(img, (60, 290))
pygame.draw.line(surface,color,(180,290),(150,150),5)

# urziceni
pygame.draw.circle(surface, color, (950,350), 15)
img = font.render("Urziceni", True, color)
surface.blit(img, (900, 370))
pygame.draw.line(surface,color,(950,350),(1100,350),5)
pygame.draw.line(surface,color,(950,350),(1025,200),5)

# hirsova
pygame.draw.circle(surface, color, (1100,350), 15)
img = font.render("Hirsova", True, color)
surface.blit(img, (1125, 350))
pygame.draw.line(surface,color,(1100,350),(1150,500),5)

# eforie
pygame.draw.circle(surface, color, (1150,500), 15)
img = font.render("Eforie", True, color)
surface.blit(img, (1150, 520))

# vaslui
pygame.draw.circle(surface, color, (1025,200), 15)
img = font.render("Vaslui", True, color)
surface.blit(img, (1050, 190))
pygame.draw.line(surface,color,(1025,200),(950,100),5)

# iasi
pygame.draw.circle(surface, color, (950,100), 15)
img = font.render("Iasi", True, color)
surface.blit(img, (975, 90))
pygame.draw.line(surface,color,(950,100),(850,70),5)

# neamt
pygame.draw.circle(surface, color, (850,70), 15)
img = font.render("Neamt", True, color)
surface.blit(img, (800, 85))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()