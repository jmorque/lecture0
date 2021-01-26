# Programmer: Jesus Morquecho
# Assignment 2
# generalize_astar_search.py
import random
from puzz8 import *
#from jugs import *
import operator

class Node:
    def __init__(self, state = None, path = [],\
                 depth = 0, evalue = None):
        self.thestate = state
        self.thepath = path
        self.thedepth = depth
        self.theeval = evalue

    # Equality by state only!
    def __eq__(self, other):
        return self.thestate == other.thestate

def ASTAR_SEARCH(start, target, GOAL_FCT, EVAL_FCT, SUCCESSOR_FCT):
    open = [Node(start,[start],0,EVAL_FCT(start,target))]
    closed = []
    steps = 0
    while open != []:
        nxt = open[0]
        open = open[1:]

        nxtstate = nxt.thestate #unpack the Node
        nxtpath = nxt.thepath
        nxteval = nxt.theeval
        nxtdpth = nxt.thedepth

        if GOAL_FCT(nxtstate,target):
            print("GOAL FOUND:")
            print("State: ",nxtstate)
            print("PathL: ",len(nxtpath))
            print("Steps: ",steps)
            return [nxtstate, nxtpath]

        if nxt in closed:
            continue
        closed.append(nxt)

        succ = SUCCESSOR_FCT(nxtstate)
        random.shuffle(succ)

        for x in succ:
            xcost = EVAL_FCT(x,target)
            newnode = Node(x,addpath(nxtpath,x),\
                           nxtdpth+1,xcost+nxtdpth+1)

            keeper = True
            for c in closed:
                if newnode.thestate == c.thestate and\
                   len(newnode.thepath) >= len(c.thepath):
                    keeper = False
                    break
            if not keeper:
                continue

            for op in open:
                if newnode.thestate == op.thestate and\
                   len(newnode.thepath) >= len(op.thepath):
                    keeper = False
                    break
            if keeper:
                open.append(newnode)
        
        open.sort(key = operator.attrgetter('theeval'))

        steps += 1
        
    return None

# Utility function
def addpath(path,x):
    newpath = path[:] # NOTICE: a copy is made!
    newpath.append(x)
    return newpath

if __name__ == '__main__':

    random.seed()

    goalfct = puzz8_goal_fct
    evalfct = puzz8_eval_fct
    succfct = puzz8_successor_fct
    showfct = show_puzz8
    start_state = puzzE
    goal_state = GOAL

    #goalfct = jugs_goal_fct
    #evalfct = jugs_eval_fct
    #succfct = jugs_successor_fct
    #showfct = show_jugs
    #start_state = [0,0]
    #goal_state = [0,2]

    solnA = ASTAR_SEARCH(start_state,goal_state,\
                         goalfct,evalfct,succfct)
    i = 0
    for p in solnA[1]:
        print("\n{0:d}. move yields: ".format(i))
        showfct(p)
        i+= 1
    




        
