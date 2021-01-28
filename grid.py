import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.transforms as trans
import numpy as np
import random


class Grid:

    def __init__(self, board_type,size):
        self.board_type = board_type  # 0 is triangle, 1 is diamond.
        self.size = size  # number of rows and columns of data structure of board.
        self.nodes = {}   # tuple with the position
        self.edges = [] #List wit tuples, from node to node
        self.positions = {} #Dict with the positions so the graph looks symetric
        self.G = nx.Graph()







        # draw with break between frames given in "play"
    def drawGrid(self):
        self.positions = self.nodePosition()
        self.G.add_nodes_from(self.nodes)
        self.G.add_edges_from(self.edges)
        self.randomStart()
        print(self.nodes)
        print(len(self.nodes))
        self.colorChange()


        print(nx.info(self.G))
        nx.draw_networkx(self.G,pos=self.positions, node_color=self.colorChange())

        plt.show()

    def nodePosition(self):
        positions = {}
        if self.board_type == 0:
            for (i,j) in self.nodes:
                posX=-i + 2*j
                posY= -i
                positions[(i,j)]=(posX, posY)

        elif self.board_type == 1:
            for (i,j) in self.nodes:
                posX = -i + j
                posY = -i - j
                positions[(i, j)] = (posX, posY)

        return positions
        print("positions=",self.positions)


    def createNodes(self):
        if self.board_type == 0:
            for i in range(self.size):
                for j in range(i+1):
                    self.nodes[(i,j)] = "blue"

        elif self.board_type == 1:
            for i in range(self.size):
                for j in range(self.size):
                    self.nodes[(i,j)] = "blue"

    def addNodes(self):
        self.G.add_nodes_from(self.nodes)

    def createEdges(self):
            for (i,j) in self.nodes:
                for (k,l) in self.nodes:
                    if self.checkEdges(i,j,k,l):
                        self.edges.append(((i,j),(k,l)))

    def checkEdges(self,i,j,k,l):
        if self.board_type == 0:
            if i == k + 1 and j == l + 1:
                return True
            elif i == k + 1 and j == l:
                return True
            elif i == k and j == l + 1:
                return True
            else:
                return False

        elif self.board_type == 1:
            if i == k + 1 and j == l - 1:
                return True
            elif i == k + 1 and j == l:
                return True
            elif i == k and j == l + 1:
                return True
            else:
                return False

    def randomStart(self):
        x = np.random.randint(0,self.size)
        y = np.random.randint(0,self.size)
        self.nodes[(x,y)] = "red"

    def colorChange(self):
        color_list = []
        for (i,j) in self.nodes:
            temp = self.nodes[(i,j)]
            color_list.append(temp)

        return color_list





g = Grid(1,4)
g.createNodes()
g.addNodes()
g.createEdges()
g.drawGrid()