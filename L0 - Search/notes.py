# Harvard CS50AI Lecture 0

'''
/* ------ */
/* Search */
/* ------ */

Search Problems:

    Agent given intial + goal state
    Returns solution of how get from one to another
    
    i.e: 
        Navigator app given location + destination
        Uses search algorithm to return suggested path

        
Agent: 

    Entity that perceives + acts within environment
    
    i.e:
        In a navigator app, Agent = Car
        Needs to decide on actions (turns) to reach destination

        
State:

    A configuration of an agent in its environment (generalized)
    
    i.e:
        In 15 puzzle, any arrangements of numbers on the board
    
    Initial State = starting configuration of agent before search algorithm starts

    
Actions:

    Choices that can be made in a state (can be defined as a "function")
    
    Given state "s", "Action(s)" returns set of actions that can be executed in state s


Transition Model:

    Description of state resulting from performing any action in any state

    Given state "s", action "a", "Result(s,a)" returns next state after performing action "a" in state "s"
    

State Space:

    Set of all states reachable from initial state given any sequences of actions
    Similar to solution space. Effectively describes "all possible outcomes"


Goal Test:

    Condition determining whether a given state is the goal state

    i.e:
        In navigator app, current location == destination
    

Path Cost: 

    Cost for given path

    i.e: 
        Fuel in navigator app


/* ----------------------- */
/* Solving Search Problems */
/* ----------------------- */


Solution: 

    A sequence of actions leading initial state to goal state

    Optimal = one w/ the lowest path cost


Node:

    Data structure to store data during search process

    Stores:

        state - checked against the goal to determine if problem has been solved
        parent node - "previous node"
        action - operation applied to go from parent node -> current node
        path cost - total cost of goin from initial state to current state

        
Search Algorithm:

    "Frontier" used to solve search problems by managing nodes

    Repeat:

        1. If frontier == empty:
            
            Stop, No solution to problem

        2. Remove node from frontier

        3. If node == goal:

            Return solution, Stop

        Else:

            Expand node (find new nodes reachable from current node) + Add resulting node to frontier
            Add current node to set of visited nodes

        
DFS (Depth-First Search):

    Exhausts one direction before considering another direction
    Managed using a "Stack" (LIFO)

    Pros:

        Best Case -> Fastest algorithm (if alwyas picking correct action)

    Cons:

        Solution might not be optimal 
        Worst Case -> Badddd (exploring every possible path)

    Code Example:
'''
# frontier = stack to manage nodes
# function to remove node from frontier (stack)
def remove(self): 
    if self.empty():
        raise Exception("Empty Frontier")
    else:
        node = self.frontier[-1]
        self.frontier = self.frontier[:-1]
        return node

'''
BFS (Breadth-First Search):

    Follows multiple directions simultaneously
    Managed using a "Queue" (FIFO)

    Pros:

        Guarantees optimal solution

    Cons:

        Almost never the fastest runtime
        Worst Case = longest possible time to run

    Code Example:
'''
def remove(self):
    if self.empty(): 
        raise Exception("Empty Frontier")
    else: 
        node = self.frontier[0]
        self.frontier = self.frontier[1:]
        return node
    
