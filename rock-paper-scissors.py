# Rock-paper-scissors-lizard-Spock Mini project

import random
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


# functions

def number_to_name(number):
    
    if number == 0:
        return "rock"
    
    elif number == 1:
        return "Spock"

    elif number == 2:
        return "paper"

    elif number == 3:
        return "lizard"

    elif number == 4:
        return "scissors"

    else:
        print "inappropriate number choice!"


def name_to_number(name):
    
    if name == "rock":
        return 0

    elif name == "Spock":
        return 1

    elif name == "paper":
        return 2

    elif name == "lizard":
        return 3

    elif name == "scissors":
        return 4

    else:
        print "inappropriate choice"        

def rpsls(name): 

    # converting name to player_number using name_to_number
    player_number = name_to_number(name)
    print "player chooses " + name

    # computing random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,4)
    comp_choice = number_to_name(comp_number)
    print "computer chooses " + comp_choice
   
    # computing difference of player_number and comp_number modulo five
    dif = (player_number - comp_number) % 5
    
    # using if/elif/else to determine winner

    if dif == 1 or dif == 2:
        print "player wins !"
        print ""
        
    elif dif == 3 or dif == 4:
        print "computer wins !"
        print ""
                
    else:
        print "none wins - its a tie !"
        print ""
        
        
# testing the code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
