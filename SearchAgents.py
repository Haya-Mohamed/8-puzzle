# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:18:24 2018

@author: HRY
"""
import bisect

class Search_Agents:
    
    goal = [['0','1','2'],['3','4','5'],['6','7','8']]
    # declare global  variable goal :
    #state : initial state
    def BFS(self,state):
        #to be changed later 
        frontier = []
        frontier.append(state)
        explored = []         
        while len(frontier) > 0:
            current = frontier.pop(0)
            current.get_children()
            explored.append(current)
            if current.test_goal(self.goal):
                print("Total cost is {} , depth = {}".format(current.cost,current.cost))
                return current
            
            #loop for state's children
            for child in current.children:
                if isVisited(child, explored) or isVisiting(child, frontier):
                    continue
                frontier.append(child)
               
    
    def DFS(self, state):
        frontier = []
        explored = []
    
        frontier.append(state)
        depth = 0
        while len(frontier) > 0:
            current = frontier.pop()
            current.print()
            explored.append(current)
            if current.test_goal(self.goal):
                print(depth)
                return current

            not_leaf = False
            current.get_children()

            for child in reversed(current.children):
                if isVisited(child, explored) or isVisiting(child, frontier):
                    continue
                frontier.append(child)
                not_leaf = True

            if not_leaf:
                depth = depth + 1
            else: 
                depth = depth - 1
        

        
    def A(self, state, heuristic):
        
        frontier = []
        explored = []
        frontier.append(state)
                
        while len(frontier) > 0:
            current = frontier.pop()
            explored.append(current)
            
            if current.test_goal(self.goal):
                return current 
            current.get_children()
            for child in current.children:
                if isVisited(child, explored):
                    continue
                node = isVisiting(child, frontier)
                if node:
                    if node.a_cost > child.a_cost:
                        node.a_cost = child.a_cost
                else:
                    bisect.insort(frontier, child)
 

def isVisited(state, explored):
    for s in explored:
        if s.board == state.board:
            return True
    return False   
    
def isVisiting(state, frontier):
    for s in frontier:
        if s.board == state.board:
            return s
    return None