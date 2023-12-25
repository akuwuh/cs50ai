# Harvard CS50AI Lecture 1

'''
/* --------- */
/* Knowledge */
/* --------- */

Knowledge-based Agents:

    Agents able to reason based on internal representations of "knowledge"


Sentence:

    An assertion about the world in a knowledge representation language


/* ------------------- */
/* Propositional Logic */
/* ------------------- */

Logic based on "propositions" - statements on the world can either be True or False

Propositional Symbols:

    Denoted by letters (P,Q,R) to represent a proposition

Logical Connectives:

    Logical symbols that connect propositional symbols in order construct more complex reasoning 

    NOT Symbol '¬' or '~' : 

        Inverses truth value of a proposition

        ----------
        | P | ¬P |
        ----------
        | T | F  |
        | F | T  |
        ----------
        
    AND Symbol '∧':

        True if both propositions are true.
        
        -----------------
        | P | Q | P ∧ Q |
        -----------------
        | T | T |   T   |
        | T | F |   F   |
        | F | T |   F   |
        | F | F |   F   |
        -----------------

    OR Symbol 'v':

        True if either propositions are true.
        
        -----------------
        | P | Q | P v Q |
        -----------------
        | T | T |   T   |
        | T | F |   T   |
        | F | T |   T   |
        | F | F |   F   |
        -----------------

        Note: XOR - exclusive OR, requires only one proposition to be true

        Example:

            OR: to eat desert, you have to:

                clean your room 
                    or
                mow the lawn" 

            XOR: for desert, you can either have:

                cookies
                   or 
                ice cream (but you can't have both)

    Implication/Conditional Symbol '->':

        Represents "if, then" sentence structure

        if "hypothesis, then "conclusion"

        Note: when the hypothesis is False, the entire implication is True.

            Hypothesis being false does not "imply" anything about the conclusion
            Technically the conclusion can either be true or false
            We then say that the implication is "trivially true"

        ------------------
        | P | Q | P -> Q |
        ------------------
        | T | T |   T    |
        | T | F |   F    |
        | F | T |   T    |
        | F | F |   T    |
        ------------------

    Biconditional/IFF Symbol '<->': 

        Represents "if and only if" sentence structure
        Equivalent to P -> Q AND Q -> P 
    
        -------------------
        | P | Q | P <-> Q |
        -------------------
        | T | T |    T    |
        | T | F |    F    |
        | F | T |    F    |
        | F | F |    T    |
        -------------------

Model:

    Assignment of truth values to all propositions

    Model = truth assignment which provides "information" about the world

Knowledge Base (KB):

    Set of sentences "known" by a knowledge-based agent
    
    Knowledge given to AI in order to make additional inferences

Entailment '⊨':

    If P ⊨ Q, or P "entails" Q
    Then for every "world" that P is True, Q will also be undisputedly be True too

    i.e:
        P = "It's a Tuesday in January"
        Q = "It's January" 
        Assert that P ⊨ Q

        If it's a "Tuesday in January", then that means that it has to also be "January"

    Entailment -> A relation between 2 sets of assertions represented by a collection of propositions
    Implication -> A logical connective between 2 propositions


/* --------- */
/* Inference */
/* --------- */
    
The process of deriving new sentences from existing ones

Model Checking Algorithm:

    To determine if KB ⊨ a:

        Enumerate all possible models
        If in every model where KB is true, a is also true, then KB ⊨ a


Example:

    P = "It's a Tuesday"
    Q = "It's raining"
    R = "Harry will go for a run"

    KB: (P ∧ ¬Q) -> R
    
    Does KB ⊨ R?

        -----------------------------------------
        | P | ¬Q | R | (P ∧ ¬Q) | (P ∧ ¬Q) -> R |
        -----------------------------------------
        | T | F  | T |    F     |       T       |
        | T | F  | F |    F     |       T       |
        -----------------------------------------
        | T | T  | T |    T     |       T       |
        -----------------------------------------
        | T | T  | F |    T     |       F       |
        | F | F  | T |    F     |       T       |
        | F | F  | F |    F     |       T       |
        | F | T  | T |    F     |       T       |
        | F | T  | F |    F     |       T       |

    Since R is true when KB/ all the models are true, that means KB entails R

Code Representation:
'''
from logic import *

# propositions
rain = Symbol("rain") # raining
hagrid = Symbol("hagrid") # harry visited hagrid
dumbledore = Symbol("dumbledore") # harry visited dumbledore

# our kb
knowledge = And(
    Implication(Not(rain), hagrid), # if not raining, then harry visited hagrid
    Or(hagrid,dumbledore), # harry visited hagrid or dumbledore
    Not(And(hagrid,dumbledore)), # harry can't visit both hagrid and dumbledore
    dumbledore # harry visited dumbledore
)

'''
To run Model Checking Algorithm, we need:

    Knowledge Base - used to draw inferences
    Query/Proprosition - we would like to know if KB entails it 
    Symbols - list of all symbols/atomic propositions used (rain, hagrid, dumbledore)
    Model - truth assignment to each symbol in symbols

Model Checking Algorithm:
'''
def model_check(knowledge, query):
    def check_all(knowledge, query, symbols, model):

        # if each symbol already assigned a truth value (base case)
        # note that this function is recursive
        # once all symbols have been assigned in model, we evaluate entailment of query in said model
        if not symbols:
            if knowledge.evaluate(model): # if knowledge base == true (based on assignment), then we evaluate the query
                return query.evaluate(model) # return true if query is also true
        else:
            remaining = symbols.copy() # shallow copy
            p = remaining.pop() # choose one of the remaining symbols w/o assignment yet

            # assign symbol as true in the model
            model_true = model.copy() 
            model_true[p] = True

            # assign symbol as false in the model
            model_false = model.copy()
            model_false[p] = False
            # if both variations of model returns true, then we have an entailment
            return check_all(knowledge, query, symbols, model_true) and check_all(knowledge, query, symbols, model_false)

    symbols = set.union(knowledge.symbols(), query.symbols())

    return check_all(knowledge, query, symbols, dict())

model_check(knowledge, rain)
'''

'''

