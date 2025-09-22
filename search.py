# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # Make my directions that I'll use later when I have a solution
    from util import Stack

    # Initialize my stack
    dfsStack = Stack()
    dfsStack.push((problem.getStartState(), []))
    
    # Make a list to keep my visited nodes so I don't do repeat work
    visited = set()
        
    while not dfsStack.isEmpty():
        state, actions = dfsStack.pop()
        if state not in visited:
            visited.add(state)
        
        if(problem.isGoalState(state)):
            return actions
        
        for succ, action, cost in problem.getSuccessors(state):
            if succ not in visited:
                dfsStack.push((succ, actions + [action]))
                
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"   
    from util import Queue
    
    bfsQueue = Queue()
    bfsQueue.push((problem.getStartState(), []))
    
    visited = set([problem.getStartState()])
    
    while not bfsQueue.isEmpty():
        state, actions = bfsQueue.pop()

        if(problem.isGoalState(state)):
            return actions
        
        for succ, action, cost in problem.getSuccessors(state):
            if succ not in visited:
                visited.add(succ)
                bfsQueue.push((succ, actions + [action]))
                
    return []
        

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    
    ucsQueue = PriorityQueue()
    ucsQueue.push((problem.getStartState(), [], 0), 0)
    
    visited = set()
    best_g = {problem.getStartState(): 0}
    
    while not ucsQueue.isEmpty():
        state, actions, g = ucsQueue.pop()
        
        if state not in visited:
            visited.add(state)
            
        if(problem.isGoalState(state)):
            return actions
        
        for succ, action, cost in problem.getSuccessors(state):
            new_g = g + cost
            if succ not in best_g or new_g < best_g[succ]:
                best_g[succ] = new_g
                ucsQueue.push((succ, actions + [action], new_g), new_g)
                
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue

    aStarQueue = PriorityQueue()
    start_state = problem.getStartState()
    aStarQueue.push((start_state, [], 0), heuristic(start_state, problem))

    visited = set()
    best_g = {start_state: 0}

    while not aStarQueue.isEmpty():
        state, actions, g = aStarQueue.pop()
        
        if state not in visited:
            visited.add(state)

        if problem.isGoalState(state):
            return actions

        for succ, action, cost in problem.getSuccessors(state):
            new_g = g + cost
            if succ not in best_g or new_g < best_g[succ]:
                best_g[succ] = new_g
                new_actions = actions + [action]
                f = new_g + heuristic(succ, problem)
                aStarQueue.push((succ, new_actions, new_g), f)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
