# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:06:34 2018

@author: HRY
"""
import State as st
import A_State as ast
import Util as ut
import SearchAgents as agent
import time

def init(init_board, Strategy):
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
    
    for s in reversed(path):
        s.print()
        print('----------')
    """
    
    for s in explored:
        s.print()
        print('--------------')
    """ 
    print('Depth = ', len(path))
    print('Execution Time = ', execution_time)
        
     
def main():
    init('142658730', 'dfs')

if __name__ == '__main__':
    main()