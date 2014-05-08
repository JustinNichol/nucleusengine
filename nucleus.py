import random
successes = 0
focusSpent= raw_input("Please input the number of Focus committed:")
skillRank= raw_input("Please input the rank of the skill being checked:")
actionPool= int(focusSpent) + int(skillRank)
diceResults = []
diceRoll = 0
explodingDice = 0
##print actionPool
 
for x in range(0, int(actionPool)):
    diceRoll = random.randint(1,6)
    diceResults += [diceRoll]
 
diceLength= len(diceResults)
 
print diceResults
 
for roll in diceResults:
##    print roll
    if roll == 6:
        explodingDice += 1
        successes += 1
    elif roll == 1:
        explodingDice -= 1
    elif roll >= 4:
        successes += 1
 
if explodingDice > 0:
    successes += explodingDice
 
print successes

