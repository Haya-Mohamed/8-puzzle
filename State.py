# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 11:47:38 2018

@author: Haya Rowan Youssef
"""
#from enum import Enum

import math

class Actions :
    UP = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3

class State():
    
    #Actions = Enum ('UP','DOWN', 'LEFT' , 'RIGHT') 
    #init every time object created ? 
    def __init__ (self, config, cost, action, blank):
        self.board = config #[[0 for x in range(3)] for y in range(3)] 
        self.board = config
        self.cost = cost
        self.blank_position = blank
        self.action = action
        self.children = [] 
        # self.get_children()
                 
    def print(self):
         for i in range(3):
            print('{} {} {}'.format(self.board[i][0],self.board[i][1],self.board[i][2]))
         print('\n')


    def print_children(self):
        for child in self.children:
            child.print()       

    def __eq__(self, other): 
        return self.board == other.board
        
            
    def get_children(self):
        left = (self.blank_position[0], self.blank_position[1] - 1)
        right = (self.blank_position[0], self.blank_position[1] + 1)
        up = (self.blank_position[0] - 1, self.blank_position[1])
        down = (self.blank_position[0] + 1, self.blank_position[1])
        if left[1] in range(3):
            self.children .append (self.move(Actions.LEFT, left))
        if right[1] in range(3):
            self.children .append (self.move(Actions.RIGHT, right))
        if up[0] in range(3):
            self.children .append (self.move(Actions.UP, up))
        if down[0] in range(3):
            self.children .append (self.move(Actions.DOWN, down))
        
        
    def move(self, action, new_blank_position):
        new_board = [[self.board[x][y] for y in range(3)] for x in range(3)]
        new_board[new_blank_position[0]][new_blank_position[1]] = '0'
        new_board [self.blank_position[0]][self.blank_position[1]] = self.board [new_blank_position[0]][new_blank_position[1]] 
        child = State(new_board, self.cost + 1, action, new_blank_position)
        return child
        
        
    # define goal_state global variable
    def test_goal(self,goal):
       return self.board == goal 



    def calculate_manhattan_distance(self,goal_board):
        distance = 0 
        for i in range(3):
            for j in range (3):  
                position = index_2d(self.board,goal_board[i][j])
                distance = distance + (abs(position[0]-i) + abs (position[1]-j))
        return distance
        
    def calculate_euclidean_distance(self,goal_board):
        distance = 0 
        for i in range(3):
            for j in range (3):  
                position = index_2d(self.board,goal_board[i][j])
                distance = distance + math.sqrt((position[0]-i)**2 + (position[1]-j)**2)
        return distance 


def index_2d(board, search):
    for i, e in enumerate(board):
        try:
            return i, e.index(search)
        except ValueError:
            pass
    raise ValueError("{} is not in list".format(repr(search)))
    
       