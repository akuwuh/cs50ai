from logic import *


# to do add knowledge to each puzzle



AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
# if a is knight -> I am both a knight and a knave
# if a is knave -> "iam both a knight and a knave" has to be false 
knowledge0 = And(

    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnave, Not(AKnight)),

    Implication(AKnight,
        And(AKnight, AKnave) #should return false
    ),

    Implication(AKnave,      
        Not(And(AKnight, AKnave))
    )
)

# Puzzle 1
# A says "We are both knaves."
# a is a knave -> not()
# B says nothing.
knowledge1 = And(

    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(BKnave, Not(BKnight)),

    Implication(AKnave,
        Not(And(AKnave, BKnave))
    ),
    Implication(AKnight,
        And(AKnave, BKnave)
    )
)

# Puzzle 2
# A says "We are the same kind."
# if a is a knave -> we are of different kinds -> AKnave and BKnight
# if a is a knight -> they have to be both knights
# B says "We are of different kinds."
# if b is a knave -> we are of same kind -> BKnave and AKnave
# if b is a knight -> we of different kinds -> BKnight and AKnave
knowledge2 = And(

    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(BKnave, Not(BKnight)),

    Implication(AKnight,
        And(AKnight, BKnight)
    ),

    Implication(AKnave,
        And(AKnave, BKnight)
    ),

    Implication(BKnight,
        And(BKnight, AKnave)
    ),

    Implication(BKnave,
        And(AKnave, BKnave)
    )
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# if aKnight -> aknight or aknave 
# if aknave -> not(aknight or aknave)
# B says "A said 'I am a knave'."
# bknight -> a said i am a knave is true 
#   A is a knave -> Not(BKnave)
#   A is a knight -> (BKnave)
# bknave -> a DID NOT say i was a knave -> it doesnt matter what A actualy is
# B says "C is a knave."
# Bkngiht -> CKnave
# BKnave -> Not(CKnave)


# C says "A is a knight."
knowledge3 = And(

    Biconditional(AKnight, Not(AKnave)),
    Biconditional(AKnave, Not(AKnight)),
    Biconditional(BKnight, Not(BKnave)),
    Biconditional(BKnave, Not(BKnight)),
    Biconditional(CKnight, Not(CKnave)),
    Biconditional(CKnave, Not(CKnight)),

    Implication(AKnight,
        Or(AKnight, AKnave)
    ),

    Implication(AKnave,
        Not(Or(AKnight, AKnave))
    ), 

    Implication(BKnight,
        And(
            Implication(AKnave, 
                Not(BKnave)
            ),

            Implication(AKnight, 
                BKnave
            )
        )
    ), 

    Implication (BKnight,
        CKnave
    ),

    Implication (BKnave,
        Not(CKnave)
    )
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
