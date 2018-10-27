# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:18:24 2018

@author: HRY
"""
import bisect

class Search_Agents:
    """
    Defines the 3 search agents used to solve the 8-puzzle
    """
    goal = [['0','1','2'],['3','4','5'],['6','7','8']]
    
    def BFS(self,state):
        """
        Implements BFS algorithm for 8-puzzle
        """
        frontier = []
        frontier.append(state)
        explored = set()         
        while len(frontier) > 0:
            current = frontier.pop(0)

            if not isVisited(current, explored):

                explored.add(current)
                if current.test_goal(self.goal):
                    return current, explored
                current.get_children()
            
                for child in current.children:
                    if isVisited(child, explored):
                        continue
                    frontier.append(child)
               
    
    def DFS(self, state):
        """
        Implements DFS algorithm for 8-puzzle
        """
        frontier = []
        explored = set()
    
        frontier.append(state)
        while len(frontier) > 0:
            current = frontier.pop()
            
            if not isVisited(current, explored):
                
                explored.add(current)
                if current.test_goal(self.goal):
                    return current, explored
                current.get_children()
                
                for child in reversed(current.children):
                    if isVisited(child, explored):
                        continue
                    frontier.append(child)

        
    def A(self, state):
        """
        Implements A* algorithm for 8-puzzle
        """
        
        frontier = []
        explored = set()
        frontier.append(state)
        
        while len(frontier) > 0:
            current = frontier.pop(0)
            if not isVisited(current, explored):
                explored.add(current)
            
                if current.test_goal(self.goal):
                    return current, explored 
            
                current.get_children()
                for child in current.children:
                    if isVisited(child, explored):
                        continue
                    bisect.insort(frontier, child)
                    

def isVisited(state, explored):
    """
    Searches for the state in explored set
    """
    if state in explored:
        return True
    return False   
    
def isVisiting(state, frontier):
    """
    Searches for the state in frontier list
    """
    if state in frontier:
        return True
    return False