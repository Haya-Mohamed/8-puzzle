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
            current = frontier.pop(0)
            # frontier_boards.pop(0)
            current.get_children()
            explored.append(current)
            # explored_boards.append(current.board)
            # current.print()
            # print("children :")
            # current.print_children()
            #print(current.cost)
            # current.print()
            


            if st.State.test_goal(current,goal):
                # current.print()
                print("Total cost is {} , depth = {}".format(current.cost,depth))
                return state
            
            #loop for state's children

            for child in current.children:
                eq =0
                for i in frontier:
                    if child.board==i.board:
                        eq=eq+1
                for i in explored:
                    if child.board ==i.board:
                        eq = eq+1
                
                if eq == 0:
                    frontier.insert(0,child)
                
                # if child not in frontier and child not in explored:
                #     #print("child")
                #     # child.print()
                #     # print('state added : ')
                #     # child.print()
                #     # print("enter")
                #     frontier.insert(0,child)
                #     frontier_boards.insert(0,child.board)
               
    
    def DFS(self, state):
        print("bla")
        
        
        
        
        
        
        
    def A(self):
        print("bla bla")
        
        