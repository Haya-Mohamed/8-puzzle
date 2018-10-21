# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:06:34 2018

@author: User
"""
import State as st
import Util as ut
     
def main():
    str = '102345678'
    utility_obj = ut.Util()
    
    board, blank = utility_obj.get_board(str)
    obj = st.State(board, 0, None, blank)
    obj.print()
    obj.get_children()
    """
    for i in obj.children :
        i.print()
    """
    
    goal_state = [['0','1','2'],['3','4','5'],['6','7','8']]
    print (obj.test_goal(goal_state))
    
if __name__ == '__main__':
    main()