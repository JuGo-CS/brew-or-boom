import time
import os

#for game aesthetics
BOLD = '\033[1m'
FAINT = '\033[2m'
ITALIC = '\033[3m' 
CYAN = '\033[36m'
RED = '\033[31m'
RESET = '\033[0m'
UNDERLINED = '\033[4m'

game_title = r"""

$$$$$$$\                                                                    $$$$$$$\                                    
$$  __$$\                                                                   $$  __$$\                                   
$$ |  $$ | $$$$$$\   $$$$$$\  $$\  $$\  $$\        $$$$$$\   $$$$$$\        $$ |  $$ | $$$$$$\   $$$$$$\  $$$$$$\$$$$\  
$$$$$$$\ |$$  __$$\ $$  __$$\ $$ | $$ | $$ |      $$  __$$\ $$  __$$\       $$$$$$$\ |$$  __$$\ $$  __$$\ $$  _$$  _$$\ 
$$  __$$\ $$ |  \__|$$$$$$$$ |$$ | $$ | $$ |      $$ /  $$ |$$ |  \__|      $$  __$$\ $$ /  $$ |$$ /  $$ |$$ / $$ / $$ |
$$ |  $$ |$$ |      $$   ____|$$ | $$ | $$ |      $$ |  $$ |$$ |            $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ | $$ | $$ |
$$$$$$$  |$$ |      \$$$$$$$\ \$$$$$\$$$$  |      \$$$$$$  |$$ |            $$$$$$$  |\$$$$$$  |\$$$$$$  |$$ | $$ | $$ |
\_______/ \__|       \_______| \_____\____/        \______/ \__|            \_______/  \______/  \______/ \__| \__| \__|                                                                                                                                                                                                                    
"""

