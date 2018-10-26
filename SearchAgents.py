# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:18:24 2018

@author: HRY
"""
import bisect

class Search_Agents:
    # declare global  variable goal :
    #state : initial state
    goal = [['0','1','2'],['3','4','5'],['6','7','8']]
    
    def BFS(self,state):
        #to be changed later 
        frontier = []
        frontier.append(state)
        explored = set()         
        while len(frontier) > 0:
            current = frontier.pop(0)
            
            if current.test_goal(self.goal):
                return current, explored
            
            if not isVisited(current, explored):
                explored.add(current)
                current.get_children()
            
                for child in current.children:
                    if isVisited(child, explored):
                        continue
                    frontier.append(child)
               
    
    def DFS(self, state):
        frontier = []
        explored = set()
    
        frontier.append(state)
        while len(frontier) > 0:
            current = frontier.pop()
            
            if current.test_goal(self.goal):
                return current, explored
            
            if not isVisited(current, explored):
                explored.add(current)
                current.get_children()

                for child in reversed(current.children):
                    if isVisited(child, explored):
                        continue
                    frontier.append(child)

        
    def A(self, state):
        
        frontier = []
        explored = set()
        frontier.append(state)
        
        while len(frontier) > 0:
            current = frontier.pop(0)
            if not isVisited(current, explored):
                explored.append(current)
            
                if current.test_goal(self.goal):
                    return current, explored 
            
                current.get_children()
                for child in current.children:
                    if isVisited(child, explored):
                        continue
                    bisect.insort(frontier, child)
                    

def isVisited(state, explored):
    if state in explored:
        return True
    
    return False   
    
def isVisiting(state, frontier):
    if state in frontier:
        return True
   
    return False