from potions import Potions
from lab3 import SLLQueue
import game_aesthetics
import random
import time
import potions
import os


BOLD = '\033[1m'
FAINT = '\033[2m'
ITALIC = '\033[3m' 
CYAN = '\033[36m'
RED = '\033[31m'
RESET = '\033[0m'
UNDERLINED = '\033[4m'

congratulations = f"""
    ╔═╗╔═╗╔╗╔╔═╗╦═╗╔═╗╔╦╗╦ ╦╦  ╔═╗╔╦╗╦╔═╗╔╗╔╔═╗ ┬┬┬
    ║  ║ ║║║║║ ╦╠╦╝╠═╣ ║ ║ ║║  ╠═╣ ║ ║║ ║║║║╚═╗ │││
    ╚═╝╚═╝╝╚╝╚═╝╩╚═╩ ╩ ╩ ╚═╝╩═╝╩ ╩ ╩ ╩╚═╝╝╚╝╚═╝ ooo

    You've correctly brew all of the potion!
    {CYAN}{ITALIC}>Thank you very much for brewing this Potion!{RESET}
"""

action_list = f"""
    ╦ ╦┌─┐┬ ┬┬─┐  ╔═╗┌─┐┌┬┐┬┌─┐┌┐┌
    ╚╦╝│ ││ │├┬┘  ╠═╣│   │ ││ ││││o
     ╩ └─┘└─┘┴└─  ╩ ╩└─┘ ┴ ┴└─┘┘└┘o
        [1] Potion's Book
        [2] Brew Potion
"""

brew_potion_list = f"""
    ╦ ╦┌─┐┬ ┬┬─┐  ╔╦╗┌─┐┬  ┬┌─┐
    ╚╦╝│ ││ │├┬┘  ║║║│ │└┐┌┘├┤ o
     ╩ └─┘└─┘┴└─  ╩ ╩└─┘ └┘ └─┘o
        [1] Add Ingredient
        [2] Undo Move
        [3] View Current Ingredients
        [4] Finish Brewing
"""

ingredients_list = f"""
    ╦┌┐┌┌─┐┬─┐┌─┐┌┬┐┬┌─┐┌┐┌┌┬┐┌─┐
    ║││││ ┬├┬┘├┤  │││├┤ │││ │ └─┐o
    ╩┘└┘└─┘┴└─└─┘─┴┘┴└─┘┘└┘ ┴ └─┘o
        [1] Water
        [2] Earth
        [3] Fire
        [4] Air
"""

buyer_scripts = [
    f"{CYAN}   >Hello there! Lovely weather today, isn’t it?\n    Could I buy this potion, please?{RESET}",
    f"{CYAN}   >Good day! I hope I’m not bothering you.\n    I’d like to buy a potion, this one right here.{RESET}",
    f"{CYAN}   >Hi! I heard your shop is open again.\n    May I get this potion? I really need it.{RESET}",
    f"{CYAN}   >Hello! I’m passing through the village.\n    Could I buy one of your potions?{RESET}",
    f"{CYAN}   >Greetings! I was told you’re the new owner.\n    May I purchase this potion, please?{RESET}",
    f"{CYAN}   >Ah, perfect timing! I really need a potion today.\n    Can I get this one right here?{RESET}",
    f"{CYAN}   >Hey there! I’m having a rough day.\n    Mind selling me this potion?{RESET}",
    f"{CYAN}   >Good afternoon! I’ve been looking for this potion.\n    Can I buy it from you?{RESET}",
    f"{CYAN}   >Hi! Sorry to rush, but I need a potion quickly.\n    Could I have this one?{RESET}",
    f"{CYAN}   >Hello again! Your potions always help.\n    May I buy this one today?{RESET}"
]

potion_catalog_string = f"""
╔═╗╔═╗╔╦╗╦╔═╗╔╗╔  ╔═╗╔═╗╔╦╗╔═╗╦  ╔═╗╔═╗
╠═╝║ ║ ║ ║║ ║║║║  ║  ╠═╣ ║ ╠═╣║  ║ ║║ ╦
╩  ╚═╝ ╩ ╩╚═╝╝╚╝  ╚═╝╩ ╩ ╩ ╩ ╩╩═╝╚═╝╚═╝"""