game_witch = r"""    
    ................................................................@%%%@.........................................
    .:::::::::::::::::::::::::::::::::::::::::::::::::::::.......@@@@%%%@@@@@@...::::::::::::::::::::::::::::::::.
    .:::::::::::::::::::::::::::::::::::::::::::::::::::....=@@@@@@%@@@@@@@@@@@@:::::::::::::::::::::::::::::::::.
    .::::::::::::::::::::::::::::::::::::::::::::::::::...@@@@@@@@@@@%@@....@%@..::::::::::::::::::::::::::::::::.
    .:::::::::::::::::::::::::::::::::::::::::::::::::..@@@@@@@@@%%%@@@....@@@@.:....::::::::::::::::::::::::::::.
    .:::::::::::::::::::::::::::::::::::::::::::::::...@@@@@@@@@@@@@@%@@:...@@@@@#@@.::::::::::::::::::::::::::::.
    .:::::::::::::::::::::....:::::::::::::::::::::...@@%###%%%%%######@@.......@@-..::::::::::::::::::::::::::::.
    .:::::::::::::::::::::..@...::::::::::::::::::...@@@@@@@@@@@@@@@@@@@@@...:......:::::::::::::::::::::::::::::.
    .:::::::::::::::::::::..@@...::::::::::........#@@@@@@@@@@@@@@@@@@@@@@@........::::::::::::::::::::::::::::::.
    .::::::::::::::::::::::..@@+..:::.....::..@@@@@@@+**#%@@@@@@@@@@%****+@@@@@*..:.....:::::::::::::::::::::::::.
    .::::::::::::::::::::....@%@@.......#@@@@@@@@@@@@@@@@@@*...:.:#@@@@@@@@@@@@@@@@@@......::::::::::::::::::::::.
    .::::::::::::::::::....%@@@@....@@@@@@@@@@+@@@@....-=--=@+==@-+-=-....@@@@%.@@@@@@@@@+..:::::::::::::::::::::.
    .:::::::::::::::::...@@@@@@....@@@@@@@@@@@..@=.:-@...@.@=:+:.@+.@..@::-.@-..@@@@@@@@@@:.::::::::::::::::::::::
    .::::::::::::::::..@@@##@...:.:..::..@@@@@@.@@@--@@.:+..@@+#@@.:+..@.-@@@:.@@@@-.....=..::::::::::::::::::::::
    .::::::::::::::::.*@%**#:...::.....@@......@....==#@@@@@@....@*@@@@*=:....@@@...:....@....:::::::::::::::::::.
    .::::::::::::::::..@@%*#@@.....@:..@@@@@@@@@@@@:+*+-:@::@@@@@.:-@:=+*.@@@@@%@@@@@..@@@..%.:::::::::::::::::::.
    .:::::::::::::::::..-@@**@@@....@...=@@@@@@@%%@%.**@@@@:......+%@@@*=.@#%%%%@@@@@@@@@@.@@::::::::::::::::::::.
    :::::::::::::::::::...@****@@...@@@....@@@@@@@@@.:=-.:==@@@@@@+=-:=-.=@@@@@@@@@@@@..:*@@..:::::::::::::::::::.
    .::::::::::::::::....+@****@@....@@@@@@@@@%@@@@@@:.:+**+:.:..-+***:.%@@#%%%%%%%%%@@@@@@...:::::::::::::::::::.
    .::::::::::::::....@@@#**@@@...=:..@@@@@@@@@%%%%@@@..:.:+*****-....@@@%@@@@@@@@@%%%%%@@......:::::::::::::::::
    .:::::::::::::..#@@@***#@@....+=.....:...@%%%@@@%@@@@@@*.......@@@@@@@%@@@@@@@%%@@@@@%@@@@@....:::::::::::::::
    .:::::::::::::.#@#*****%.....@@..:::...@@@@@@@@@@%@@##%@@@@@@@@@####@%%@@@@@@@@@%%%@@@@@%@@@@...:::::::::::::.
    .:::::::::::::.@@#*****%@...@@@.......@@@@@%%%%@@%%@%@@#%@%%%@##@@%@%%@@@@@@@%%%@@###%%%%@%%@@@...:::::::::::.
    .:::::::::::::..@@@@@%#*@@@.@@@@@...+@@@@@@#@@%@@@%%@%%%%%@%@%%%%%@@%@@@@@@@@@%%##@@@@@@@@@@@%@@..:::::::::::.
    .:::::::::::::.....*%@@@%*@@.....-*=.%@@###@@*########%%%%#@%%@@@@@@@@@@@%%%%@@@@@###%%%%@@@@@%@@.:::::::::::.
    .::::::::::::::::.......---@:@@@@@@@@..@@@@@@@@@@@@@@@@@@@####%%@@@@@%@@@@@@@@...@@%@@@@@@@@%@@@@.:::::::::::.
    .::::::::..::::::..@@@@@@..@@@=.::--#+..+--====-::-=#@@@@@@@@@@%@@@@%@@-...:..-*-.@%@@@@@%@@@@@...:::::::::::.
    .::::::.....:...:..@@@@@@@@@@@*:...........:......:=*@@@@@@@@@@@@@%#@@:@@@@:==*+=.@%%%@@@@@%.....::::::::::::.
    .::::::.@@@@@@@.....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@%...@..@...=.@%@@@@.:....:::::::::::::::.
    .::::::.@@@@+.:%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.:...*@@..@.-@@@@@%%#@...:::::::::::::::::::.
    .::::::...:.#@@@@+....@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@...:.@@@@@:.:@@@@@@%%@@@%@..:::::::::::::::::::::
    .::::::::.........@@@.@@@@@@@@@@@@@@@@@@.@@@@@@@@@@@@@@@@@@@+.@@@@@#%%@@@@@###%%@@@@@%@@:.:::::::::::::::::::.
    .::::::::::::::.:@@@@@@@@@@@@@@@@@@@@@@@...@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@..:::::::::::::::::::.
    .:::::::::::::.:.@@@@@@@@@@@@@@@@@@@@@@@.=.@@@@@@@@@@@@@@@@@@@@@@#%@@@@@@@@@@@@@@@@@@@%@..:::::::::::::::::::.
    ::::::::::::::..@@@@@@@@@@@@@@@@@.@@@@@.-=.@@@%@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@%@..:::::::::::::::::::.
    .:::::::::::::..@@@@@@@@@@@@@@@@:.@@@-.=*=.@@@@.@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@%@..:::::::::::::::::::.
    .:::::::::::::.-@@@@@@@@@@@@@@@..@@@@.=**+.@@@...@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@%@=.:::::::::::::::::::.
    .:::::::::::::..@@@@@@@@@@@.@@@..%@@.=****-...:+.@@@@.@@@@@@@@@@@@#@@@@@@@@@@@@@@@@@@@%@@.:::::::::::::::::::.
    .:::::::::::::..@@@@@@@@@@@:@@@.=..@:***********.@@@@..@@@@@@@@@@%##%%##%%%%%%@@@@#@@@@@@.:::::::::::::::::::.
    .:::::::::::::::.@@@@@@@@@%..@@:*+---***********:.@....@@@@@@@@@@@@@@@@@@%@@@%@@.@@@.*@@:....::::::::::::::::.
    .:::............:..@@@@@@@@.:..-****************+-::=..@@@@@@@@.....@@@@@@@@@@@........:@@@:.:........:...:::.
    .:......@@@@@@@@@@@@@@@@@@@...-********************-..@@@@@@@......@@@@@@@@@@@@@@@@..:...:.#@@@@@@@@@@@.....:.
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.....................:@@@@@@@-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    :.:@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:.:
    ....................-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:.......:.......:..:..
"""

