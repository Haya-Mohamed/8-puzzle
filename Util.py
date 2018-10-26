# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:03:53 2018

@author: HRY
"""
import State as St

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

     def back_track(self, state):
        list = [] 
        while state.parent:
            list.append(St.Actions(state.action))
            state = state.parent
        return list


def index_2d(board, search):
        for i, e in enumerate(board):
            try:
                return i, e.index(search)
            except ValueError:
                pass
        raise ValueError("{} is not in list".format(repr(search)))
