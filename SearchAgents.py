# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:18:24 2018

@author: HRY
"""

import State as st
class Search_Agents:
    
    # declare global  variable goal :
    #state : initial state
    def BFS(self,state):
        #to be changed later
        goal = [['0','1','2'],['3','4','5'],['6','7','8']]
        frontier = []
        frontier.append(state)
        explored = [] 
        depth = 0
        
        while len(frontier) > 0:
            depth = depth + 1
            current = frontier.pop(len(frontier)-1)
            current.get_children()
            explored.append(current)
            if st.State.test_goal(current,goal):
                print("Total cost is {} , depth = {}".format(current.cost,depth))
                return state
            
            #loop for state's children
            for child in current.children:
                if child not in frontier and child not in explored:
                    frontier.insert(0,child)
               
    
    def DFS(self, state):
        print("bla")
        
        
        
        
        
        
        
    def A(self):
        print("bla bla")
        
        