def display_potion_catalog(catalog, original_queue,  buyers_script):
    print(potion_catalog_string)
    print("\n" + "-"*40 + "\n")
    # Iterate through each potion entry in the main list
    for potion_data in catalog:
        # Unpack the list into meaningful variables
        name = potion_data[0]
        ingredients_list = potion_data[1]
        description = potion_data[2]

        # Print the Potion Name with BOLD and UNDERLINED styles
        print(f"{BOLD}{UNDERLINED}Potion of {name}{RESET}")
        print("    Ingredients:")

        # Iterate through the ingredients list using enumerate for the numbered index
        for index, ingredient in enumerate(ingredients_list):
            # index + 1 makes the numbering start at [1] instead of [0]
            print(f"        [{index + 1}] {ingredient}")

        # Print the description with indentation
        print(f"    Description: {description}")
        print("\n" + "-"*40 + "\n")
    
    while(True):
        player_input = input("Close the Potion's Catalog[Y/y]: ")

        if(player_input == 'Y' or player_input == 'y'):
            break

        else:
            print(f"{FAINT}{ITALIC}     I don't quite get it!{RESET}")
    os.system('cls')
    print(game_aesthetics.game_title)
    print(game_aesthetics.breaker)
    print(buyers_script)
    print_potions_request(original_queue)
    
def player_action():
    while(True):
        print(action_list)
        try:
            players_input = int(input(f"{ITALIC}Input their corresponding value: {RESET}"))

            if 1 <= players_input <= 3:
                break 
            else:
                print(f"{RED}Invalid input: Please enter a number between 1 and 3.{RESET}")
        
        except ValueError:
            print(f"{ITALIC}     I don't quite get it!{RESET}")
    
    return players_input

def player_brew_action():
    while(True):
        print(brew_potion_list)

        try:
            players_brew_input = int(input(f"{ITALIC}Input their correspoding value: {RESET}"))

            if 1 <= players_brew_input <= 4:
                break
            else:
                print(f"{RED}Invalid input: Please enter a number between 1 and 4.{RESET}")
            
        except ValueError:
            print(f"{ITALIC}     I don't quite get it!{RESET}")
    
    return players_brew_input

def potion_randomizer():
    total_potions = game_difficulty
    picked_entries = [] 
    max_index = potion_catalog.size - 1
    
    valid_entries = []
    for entry in potion_catalog.array:
        if entry is not None:
            valid_entries.append(entry)

    for i in range(total_potions):
        random_entry = random.choice(valid_entries)
        picked_entries.append(random_entry)
    
    return picked_entries

def print_potions_request(original_queue):
    print("\n    -----------------------------------------\n        Potion's needed to brew:")
    counter = 1
    
    temp_queue = SLLQueue()
    
    # Iterate while the original stack is not empty
    while not original_queue.is_empty():
        # Pop the Entry object from the top of the stack
        entry_object = original_queue.dequeue()
        
        # Access the Potion object value from the Entry object
        potion_object = entry_object.value 
        
        # Print using your requested formatting
        print(f"            [{counter}] Potion of {BOLD}{UNDERLINED}{potion_object.potion_name}{RESET}")
        
        # Push the item onto the temporary stack to preserve order
        temp_queue.enqueue(entry_object)
        counter += 1

    # Restore the original stack using the temporary stack
    while not temp_queue.is_empty():
        original_queue.enqueue(temp_queue.dequeue())

    print("    -----------------------------------------\n")

#this function is to ensure that the added ingredients are correct (within the scope of of the lists)
def adding_ingredients():
    while(True): 
        print(ingredients_list)
        try:
            players_input = int(input(f"{ITALIC}Input their corresponding value: {RESET}"))

            if 1 <= players_input <= 4:
                break 
            else:
                print(f"{RED}Invalid input: Please enter a number between 1 and 4.{RESET}")
        
        except ValueError:
            print(f"{ITALIC}     I don't quite get it!{RESET}")
    
    return_ingredients = "Holder"

    if players_input == 1:
        return_ingredients = "Water"

    elif players_input == 2:
        return_ingredients = "Earth"

    elif players_input == 3:
        return_ingredients = "Fire"

    elif players_input == 4:
        return_ingredients = "Air"
    
    return return_ingredients

def undo_ingredients(ingredients_queue):
    temp_queue = SLLQueue()

    while ingredients_queue.size - 1 > 0:
        temp_queue.enqueue(ingredients_queue.dequeue())
    
    ingredients_queue.dequeue() #so that we can remove the last that we added ~implement the undo in SLL Queue

    while not temp_queue.is_empty():
        ingredients_queue.enqueue(temp_queue.dequeue())

#just prints the current ingredients being added
def print_current_ingredients(current_ingredients):

    temp_queue_ingredients = SLLQueue()
    print(f"\n{CYAN}-------------------------------------------------{RESET}")
    print(f"    Added Ingredients {ITALIC}(in order){RESET}:")
    while not current_ingredients.is_empty():
        current_object_ingredient = current_ingredients.dequeue()
        # current_potion_ingredient = current_object_ingredient.value

        # print(f"    >{current_potion_ingredient}") current_object_ingredient
        print(f"        >{current_object_ingredient}")

        temp_queue_ingredients.enqueue(current_object_ingredient)
    
    while not temp_queue_ingredients.is_empty():
        current_ingredients.enqueue(temp_queue_ingredients.dequeue())
    print(f"{CYAN}-------------------------------------------------{RESET}\n")

