from potions import Potions
from lab8 import HashTableLP
import game_aesthetics
import time
import os

BOLD = '\033[1m'
FAINT = '\033[2m'
ITALIC = '\033[3m' 
CYAN = '\033[36m'
RED = '\033[31m'
RESET = '\033[0m'
UNDERLINED = '\033[4m'


action_list = f"""{BOLD}
    ╦ ╦┌─┐┬ ┬┬─┐  ╔═╗┌─┐┌┬┐┬┌─┐┌┐┌
    ╚╦╝│ ││ │├┬┘  ╠═╣│   │ ││ ││││o
     ╩ └─┘└─┘┴└─  ╩ ╩└─┘ ┴ ┴└─┘┘└┘o
        [1] Potion's Book
        [2] Brew Potion
        [3] Give it to Customer{RESET}
    
"""

brew_potion_list = f"""{BOLD}
    ╦ ╦┌─┐┬ ┬┬─┐  ╔╦╗┌─┐┬  ┬┌─┐
    ╚╦╝│ ││ │├┬┘  ║║║│ │└┐┌┘├┤ o
     ╩ └─┘└─┘┴└─  ╩ ╩└─┘ └┘ └─┘o
        [1] Add Ingredient
        [2] Undo Move
        [3] View Potion's Details
        [4] Finish Brewing{RESET}
        
"""

def player_action():
    while(True):
        print(action_list)
        players_input = int(input(f"{CYAN}Input their correspoding value: {RESET}"))

        if players_input >= 1 and players_input <= 3:
            break
    
    return players_input

def player_brew_action():
    while(True):
        print(brew_potion_list)
        players_brew_input = int(input(f"{CYAN}Input their correspoding value: {RESET}"))

        if players_brew_input >= 1 and players_brew_input <= 4:
            break
    
    return players_brew_input



potion_instance = Potions()
potion_catalog = potion_instance.potion_recipe()

game_aesthetics.game_start()








