from random import randint


# MonteCarlo.py
# This program uses a Monte Carlo approach to estimate the probability of winning the dice game "Approach" with different
# "hold" values.
# Recall that approach works like this:
# Both players agree on a limit n.
# Player 1 rolls first. They go until they either exceed n or hold.
# Then player 2 rolls. They go until they either exceed n or beat player 1's score.
# The player who is closest to n without going over wins.
# Note:
# We can reduce this to the problem of player 1 choosing the best value at which to hold.
# This is called a policy; once we know the best number to hold at, we can act optimally.

# To estimate the best number to hold at, we'll try to estimate the probability of winning
# for each possible hold value between n-5 and n.
# Once we have this, we will know which hold value to use for our strategy.

# This function should try each possible hold value 1000000 times. For each time, play a random
# game. If Player 1 wins, increment the appropriate value in the win_table dictionary.

# n is the limit.

def monte_carlo_approach(n):
    win_table = {}
    for i in range(n - 5, n + 1):
        win_table[i] = 0

    ## try each hold value 1000000 times
    for i in range(1000000):
        for hold_val in range(n - 5, n + 1):    
            ## player 1 plays
            player1 = 0
            while player1 <= hold_val and player1 < n:
                player1 += randint(1, 6)  
            if player1 > n:
                continue
                ## player 1 exceeded n, player 2 wins automatically, no need to continue with this hold_val
            else :
                ## player 2 rolls until they either beat player 1's score or exceed n
       
                player2 = 0
                while player2 < player1:
                    player2 += randint(1, 6)
                ## player 1 win - we'll assume ties go to player 1:
                if player2 >= n:
                    win_table[hold_val] += 1
                

    for item in win_table.keys():
        print("%d: %f" % (item, win_table[item] / 1000000))

if __name__ == "__main__":
    monte_carlo_approach(10)