breaker = "------------------------------------------------------------------------------------------------------------------------"

game_intro_story = f"""

                In the quiet village of {BOLD}{ITALIC}Apitong{RESET}, you lived a peaceful life with your mother.
                She was the village’s Head Witch, known for her potions that healed, protected, and 
                helped everyone. Her little shop was the heart of Apitong, without her potions, the 
                villagers would struggle.

                Every morning, she brewed remedies. Every night, she taught you small spells.
                Life was calm… until everything changed.

                One day, an {RED} unexplainable magical accident {RESET} struck the shop.
                A strange burst of energy filled the air, and your mother fell terribly ill.
                No healer, no spell, no potion could save her.

                Before she passed, she placed your hands on the old wooden counter and whispered:

                {CYAN}{ITALIC}“The village needs you now. Take care of the shop… and be careful with the recipes.” {RESET}

                {FAINT}And just like that, you became the new keeper of the potion shop. {RESET}

                Now it’s your turn to brew the potions Apitong depends on.
                With only four basic ingredients, {ITALIC}Earth, Water, Fire, and Air,{RESET} and your mother’s old 
                recipe book, you must keep the shop running.

                Customers will come. Requests will grow.
                And you must mix each potion in the exact order…
                or the whole shop might explode.

                Your story begins here.
                {BOLD}Welcome to {ITALIC} Apitong’s Potion Shop. {RESET}

"""

tips = f"""
                {RED}Please remember:{RESET}
                    {BOLD}Your safety{BOLD} always comes first.
                    Some customers might be impatient, but it’s okay if you not ready yet. 
                    A wrong brew can be dangerous… and very explosive. It will {RED}{ITALIC}kill{RESET} you.

                    Always follow each recipe {ITALIC}{CYAN}{UNDERLINED}STEP BY STEP{RESET}.
                    Your mother left you her old Potion Book, filled with the proper ingredient
                    orders. Whenever you feel unsure, open the book and check the recipes carefully.

                    Take your time.
                    Brew wisely.
                    And trust yourself.
                    Every great witch started somewhere. ⭐

                    {FAINT}Good luck, young potion keeper.{RESET}
    """

game_guide_customer = f"""
    {CYAN}“Hello there! I would like to buy a Potion of Invisibility, please!”{RESET}
"""

game_guide_starting = f"""
    {ITALIC}This is your {BOLD}first customer.{RESET}
    To help them, you need to brew the potion they requested."
    Remember: in Apitong’s Potion Shop, the order of ingredients is very 
    important. One wrong step… and things might {RED}explode and kill you{RESET}.",

    Let’s take things slowly, yes? Ready? Please read the guide below.


"""