#this function is to check wether the ingredients is correct, will return the verdict
def check_correct_ingredients(ingredients_queue, potions_ingredients):
    is_same_ingredients = True

    if ingredients_queue.size != potions_ingredients.size:
        is_same_ingredients = False

    else:
        while not ingredients_queue.is_empty():
            if ingredients_queue.dequeue() != potions_ingredients.dequeue():
                is_same_ingredients = False

    return is_same_ingredients

def brewing_potion(brew_inorder_potions):
    ingredients_queue = SLLQueue()

    current_object = brew_inorder_potions.dequeue()
    current_potion = current_object.value

    potions_ingredients = SLLQueue()
    for ingredients in current_potion.ingredients:
        potions_ingredients.enqueue(ingredients)

    print(f"\n\n    Current Potion to be Brewed:\n        {BOLD}Potion of {UNDERLINED}{current_potion.potion_name}{RESET}\n")

    while(True):
        brew_action = player_brew_action()
        if brew_action == 1:    # player want's to add 
            ingredients_queue.enqueue(adding_ingredients())

        elif brew_action == 2:  # player's want to undo the added ingredient
            if ingredients_queue.is_empty():
                print(f"{ITALIC}    Your currently have no added ingredients in your cauldron!{RESET}")
            else:
                undo_ingredients(ingredients_queue)
        
        elif brew_action == 3: # player can see the current added ingredients of the potion (inorder)
            if ingredients_queue.is_empty():
                print(f"{ITALIC}Your currently have no added ingredients in your cauldron!{RESET}")
            else:
                print_current_ingredients(ingredients_queue)
        
        elif brew_action == 4: # player choosing to finish brewing of the current potion
            is_ingredients_correct = check_correct_ingredients(ingredients_queue, potions_ingredients)

            if is_ingredients_correct:
                return True
            else:
                return False

def proceeds():
    os.system('cls')
    print(game_aesthetics.game_title)
    print(game_aesthetics.breaker)
    print(congratulations)
    while(True):
        player_input = input("Proceeds to next customer?[Y/y]: ")

        if(player_input == 'Y' or player_input == 'y'):
            break

        else:
            print(f"{FAINT}{ITALIC}     I don't quite get it!{RESET}")
    os.system('cls')


def create_SLLQueue(list_of_picked_entries):
    object_SLLQueue= SLLQueue()

    for entry in list_of_picked_entries:
        object_SLLQueue.enqueue(entry)
    
    return object_SLLQueue



# GAME LOGIC FLOW 
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

potion_instance = Potions()
potion_catalog = potion_instance.potion_recipe()

game_aesthetics.game_start()
start_time = time.time()
time_difficulty_updated = start_time
game_difficulty = 1
TIME_INTERVAL = 120 #in second


if(game_aesthetics.game_proper()):
    game_over = False

    while(True):
        print(game_aesthetics.game_title)
        print(game_aesthetics.breaker)

        list_of_picked_entries = potion_randomizer()
        buyers_script = random.choice(buyer_scripts)
        game_aesthetics.animate_string(buyers_script, 1, 0.03)

        brew_inorder_potions = create_SLLQueue(list_of_picked_entries)
        print_potions_request(brew_inorder_potions)
        
        while(True):

            next_action = player_action()
                
            if next_action == 1: # View Potion's Book
                display_potion_catalog(potions.list_of_potions, brew_inorder_potions, buyers_script)

            elif next_action == 2: # Proceeds on brewing the potion
                succesfully_brewed_potion = brewing_potion(brew_inorder_potions)

                if succesfully_brewed_potion:

                    if brew_inorder_potions.is_empty():
                        proceeds()
                        os.system('cls')
                        break
                    
                    else:
                        os.system('cls')
                        print(game_aesthetics.game_title)
                        print(game_aesthetics.breaker)
                        print(buyers_script)
                        print_potions_request(brew_inorder_potions)
                elif not succesfully_brewed_potion:
                    game_over = True
                    break
                   

        if game_over:
            break
        
        current_time = time.time()
        time_elapse = current_time - time_difficulty_updated
        if(time_elapse >= TIME_INTERVAL and game_difficulty < 3):
            time_difficulty_updated = current_time
            game_difficulty += 1

    # os.system('cls')
    print("Game Over!")        































# list_of_picked_entries = potion_randomizer()

# for entry in list_of_picked_entries):
#     potion_object = entry.value 
    
#     print(f"Potion Name: {BOLD}{potion_object.potion_name}{RESET}")
    
#     print("Ingredients Required:")
#     for ingredient in potion_object.ingredients:
#         print(f"  - {ingredient}")
        
#     print(f"Description: {ITALIC}{potion_object.description}{RESET}")











