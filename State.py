# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 11:47:38 2018

@author: HRY
"""

import enum

class Actions(enum.Enum) :
    """
    Class used as enum for board's actions (moves)
    """
    UP = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3

class State():
    """
    State class defines the basic attributes and functions 
    for the board 
    """
    
    def __init__ (self, config, cost, action, blank):
        """
        Initializes the state with the needed params
        """
        self.board = config 
        self.board = config
        self.cost = cost
        self.blank_position = blank
        self.action = action
        self.children = []
        self.parent = None
        
    def __eq__(self, other): 
        """
        Overrides eq function
        States are compared with respect to their  2D boards
        """
        return self.board == other.board
    
    def __hash__(self):
        """
        Overrides default hash function
        Uses string representation of boards for the hashing 
        """
        return hash(str(self.board))
                 
    def print(self):
        """
        Print the state's board in a tabular-like format
        """
        for i in range(3):
            print('{} {} {}'.format(self.board[i][0],self.board[i][1],self.board[i][2]))
        print('\n')

    def print_children(self):
        """
        Print boards of all children
        """
        for child in self.children:
            child.print()       
     
    def get_children(self):
        """
        Gets all the neighbours of the current state
        Adds all valid neighbours to children list
        """
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
        """
        Moves the blank position to a new position
        Returns the new state after moving the blank position
        """
        new_board = [[self.board[x][y] for y in range(3)] for x in range(3)]
        new_board[new_blank_position[0]][new_blank_position[1]] = '0'
        new_board [self.blank_position[0]][self.blank_position[1]] = self.board [new_blank_position[0]][new_blank_position[1]] 
        child = State(new_board, self.cost + 1, action, new_blank_position)
        child.parent = self
        return child
        
        
    def test_goal(self,goal):
        """
        Test the current state with the goal state
        by comparing boards
        """
        if self.board == goal:
            return True
        return False