game_guide = f"""
    ╔═╗  ╔═╗  ╔╦╗  ╔═╗      ╔═╗  ╦ ╦  ╦  ╔╦╗  ╔═╗
    ║ ╦  ╠═╣  ║║║  ║╣       ║ ╦  ║ ║  ║   ║║  ║╣ 
    ╚═╝  ╩ ╩  ╩ ╩  ╚═╝      ╚═╝  ╚═╝  ╩  ═╩╝  ╚═╝
    ---------------------------------------------------------------------------------

    When a customer asks for a potion, your first step is to check the Potion’s Book.
    You'll see these options:
        {ITALIC}{FAINT}
        ╦ ╦┌─┐┬ ┬┬─┐  ╔═╗┌─┐┌┬┐┬┌─┐┌┐┌
        ╚╦╝│ ││ │├┬┘  ╠═╣│   │ ││ ││││o
         ╩ └─┘└─┘┴└─  ╩ ╩└─┘ ┴ ┴└─┘┘└┘o
            [1] Potion's Book
            [2] Brew Potion
            [3] Give it to Customer {RESET}
    
            
    For now, let's focus on Potion’s Book.

    In the {BOLD}"Potion’s Book{RESET}, look for the potion the customer wants.
    Here, they want Invisibility, so find the recipe for it and study 
    the ingredients in {BOLD}{UNDERLINED}EXACT ORDER.{RESET}

    After checking the ingredients, go back to the menu and choose Brew Potion.

    Inside Brew Potion, you will find these options:
        {ITALIC}{FAINT}
        ╦ ╦┌─┐┬ ┬┬─┐  ╔╦╗┌─┐┬  ┬┌─┐
        ╚╦╝│ ││ │├┬┘  ║║║│ │└┐┌┘├┤ o
         ╩ └─┘└─┘┴└─  ╩ ╩└─┘ └┘ └─┘o
            [1] Add Ingredient
            [2] Undo Move
            [3] View Potion's Details
            [4] Finish Brewing {RESET}
 
            
    Here’s what each one does:

        ⭐ {BOLD}{UNDERLINED}Add Ingredients{RESET}
        Lets you add an ingredient to the cauldron.
        Since we’re making Invisibility, choose Add, 
        then pick the correct ingredient. One step at a time.

        ----------------------------------------------------------------

        ⭐ {BOLD}{UNDERLINED}Undo Move{RESET}
        If you misclicked or added the wrong ingredient, don’t panic.
        Choose Undo to remove the last ingredient you added.

        ----------------------------------------------------------------

        ⭐ {BOLD}{UNDERLINED}View Potion's Details{RESET}
        If you forget the steps, you can always choose View to check the 
        ingredients again. Just type the potion’s name.

            {ITALIC}For example:
                View: Invisibility{RESET}

        It will show the ingredient list and its description.
        Important: Only type the main name of the potion.
        If the potion is {BOLD}Potion of Healing{RESET}, type only: {BOLD}Healing{RESET}

        ----------------------------------------------------------------

        ⭐ {BOLD}{UNDERLINED}Finish Brewing{RESET}
        Choose this once you have added all ingredients correctly.
        This will give the finished potion to the customer.

        If the customer only wants one potion, you may now choose 
        Finish to end the transaction.

        If they want multiple potions, simply repeat the same steps 
        for each one.
"""


"""
    This function is dynamic. It can be use to apply animation for strings.

    type_of_animation is either "line_by_line" = [0] or "char_by_char" = [1]
    Can also use the blinking feature
"""

def animate_string(string, type_of_animation = 0, delay = 0.1, blinking = 0):
            
    if type_of_animation == 0: #[0] means type of animation is line by line
        string_as_list = string.strip().split('\n')
        for i in range(len(string_as_list)):
            # Clear terminal before drawing the next frame
            os.system('cls')
            
            # Select lines from the start up to and including the current line (i)
            lines_to_print = string_as_list[:i + 1]
            
            # Print the accumulating lines (from the start to i)
            for line in lines_to_print:
                print(line)

            time.sleep(delay)

    elif type_of_animation == 1: #[1] means type of animation is character by character
        for char in string:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()


    #if blinking is enable, it will run through this (blinks the string n times ~ depends on how many it is)
    if blinking > 0:
        for i in range(blinking):
            os.system('cls')
            time.sleep(delay)

            print('\n'.join(string_as_list))
            time.sleep(delay)

def game_start():
    animate_string(game_title, type_of_animation = 0, delay = 0.4, blinking = 3)
    print(game_witch)
    time.sleep(3)

    os.system('cls')
    print(game_title)
    print(breaker)
    animate_string(game_intro_story, 1, 0.03)
    print(breaker)
    time.sleep(3)

    os.system('cls')
    print(game_title)
    print(breaker)
    print(tips)
    print(breaker)

    time.sleep(8)
    os.system('cls')
    print(game_title)
    print(breaker + "\n")
    animate_string(game_guide_customer, type_of_animation = 1, delay = 0.03)
    time.sleep(2)
    animate_string(game_guide_starting, type_of_animation = 1, delay = 0.03)
    time.sleep(2)

    print(game_guide)

def game_proper():
    print(game_title)
    print(game_guide)
    while(True):
        player_input = input("Proceeds to Game[Y/y]: ")

        if(player_input == 'Y' or player_input == 'y'):
            break

        else:
            print(f"{FAINT}{ITALIC}     I don't quite get it!{RESET}")
    
    return True