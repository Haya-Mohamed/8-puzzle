

import State as st
import Util as ut
import SearchAgents as agent
  
class A_State (st.State):

    def __init__ (self , a_cost,*args , **kawrgs):
        super(A_State,self).__init__(*args,**kawrgs)
        self.a_cost = a_cost

    def __gt__(self, other): 
        return self.a_cost > other.a_cost

    

def main():
        str = '125340678'
        utility_obj = ut.Util()
        board, blank = utility_obj.get_board(str)
        obj = A_State(19,board, 0, None, blank)
        board, blank = utility_obj.get_board(str)
        obj2 = A_State(12,board, 0, None, blank)
        print(obj.a_cost)
        obj.print()
        print (obj<obj2)

if __name__ == '__main__':
    main()


        