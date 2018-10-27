import State as st
import Util as ut
import math
  
class A_State (st.State):
    """
    State class for A* search
    Inherits from State class
    Cost is calculated based on the heuristics used
    """
    goal_board = [['0','1','2'],['3','4','5'],['6','7','8']]

    def __init__ (self , a_cost,*args , **kawrgs):
        """
        Intitializes A_state with state constructor 
        Sets the A_state cost to the passed cost
        """
        super(A_State,self).__init__(*args,**kawrgs)
        self.a_cost = a_cost

    def __gt__(self, other): 
        """
        Overrides __gt__ function
        Compares A_states with repect to the cost
        """
        return self.a_cost > other.a_cost
    
    def __eq__(self, other): 
        return self.board == other.board
    
    def __hash__(self):
        return hash(str(self.board))
    
    def calculate_euclidean_distance(self,goal_board):
        """
        First heuristic for A* search
        Calculates Euclidean distance between current state and goal state
        """
        distance = 0
        for i in range(3):
            for j in range (3):  
                position = ut.index_2d(self.board,goal_board[i][j])
                distance = distance + math.sqrt((position[0]-i)**2 + (position[1]-j)**2)
        return distance

    def calculate_manhattan_distance(self,goal_board):
        """
        Second heuristic for A* search
        Calculates Manhattan distance between current state and goal state
        """
        distance = 0
        for i in range(3):
            for j in range (3):  
                position = ut.index_2d(self.board,goal_board[i][j])
                distance = distance + (abs(position[0]-i) + abs (position[1]-j))
        return distance
    
    def move(self, action, new_blank_position):
        """
        Moves the blank position to a new position
        Calculates the new cost using Euclidean Distance
        Returns the new state after moving the blank position
        """
        new_board = [[self.board[x][y] for y in range(3)] for x in range(3)]
        new_board[new_blank_position[0]][new_blank_position[1]] = '0'
        new_board [self.blank_position[0]][self.blank_position[1]] = self.board [new_blank_position[0]][new_blank_position[1]] 
        h = self.calculate_euclidean_distance( self.goal_board)
        child = A_State(h + self.cost + 1, new_board, self.cost + 1, action, new_blank_position)
        child.parent = self
        return child

        