'''

BFS and DFS are "uninformed" search algorithms. Do not utilize any knowledge about problem.

"Informed" search algorithms = one that considers additional knowledge to improve performance


Greedy Best-First Search: 

    Expands node closest to the goal, determined by a "heurisitc function" 

    Heuristic Function h(n):

        Estimates how close to the goal the next node is
        But can be mistaken 
    
    Efficiency of GBFS depends on how good the "heuristic function" is
    
    i.e:
        For a maze, heuristic function could be one that uses Manhattan disance to determine closeness to the goal 

    
    Takeaway: 

        Less likely for "uninformed" search to determine better solution faster than "informed" search


A* Search:

    Employs both h(n) and g(n)
        
        g(n): function that considers cost accurred to reach the current state

    Keeps track of ( cost of path until now + estimatd cost to goal )
                            g(n)                    h(n)
    
    If estimated cost of current path exceeds previously considered paths, goes back to previous option

    
    For A* search to be optimal, the heuristic function h(n) should be:

        1. Admissible - never overestimating the true cost
        2. Consistent - h(n) if consistent if for everynode n, next node n' w/ step cost c:

            h(n) <= h(n') + c

            Moving to n' should be less than or equal to estimated cost to goal


Adversarial Search:

    Algorithm that faces "opponent" trying to reach opposite goal 


Minimax:

    A type of adversarial search algorithm

    Represents "winning conditions" as (-1) and (+1) for different sides
    
        Actions will be driven by these conditions

        Minimizing side tries to get lowest score
        Maximizing side tries to get highest score

    i.e Tic Tac Toe AI:

        S_0: initial state (empty 3x3 board)

        Players(s): given state "s", returns the turn of player

        Actions(s): given state "s", returns all "legal" moves in current state

        Result(s,a): given state "s", action "a", returns resulting state

        Terminal(s): given a state "s", returns True if the game has ended, False otherwise

        Utility(s): given a terminal state "s", returns "utility" value as -1,0,+1


        How the algorithm works:

            Recursively simulate all possible games that can take place at any current state

            Once terminal state is reached, utility value is either -1,0,+1

        
        Minimax Algorithm in Tic Tac Toe:

            I get it, but idk how to take notes for it 
            Maximizer considers possible values fo future states

        Diagram:

                         9
                     ____|____
                    |    |    |
                    5    3    9

        Pseudo:

            Given state s:

                Maximizing player picks action "a" in Action(s) s.t they produce the highest Min-Value(Results(s,a))

                Minimizing player picks action "a" in Action(s) s.t they produce the lowest Max-Value(Results(s,a))

            Function Max-Value(state): max possible value that can be achieved

                v = -infinity
                if Terminal(state) == True: return Utility(state)
                
                for action in Action(state):
                
                    v = max(v, Min-Value(Result(state,action)))
                    return v

            Function Min-Value(state): # min possible value that can be achieved

                v = infinity
                if Terminal(state) == True: return Utliity(state)

                for action in Action(state):
                    
                    v = min(v, Max-Value(Result(state,action)))
                    return v
            

Alpha-Beta Pruning:

    Used to optimize Minimax by skipping computations that are deemed unfavourable

    i.e:
        Consider the decision tree:

                      4
            __________|__________
           |          |          |
           4        <= 3       <= 2
         __|__      __|__      __|__
        |  |  |    |  |  |    |  |  |
        4  8  5    9  3  ?    2  ?  ?

        1. Maximizer current state = 4, and has 3 options.
        2. Starting with first option, it is a 4.
        3. Now maximizer must calculate the value for the next moves.
        4. This is done by "generating" the values of the minimizer's actions
        5. For the second action, the first action is a 9, but the second one is a 3
        6. If the maximizer takes this second action, the minimizer will then pick the action w/ a value of 3. Which is worse than the action value of 4 for the maximizer
        7. Same thing for 2, theres no point calculating remaining action values if there is already a max/min value that presents the best worst case scenario for the maximizer for each option

        
There is a total of 255,168 possible Tic Tac Toe games

Minimax w/ Alpha-Beta Pruning requires generating all possible outcomes from a state to terminal state

This is super computationally heavy


Depth-Limited Minimax:

    Considers only "pre-defined" number of moves before stopping algorithm (not reaching terminal state)

        Not allowing accurate evaluations of each action values

    Relies on "evaluation function" - estimates expected utility of the game from a given state

        In other words: "Assigns expected values to states" 

    i.e Chess:

        Utlity Function:
        
            Takes current config of board as input

            Tries to assess expected utility 

            Returns positive or negative value (represents favourability of board for one player vs the other)

        These values can be used to decide on the correct action

        The better the evaluation function, the better the minimax algorithm

'''



