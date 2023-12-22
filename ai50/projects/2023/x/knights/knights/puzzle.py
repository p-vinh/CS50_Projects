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
    Or(AKnight, AKnave), # A must be either a knight or a knave
    Implication(AKnight, Not(AKnave)), # If A is a knight, then A is not a knave
    Implication(AKnave, Not(AKnight)), # If A is a knave, then A is not a knight
    
    Biconditional(AKnight, And(AKnight, AKnave)) # A is a knight if and only if A is both a knight and a knave
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(    
    Or(AKnight, AKnave), # A must be either a knight or a knave
    Implication(AKnight, Not(AKnave)), # If A is a knight, then A is not a knave
    Or(BKnight, BKnave), # B must be either a knight or a knave
    Implication(BKnight, Not(BKnave)), # If B is a knight, then B is not a knave
    
    # Info from the given statements
    Biconditional(AKnight, And(AKnave, BKnave)) # A is a knight if and only if A and B are both knaves
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(    
    # Infomation about the structure of the puzzle
    Or(AKnight, AKnave), # A must be either a knight or a knave
    Implication(AKnight, Not(AKnave)), # If A is a knight, then A is not a knave
    
    Or(BKnight, BKnave), # B must be either a knight or a knave
    Implication(BKnight, Not(BKnave)), # If B is a knight, then B is not a knave
    
    # Info from the given statements
    Biconditional(AKnight, Or(And(AKnight, BKnight),
                              And(AKnave, BKnave))), # A is a knight if and only if A and B are both knights or both knaves
    Biconditional(BKnight, Or(And(AKnave, BKnight),
                              And(AKnight, BKnave))) # B is a knight if and only if A is a knave and B is a knight or A is a knight and B is a knave
    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Infomation about the structure of the puzzle
    Or(AKnight, AKnave), # A must be either a knight or a knave
    Implication(AKnight, Not(AKnave)), # If A is a knight, then A is not a knave
    Or(BKnight, BKnave), # B must be either a knight or a knave
    Implication(BKnight, Not(BKnave)), # If B is a knight, then B is not a knave
    Or(CKnight, CKnave), # C must be either a knight or a knave
    Implication(CKnight, Not(CKnave)), # If C is a knight, then C is not a knave
    
    # Info from the given statements
    Biconditional(AKnight, Or(AKnight, AKnave)), # A is a knight if and only if A is a knight or A is a knave
    # B is a knight if and only if A is a knave
    Biconditional(BKnight, Biconditional(AKnight, AKnave)), # B is a knight if and only if (A is a knight if and only if A is not a knave)
    Biconditional(BKnight, CKnave), # B is a knight if and only if C is a knave
    Biconditional(CKnight, AKnight) # C is a knight if and only if A is a knight
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
