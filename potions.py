from lab8 import HashTableLP

list_of_potions = [

    # 3 ingredient potions
    [
        "Healing",
        ["Water", "Earth", "Water"],
        "This potion will heal any small cuts you have. If the user smells fresh morning dew, it's working."
    ],
    [
        "Speed",
        ["Air", "Fire", "Air"],
        "A sharp taste that gives a burst of speed. If you drink it too fast, you'll dash straight into a wall."
    ],
    [
        "Bravery",
        ["Fire", "Earth", "Fire"],
        "Warms your chest and boosts bravery immensely. This is perfect before you talk to your crush."
    ],
    [
        "Sleep",
        ["Water", "Air", "Earth"],
        "This brew helps you fall asleep peacefully. Be warned: it is not recommended while standing up."
    ],
    [
        "Glow",
        ["Fire", "Water", "Air"],
        "Makes your body glow faintly like a candle. This is great if the buyer needs to read in the dark."
    ],

    # 4 ingredient potions
    [
        "Night Vision",
        ["Air", "Water", "Air", "Fire"],
        "Helps you see in the dark effectively. Be aware that everything may look a little greenish."
    ],
    [
        "Fire Shield",
        ["Earth", "Water", "Fire", "Fire"],
        "This formula protects you from small burns. It is good for cooking dragons’ eggs—if you find any."
    ],
    [
        "Water Breathing",
        ["Water", "Water", "Air", "Earth"],
        "This elixir lets you breathe underwater for an extended period. The only side effect is slight fish-like burping."
    ],
    [
        "Focus",
        ["Earth", "Air", "Water", "Air"],
        "A clear liquid that clears your thoughts and keeps you focused. Students love this one during exams."
    ],
    [
        "High Jump",
        ["Air", "Fire", "Air", "Earth"],
        "Makes your jumps lighter and higher when consumed. Do not try jumping off roofs though."
    ],

    # 5 ingredient potions
    [
        "Strength",
        ["Earth", "Fire", "Earth", "Fire", "Water"],
        "This potion greatly boosts strength for a short time. You might accidentally crush cups, so be careful."
    ],
    [
        "Water Ward",
        ["Water", "Earth", "Water", "Air", "Water"],
        "Creates a swirling water shield around you when activated. This is perfect for rainy adventures."
    ],
    [
        "Fire Burst",
        ["Fire", "Fire", "Air", "Fire", "Water"],
        "Allows the user to release a small burst of flame from their hands. Keep away from curtains when using."
    ],
    [
        "Ultra Speed",
        ["Air", "Air", "Earth", "Air", "Fire"],
        "Lets you move with wind-like agility. People might hear whooshing noises when you walk."
    ],
    [
        "Lantern",
        ["Fire", "Water", "Air", "Water", "Air"],
        "Upon drinking, you summon a floating glowing orb that follows you around. A great night companion."
    ]
]

class Potions:
    def __init__(self, potion_name = "holder", ingredients = ["fire", "air", "air", "water"], description = "This potions heals wound."):
        self.potion_name = potion_name
        self.ingredients = ingredients
        self.description = description

    def potion_recipe(self):
        potion_catalog = HashTableLP()

        for x in range(len(list_of_potions)):
            potion = Potions()

            potion.potion_name = list_of_potions[x][0]
            potion.ingredients = list_of_potions[x][1]
            potion.description = list_of_potions[x][2]
            
            potion_catalog.put(potion.potion_name, potion)
        

        return potion_catalog