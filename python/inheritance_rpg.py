#TUAZON, Francesca Marie A. (BCS14)

import random

#superclass --------------------------------------
class Humanoid:
    strength = random.randint(1, 18)
    dexterity = random.randint(1, 18)
    constitution = random.randint(1, 18)
    intelligence = random.randint(1, 18)
    wisdom = random.randint(1, 18)
    charisma = random.randint(1, 18)
    _sleep_resistance = 100 #for elves
    _magic_resistance = 20 #for dwarves

    def __init__(self, height_input, weight_input, hairColor_input, eyeColor_input):
        #user choice
        self.height_input = height_input
        self.weight_input = weight_input
        self.hairColor_input = hairColor_input
        self.eyeColor_input = eyeColor_input

    def randomize_attributes(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        print("\nThese are your random attributes:")
        print(f"Strength: {strength}"
              f"\nDexterity: {dexterity}"
              f"\nConstitution: {constitution}"
              f"\nIntelligence: {intelligence}"
              f"\nWisdom: {wisdom}"
              f"\nCharisma: {charisma}")


#subclass --------------------------------------
class Humans(Humanoid): #+2 to any attribute (user choice)
    strength = Humanoid.strength
    dexterity = Humanoid.dexterity
    constitution = Humanoid.constitution
    intelligence = Humanoid.intelligence
    wisdom = Humanoid.wisdom
    charisma = Humanoid.charisma

    def choose_attribute(self):
        choice = input("\nWhich attribute would you like to add the +2 points to? (strength, dexterity, constitution, intelligence, wisdom, charisma): ")
        if choice.lower() == "strength":
            Humans.strength +=2
        if choice.lower() == "dexterity":
            Humans.dexterity +=2
        if choice.lower() == "constitution":
            Humans.constitution +=2
        if choice.lower() == "intelligence":
            Humans.intelligence +=2
        if choice.lower() == "wisdom":
            Humans.wisdom += 2
        if choice.lower() == "charisma":
            Humans.charisma +=2

class Elves(Humanoid): #100% resistance to sleep ; +2 dexterity/charisma
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma, _sleep_resistance):
        super.__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma, _sleep_resistance)

    def elves_bonus(self):
        Humanoid.dexterity += 2
        Humanoid.charisma += 2

class Dwarves(Humanoid): #20% resistance to magic ; +2 strength/constitution ; -2 charisma
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma, _magic_resistance):
        super.__init__(height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma, _magic_resistance)

    def dwarves_bonus(self):
        Humanoid.strength += 2
        Humanoid.constitution += 2
        Humanoid.charisma -= 2

#function --------------------------------------
def characterCreation():
    print("Welcome to the Falls of Eternity. This is a simple RPG simulator written in Python. You may choose from the following playable races:")
    print("\t1. Human")
    print("\t2. Elf")
    print("\t3. Dwarf")
    clan_choice = input("\nChoose your clan (Human, Elf, Dwarf): ")

    # HEIGHT
    height_input = input("Enter your height (3ft to 7ft): ")
    while not (3 <= float(height_input) <= 7):
        print("The height you chose is not an option.")
        height_input = input("You may only enter a height between 3ft to 7ft: ")

    # WEIGHT
    weight_input = input("Enter a WEIGHT between 60 lbs and 300 lbs: ")
    while not (60 <= float(weight_input) <= 300):
        print("The weight you chose is not an option.")
        weight_input = input("You may only enter a weight between 60lbs to 300lbs: ")

    # HAIR COLOR
    hair_color_options = ("white", "silver", "gray", "black", "brown", "green", "blue", "yellow", "pink", "red", "blonde")
    hairColor_input = input("Choose a HAIR COLOR (white, silver, gray, black, brown, green, blue, yellow, pink, red, blonde): ")
    while hairColor_input.lower() not in hair_color_options:
        print("The hair color you chose is not an option.")
        hairColor_input = input("You may only enter a hair color (white, silver, gray, black, brown, green, blue, yellow, pink, red, blonde): ")

    # EYE COLOR
    eye_color_options = ("white", "black", "red", "brown", "green", "blue", "purple", "amber")
    eyeColor_input = input("Choose an EYE COLOR (white, black, red, brown, green, blue, purple, amber):")
    while eyeColor_input.lower() not in eye_color_options:
        print("The eye color you chose is not an option.")
        eyeColor_input = input("You may only enter an eye color (white, black, red, brown, green, blue, purple, amber): ")

    print("These are your random attributes:")
    print(f"Strength: {Humanoid.strength}"
    f"\nDexterity: {Humanoid.dexterity}"
    f"\nConstitution: {Humanoid.constitution}"
    f"\nIntelligence: {Humanoid.intelligence}"
    f"\nWisdom: {Humanoid.wisdom}"
    f"\nCharisma: {Humanoid.charisma}")

    # clan choice conditions
    if clan_choice.upper() == "HUMAN":
        Humans.choose_attribute(0)
        print(f"\nYou have chosen the {clan_choice.capitalize()} clan, your character traits are:")
        print(f"Hair Color: {hairColor_input}"
              f"\nEye Color: {eyeColor_input}"
              f"\nHeight: {height_input} ft"
              f"\nWeight: {weight_input} lbs"
              f"\nStrength: {Humans.strength}"
              f"\nDexterity: {Humans.dexterity}"
              f"\nConstitution: {Humans.constitution}"
              f"\nIntelligence: {Humans.intelligence}"
              f"\nWisdom: {Humans.wisdom}"
              f"\nCharisma: {Humans.charisma}")

    elif clan_choice.upper() == "ELF":
        Elves.elves_bonus(0)
        print(f"\nYou have chosen the {clan_choice.capitalize()} clan, your character traits are:")
        print(f"Hair Color: {hairColor_input}"
              f"\nEye Color: {eyeColor_input}"
              f"\nHeight: {height_input} ft"
              f"\nWeight: {weight_input} lbs"
              f"\nStrength: {Elves.strength}"
              f"\nDexterity: {Elves.dexterity}"
              f"\nConstitution: {Elves.constitution}"
              f"\nIntelligence: {Elves.intelligence}"
              f"\nWisdom: {Elves.wisdom}"
              f"\nCharisma: {Elves.charisma}"
              f"\n{Humanoid._sleep_resistance}% resistance to SLEEP.")

    elif clan_choice.upper() == "DWARF":
        Dwarves.dwarves_bonus(0)
        print(f"\nYou have chosen the {clan_choice.capitalize()} clan, your character traits are:")
        print(f"Hair Color: {hairColor_input}"
              f"\nEye Color: {eyeColor_input}"
              f"\nHeight: {height_input} ft"
              f"\nWeight: {weight_input} lbs"
              f"\nStrength: {Dwarves.strength}"
              f"\nDexterity: {Dwarves.dexterity}"
              f"\nConstitution: {Dwarves.constitution}"
              f"\nIntelligence: {Dwarves.intelligence}"
              f"\nWisdom: {Dwarves.wisdom}"
              f"\nCharisma: {Dwarves.charisma}"
              f"\n{Humanoid._magic_resistance}% resistance to MAGIC.")
    else:
        print("\nPlease enter a valid clan choice.")

def Main():
    characterCreation()

Main()

