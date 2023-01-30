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
    # A can only be knight or knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # If A is knight, then A is both knight and knave
    Implication(AKnight, And(AKnight, AKnave)),
    # If A is knave, then A is either knight or knave
    Implication(AKnave, Not(And(AKnight, AKnave))),
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A can only be knight or knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B can only be knight or knave, but not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # If A is knight, then A and B are both knave
    Implication(AKnight, And(AKnave, BKnave)),
    # If A is knave, then A and B arent both knave
    Implication(AKnave, Not(And(AKnave, BKnave))),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A can only be knight or knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B can only be knight or knave, but not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # If A is knight, then A and B are on same kind
    Implication(AKnight, Biconditional(AKnight, BKnight)),
    # If A is knave,  then A and B are on different kind
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),
    # If B is knight,  then A and B are on different kind
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),
    # If B is knave,  then A and B are on same kind
    Implication(BKnave, Biconditional(AKnight, BKnight))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A can only be knight or knave, but not both
    And(Or(AKnight, AKnave), Not(And(AKnight, AKnave))),
    # B can only be knight or knave, but not both
    And(Or(BKnight, BKnave), Not(And(BKnight, BKnave))),
    # C can only be knight or knave, but not both
    And(Or(CKnight, CKnave), Not(And(CKnight, CKnave))),
    # If A is knight, then either he is knight or knave
    Implication(AKnight, Or(AKnight, AKnave)),
    # If A is knave, then either he is neither knight nor knave
    Implication(AKnave, Not(Or(AKnight, AKnave))),
    # If B is knight, then A is knave if A is knight
    Implication(BKnight, 
        Implication(AKnight, AKnave)),
    # If B is knight, then A is knight if A is knave
    Implication(BKnight, 
        Implication(AKnave, Not(AKnave))),   
    # If B is knave, then A is knave if A is knight
    Implication(BKnave,
        Not(Implication(AKnight, AKnave))),
    # If B is knave, then A is knight if A is knave
    Implication(BKnight, 
        Not(Implication(AKnave, Not(AKnave)))), 
    # If B is knight, then C is knave
    Implication(BKnight, CKnave),
    # If B is knave, then C is knight
    Implication(BKnave, Not(CKnave)),
    # If C is knight, then A is knight
    Implication(CKnight, AKnight),
    # If C is knave, then A is knave
    Implication(CKnave, Not(AKnight)),
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
