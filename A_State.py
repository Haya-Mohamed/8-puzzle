

import State as st
import Util as ut
import math
  
class A_State (st.State):

    goal_board = [['0','1','2'],['3','4','5'],['6','7','8']]
    def __init__ (self , a_cost,*args , **kawrgs):
        super(A_State,self).__init__(*args,**kawrgs)
        self.a_cost = a_cost

    def __gt__(self, other): 
        return self.a_cost > other.a_cost

    
    def calculate_manhattan_distance(self, current_position, goal_position):
        return abs(current_position[0] - goal_position[0]) + abs(current_position[1] - goal_position[1])
        
    def calculate_euclidean_distance(self, current_position, goal_position):
        return math.sqrt((current_position[0] - goal_position[0])**2 + (current_position[1] - goal_position[1])**2)

    
    def move(self, action, new_blank_position, strategy):
        util_obj = ut.Util()
        goal_position = util_obj.index_2d(self.goal_board, self.board[new_blank_position[0]][new_blank_position[1]])
        h = self.calculate_manhattan_distance(new_blank_position, goal_position)
        #h = self.calculate_euclidean_distance(new_blank_position, goal_position)
        new_board = [[self.board[x][y] for y in range(3)] for x in range(3)]
        new_board[new_blank_position[0]][new_blank_position[1]] = '0'
        new_board [self.blank_position[0]][self.blank_position[1]] = self.board [new_blank_position[0]][new_blank_position[1]] 
        child = A_State(h + self.cost + 1, new_board, self.cost + 1, action, new_blank_position)
        return child

        