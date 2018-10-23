# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:06:34 2018

@author: HRY
"""
import State as st
import Util as ut
import SearchAgents as agent
     
def main():
    
    str = '125340678'
    utility_obj = ut.Util()
    board, blank = utility_obj.get_board(str)
    obj = st.State(board, 0, None, blank)
    goal = [['0','1','2'],['3','4','5'],['6','7','8']]
    man = obj.calculate_manhattan_distance(goal)
    euc = obj.calculate_euclidean_distance(goal)
    # print ("manhattan : {} , euclidean : {}".format(man,euc))
    
    bfs = agent.Search_Agents.BFS(agent.Search_Agents.BFS,obj)
    # dfs = agent.Search_Agents.DFS(agent.Search_Agents.DFS,obj)
if __name__ == '__main__':
    main()