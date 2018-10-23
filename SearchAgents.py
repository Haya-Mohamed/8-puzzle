# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:18:24 2018

@author: HRY
"""

import State as st
import bisect
import A_State as ast
class Search_Agents:
    
    # declare global  variable goal :
    #state : initial state
    def BFS(self,state):
        #to be changed later
        goal = [['0','1','2'],['3','4','5'],['6','7','8']]
        frontier = []
        frontier.append(state)
        explored = []         
        while len(frontier) > 0:
            current = frontier.pop(len(frontier)-1)
            current.get_children()
            explored.append(current)
            if st.State.test_goal(current,goal):
                print("Total cost is {} , depth = {}".format(current.cost,current.cost))
                return state
            
            #loop for state's children
            for child in current.children:
                if child not in frontier and child not in explored:
                    frontier.insert(0,child)
               
    
    def DFS(self, state):
        frontier = []
        explored = []
        goal = [['0','1','2'],['3','4','5'],['6','7','8']]
        frontier.append(state)
        depth = 0
        while len(frontier) > 0:
            current = frontier.pop()
            current.print()
            explored.append(current)
            if current.test_goal(goal):
                print(depth)
                return 

            not_leaf = False
            current.get_children()

            for child in reversed(current.children):
                if child not in frontier and child not in explored:
                    frontier.append(child)
                    not_leaf = True

            if not_leaf:
                depth = depth + 1
            else: 
                depth = depth - 1
        
            
        
        
        
        
    def A(self,state):
        
        frontier = []
        explored = []
        frontier.append(state)
        goal = [['0','1','2'],['3','4','5'],['6','7','8']]
        while len(frontier) > 0:
            current = frontier.pop(0)
            explored.append(current)

            if current.test_goal(goal):
                #print
                return 
            current.get_children()
            for child in current.children:
                if child not in frontier and child not in explored:
                    frontier.append(child)
                    not_leaf = True

            if not_leaf:
                depth = depth + 1
            else: 
                depth = depth - 1


    
    
        