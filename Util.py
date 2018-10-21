# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:03:53 2018

@author: User
"""

class Util:
     def get_board(self,config):
        index = 0
        board = [[0 for x in range(3)] for y in range(3)]
        blank_position = tuple()
        for i in range (3):
            for j in range (3):
                if config[index] == '0':
                    blank_position = (i, j)
                board[i][j] = config[index]
                index = index + 1
        return board, blank_position



