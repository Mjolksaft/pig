"""
Welcome to the pig dice game!.

here are the rules:
Each turn, a player repeatedly rolls a die until
either a 1 is rolled or the player decides to "hold"
if a player rolls a one they score nothing
if a player rolls any other number their points gets
added to the total and they may roll again
if a player decides to hold their turn they add their points to the score

first player to 20 points win

to start write "start player_name player_name... "
if you leave the second arugment empty a bot will replace it
"""

import command

if __name__ == "__main__":

    print(__doc__)
    command.Command().cmdloop()
