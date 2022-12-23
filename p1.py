#INFO 190S Project 1 Slayer Puzzle

#Brief description message
print("Solve: SLAYER + SLAYER + SLAYER = LAYERS")

#Prompt user for a single guess for SLAYER
SLAYER = int(input("What is your guess? "))

#Adding SLAYER thrice
SLAYER3 = SLAYER + SLAYER + SLAYER

#Computing for LAYERS
S = SLAYER // 100000
LAYER = SLAYER % 100000
LAYERS = (LAYER * 10) + S

#Print message showing if the guess solved the puzzle
print(f"{LAYERS} == {SLAYER3} -> {SLAYER3 == LAYERS}")

