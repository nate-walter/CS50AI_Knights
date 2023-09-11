from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")


# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # General Information: A is either a knight or a knave, but not both
    Or(
        And(AKnight, Not(AKnave)),
        And(Not(AKnight), AKnave)
    ),

    # Specific Information: A says "I am both a knight and a knave."
    # This is contradictory. If A is a Knight, then the sentence has to be true (which it can't be).
    # If A is a Knave, then the sentence has to be false (which is true in this case).
    And(
        Implication(AKnight, And(AKnight, AKnave)),
        Implication(AKnave, Not(And(AKnight, AKnave)))
    )
)



# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # General Information: A and B are either Knights or Knaves, but not both.
    
    Or(And(AKnight, Not(AKnave)), And(Not(AKnight), AKnave)),
    Or(And(BKnight, Not(BKnave)), And(Not(BKnight), BKnave)),

     
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Or(AKnight, BKnight))
)



# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(

    # General Information A and B are either Knights or Knaves, but not both.
    Or(And(AKnight, Not(AKnave)), And(Not(AKnight), AKnave)),
    Or(And(BKnight, Not(BKnave)), And(Not(BKnight), BKnave)),



    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Implication(AKnave, Or(And(AKnight, BKnave), And(AKnave, BKnight))),

    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))), 
    Implication(BKnave, Or(And(AKnight, BKnave), And(AKnight, BKnight)))
)



# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(And(AKnight, Not(AKnave)), And(Not(AKnight), AKnave)),
    Or(And(BKnight, Not(BKnave)), And(Not(BKnight), BKnave)),
    Or(And(CKnight, Not(CKnave)), And(Not(CKnight), CKnave)),

    # A says either "I am a knight." or "I am a knave.", but you don't know which.
    Implication(AKnight, AKnight),
    Implication(AKnave, AKnight),

    # B says "A said 'I am a knave'."
    Implication(BKnight, AKnave),
    Implication(BKnave, AKnight),

    # B says "C is a knave."
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),

    # C says "A is a knight."
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave)
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
