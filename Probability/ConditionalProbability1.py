import random

def printProbabilityOfWining(takes: int, repeats: int, replace:bool = True) -> None:
    '''
    - takes - number of tries in the game.
    - repeats - number of times the game is repeated
    - replace - True if the white ball is replaced
    '''
    # number of times first or second wins
    first_wins = 0
    second_wins = 0
    # total number of times 
    total = 0

    # loop through number of times game is played
    for x in range(repeats):
        probability_factor = 10
        # loop through otal Number of tries in the game
        for y in range(takes):
            # Simulates the probability of wining
            n = random.randint(1, probability_factor)
            # Only when ball is not replaced back
            if not replace: 
                probability_factor -= 1
            # One is the wining digit/or simulates the white ball
            if(n == 1):
                # Player 2
                if(y%2 == 0):
                    second_wins += 1
                    break
                # Player 1
                else:
                    first_wins += 1
                    break
        # Adds irrespective of win or loss or draw
        total += 1

    # Averages the result for the repeats to find probability
    if not replace: print("Without replacement")
    else: print("With Replacement")
    print("First Wining Probability " + str(first_wins/total))
    print("Second Wining Probability " + str(second_wins/total))
    

printProbabilityOfWining(takes=10, repeats=1000000, replace=False)
printProbabilityOfWining(takes=10, repeats=1000000)

