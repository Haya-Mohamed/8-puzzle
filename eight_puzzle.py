# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:06:34 2018

@author: User
"""
import State as st
import Util as ut
import SearchAgents as agent
     
def main():
    
    
    
    str = '102345678'
    utility_obj = ut.Util()
    
    board, blank = utility_obj.get_board(str)
    obj = st.State(board, 0, None, blank)
    #obj.print()
    # obj.get_children()
    """
    for i in obj.children :
        i.print()
    """
    
  #  print (obj.test_goal(goal_state))
    
    bfs = agent.Search_Agents.BFS(agent.Search_Agents.BFS,obj)
    
if __name__ == '__main__':
    main()