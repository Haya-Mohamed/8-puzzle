# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:06:34 2018

Main Script for 8-puzzle

@author: HRY
"""
import State as st
import A_State as ast
import Util as ut
import SearchAgents as agent
import time

def init(init_board, Strategy):
    """
    Initializes the board and strategy to solve 8-puzzle
    """
    utility_obj = ut.Util()
    board, blank = utility_obj.get_board(init_board)
    
    agent_driver = agent.Search_Agents()
    state = None
    explored = []
    start_time = time.process_time()
    if Strategy == 'dfs':
        obj = st.State(board, 0, None, blank)
        state, explored = agent_driver.DFS(obj)
    elif Strategy == 'bfs':
        obj = st.State(board, 0, None, blank)
        state, explored = agent_driver.BFS(obj)
    else:
       obj = ast.A_State(0, board, 0, None, blank)
       state, explored = agent_driver.A(obj)
      
    execution_time = time.process_time() - start_time
    
    path = utility_obj.back_track(state)
    
    print('Path:')
    for s in reversed(path):
        print(s)

    print('# of Explored = ', len(explored))
    print('Depth = ', len(path))
    print('Cost = ', len(path))
    print('Execution Time = ', execution_time)
        
     
def main():
    init('102754863', 'bfs')

if __name__ == '__main__':
    main()