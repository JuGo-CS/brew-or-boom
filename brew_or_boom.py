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

#this function will just prints the list of potions (potions catalog)
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
    
    # will not exit on this part until the player inputs Y or y
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
    
# this function is for getting the player's action
def player_action():
    # will not exit/return unless the player's input is within the range
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

# this function is for getting the player's action if they are already inside of the brewing part
def player_brew_action():
    #will run definitely until valid input
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

#basicaclly returns a randomize potions to be pick by the 'buyer' in the game
def potion_randomizer():
    total_potions = game_difficulty #number of potions to be pick
    picked_entries = [] 
    # max_index = potion_catalog.size - 1
    
    #first will get all of the valid nodes (nodes that has value)
    valid_entries = []
    for entry in potion_catalog.array:
        if entry is not None:
            valid_entries.append(entry)

    # then proceeds to picking a randomize potion
    for i in range(total_potions):
        # index_picked = random.randint(0, len(potions.list_of_potions))
        random_entry = random.choice(valid_entries)
        # random_entry = potions.list_of_potions[index_picked]
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

#will undo the last ingredients added
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

#this function is for printing the valid ingredients (just to show to the player what should be the correct order/ingredients of that potion)
def game_validation(players_ingredients_queue, potions_ingredients):

    print(game_aesthetics.breaker)
    print(f"\n{BOLD}    Oh noooo!!! You make a big {UNDERLINED}MISTAKE{RESET}!")
    print(f"\n        Correct Potion's Ingredients {ITALIC}inorder{RESET}: ")
    counter = 1

    #basically prints the correct order of ingredients
    while not potions_ingredients.is_empty():
        item = potions_ingredients.dequeue()

        print(f"            [{counter}]{item}")
        counter += 1

    print(f"\n        Your Potion's Ingredients {ITALIC}inorder{RESET}: ")
    counter = 1

    #prints the player's ingredients
    while not players_ingredients_queue.is_empty():
        item = players_ingredients_queue.dequeue()

        print(f"            [{counter}]{item}")
        counter += 1

    print("\n" + game_aesthetics.breaker)
    time.sleep(5)

#this function is to check wether the ingredients is correct, will return the verdict
def check_correct_ingredients(players_ingredients_queue, potions_ingredients):
    is_same_ingredients = True

    if players_ingredients_queue.size != potions_ingredients.size:
        is_same_ingredients = False
        game_validation(players_ingredients_queue, potions_ingredients)
        

    else:
        # while not players_ingredients_queue.is_empty():
        # will iterate in the size of the ingredients of that potion
        for i in range(potions_ingredients.size):
            #this is the correct ingredients
            potions_ingredients_holder = potions_ingredients.dequeue() # will hold first the item 
            potions_ingredients.enqueue(potions_ingredients_holder)  # and push it also in our original SLL queue so that the value will not be remove, 
                                                                     # it will be stored at the back

            #this naman is the holder for the player's ingredients
            players_ingredients_queue_holder = players_ingredients_queue.dequeue()
            players_ingredients_queue.enqueue(players_ingredients_queue_holder)

            if potions_ingredients_holder != players_ingredients_queue_holder: # meaning mali ang ingredients, then set the checker to False
                is_same_ingredients = False

        #it means that the ingredients are not the same, we will print the correct and the player's version
        if not is_same_ingredients:
            game_validation(players_ingredients_queue, potions_ingredients)

    return is_same_ingredients

# this function is a bit heavy because this is the core function of the game
# this holds the logic on brewing a potion
# if the player choose to brew a potion, this function will be called. Then starts the process of making the potion
def brewing_potion(brew_inorder_potions):
    ingredients_queue = SLLQueue() # creates a SLLQueue to store the ingredients added by our player

    current_object = brew_inorder_potions.dequeue() # get the first potion to be brewed (nodes)
    current_potion = current_object.value #then get the value(the potion) in the node

    potions_ingredients = SLLQueue()
    # we need to store the correct order of the ingredients of the potion
    for ingredients in current_potion.ingredients:
        potions_ingredients.enqueue(ingredients)

    print(f"\n\n    Current Potion to be Brewed:\n        {BOLD}Potion of {UNDERLINED}{current_potion.potion_name}{RESET}\n")

    # loop for the brewing part of the potion
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
            
            is_ingredients_correct = check_correct_ingredients(ingredients_queue, potions_ingredients) #go to the checking of the ingredients if correct or nah

            if is_ingredients_correct:
                return True
            else:
                print("Correct ")

                return False

# will show this if the player succesfully brewed the customer's potion
# then after this, proceeds to next customer
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

#use to create a SLL queue of the potions to be brewed
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

game_aesthetics.game_start() # to start the animation (game aesthetics)
start_time = time.time()
time_difficulty_updated = start_time
game_difficulty = 1
TIME_INTERVAL = 120 #in second


if(game_aesthetics.game_proper()): #if the game starts
    game_over = False

    while(True):
        print(game_aesthetics.game_title)
        print(game_aesthetics.breaker)

        list_of_picked_entries = potion_randomizer() # will pick a random potions for the player to brew
        buyers_script = random.choice(buyer_scripts)
        game_aesthetics.animate_string(buyers_script, 1, 0.03)

        brew_inorder_potions = create_SLLQueue(list_of_picked_entries) # creates a SLL queue for the potions to brew
        print_potions_request(brew_inorder_potions) #prints the potions in order
        
        while(True):

            next_action = player_action() #will get the action of the player, wether to see the potions book or to brew a potion
                
            if next_action == 1: # View Potion's Book
                display_potion_catalog(potions.list_of_potions, brew_inorder_potions, buyers_script)

            elif next_action == 2: # Proceeds on brewing the potion
                succesfully_brewed_potion = brewing_potion(brew_inorder_potions) # will determine if tama ba yung potion na na-brew

                if succesfully_brewed_potion:

                    if brew_inorder_potions.is_empty(): # if wala ng next na potion,
                        proceeds()                      # continue to the next customer 'buyer'
                        os.system('cls')
                        break
                    
                    else: # if may laman pa, continue lang sa current buyer
                        os.system('cls')
                        print(game_aesthetics.game_title)
                        print(game_aesthetics.breaker)
                        print(buyers_script)
                        print_potions_request(brew_inorder_potions)

                elif not succesfully_brewed_potion: # if the brewed potion is not correct, then game over
                    game_over = True
                    break
                   

        if game_over:
            break
        
        # this line is for determining the current difficulty. This dictates how many potions the buyer will buy
        current_time = time.time()
        time_elapse = current_time - time_difficulty_updated
        if(time_elapse >= TIME_INTERVAL and game_difficulty < 3):
            time_difficulty_updated = current_time
            game_difficulty += 1



game_aesthetics.game_over() 


# list_of_picked_entries = potion_randomizer()

# for entry in list_of_picked_entries):
#     potion_object = entry.value 
    
#     print(f"Potion Name: {BOLD}{potion_object.potion_name}{RESET}")
    
#     print("Ingredients Required:")
#     for ingredient in potion_object.ingredients:
#         print(f"  - {ingredient}")
        
#     print(f"Description: {ITALIC}{potion_object.description}{RESET}")











