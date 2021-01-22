import sys
print(sys.path)
import networkx as nx
import matplotlib.pyplot as plt
import random

class Grid:
    def __init__(self, type, size, initial = [], random = 0):
        self.__type = type
        self.__size = size


        # draw with break between frames given in "play"
    def draw(self, animation_delay = 0):
        fig = plt.figure(figsize = (9,7))
        plt.axes()
        filled = self.__cellsWithPeg()
        empty = self.__emptyCells()
        if not (self.__jumpedTo is None and self.__jumpedFrom is None): # if first move has been made
            filled.remove(self.__jumpedTo)
            empty.remove(self.__jumpedFrom)
            nx.draw(self.__G, pos = self.__positions, nodelist = [self.__jumpedTo], node_color='blue', node_size = 2400, ax = fig.axes[0])
            nx.draw(self.__G, pos = self.__positions, nodelist = [self.__jumpedFrom], node_color='black', node_size = 200, ax = fig.axes[0])
        nx.draw(self.__G, pos = self.__positions, nodelist = filled, node_color='blue', node_size = 800, ax = fig.axes[0])
        nx.draw(self.__G, pos = self.__positions, nodelist = empty, node_color='black', node_size = 800, ax = fig.axes[0])
        if animation_delay: # run animation automatically if delay > 0
            plt.show(block = False)
            plt.pause(animation_delay)
            plt.close()
        else: # show single figure if delay not given
            plt.show(block = True)