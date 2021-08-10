from monsters import Monster, Friend, Enemy 
from random import randrange
from time import sleep

#monstername = Monster(name, species,description, healthpoints,greeting,damaged
#friendname = name, species,description, healthpoints,greeting,damaged,highfive,gift
#enemyname = name, species,description, healthpoints,greeting,damaged,weakness
slime = Monster(
 "Sludge",
 "Slime",
  "Body made of gelitine, not tasty, very dangerous",
  15,
  "Squelch! Squelch!",
  "Angry slimey noises" )

slimeFriendly = Friend(
 "Sludge",
 "Slime",
 "Body made of gelitine, not tasty, very dangerous",
  15,
  "Squelch! Squelch!",
  "Angry slimey noises",
  "Happy slimey noises",
  "Very slimy egg" )

slimeEnemy = Enemy(
 "Sludge",
 "Slime",
  "Body made of gelitine, not tasty, very dangerous",
  15,
  "Squelch! Squelch!",
  "Angry slimey noises",
  "Sword")

rat = Monster(
  "Remmy",
  "Rat",
  "Hunts for garbage and eats it, so try not too look like such trash",
  10,
  "Sqeak! Squeak!",
  "Squeeeeeeeeeeeeeeeeeeeeeeek!...")

ratFriendly = Friend(
  "Remmy",
  "Rat",
  "Hunts for garbage and eats it, so try not too look like such trash",
  10,
  "Sqeak! Squeak!",
  "Squeeeeeeeeeeeeeeeeeeeeeeek!...",
  "Happy Squeak!",
  "A Piece of Cheese")

ratEnemy = Enemy(
   "Remmy",
  "Rat",
  "Hunts for garbage and eats it, so try not too look like such trash",
  10,
  "Sqeak! Squeak!",
  "Squeeeeeeeeeeeeeeeeeeeeeeek!...",
  "Sword")

centaur = Monster(
  "Chiron",
  "Centaur",
  "Half man, Half horse, Equal parts intelligence and temper",
  35,
  "Greetings Bipedal ape man",
  "Im on my way to olympus")

centaurFriendly = Friend(
  "Chiron",
  "Centaur",
  "Half man, Half horse, Equal parts intelligence and temper",
  35,
  "Greetings Bipedal ape man",
  "Im on my way to olympus",
  "I will follow you to Taratus and back",
  "A Gold Coin")

centaurEnemy = Enemy(
  "Chiron",
  "Centaur",
  "Half man, Half horse, Equal parts intelligence and temper",
  35,
  "Greetings Bipedal ape man",
  "Im on my way to olympus",
  "Magic")

wraith = Monster(
  "Women in White",
  "Wraith",
  "From afar she looks like a bride on the day of her wedding, but up close she is a translucent nightmare ",
  25,
  "Can you help me?",
  "Free atlast")

wraithFriend = Friend(
  "Women in White",
  "Wraith",
  "From afar she looks like a bride on the day of her wedding, but up close she is a translucent nightmare ",
  25,
  "Can you help me?",
  "screech",
  "Thankyou for helping me",
  "Wisp Salts")

wraithEnemy = Enemy(
  "Women in White",
  "Wraith",
  "From afar she looks like a bride on the day of her wedding, but up close she is a translucent nightmare ",
  25,
  "Can you help me?",
  "Screeeech",
  "Magic")

wyvern = Monster(
  "Draco",
  "Wyvern",
  "Silent death from above",
  30,
  "Screeeeeeech",
  "Low Grumbling...")

wyvernFriend = Friend(
  "Draco",
  "Wyvern",
  "Silent death from above",
  30,
  "Screeeeeeech",
  "Low Grumbling...",
  "Reptillian Purr",
  "A Silver Scale")

wyvernEnemy = Enemy(
  "Draco",
  "Wyvern",
  "Silent death from above",
  30,
  "Screeeeeeech",
  "Low Grumbling...",
  "Bow")

golem = Monster(
  "Clay",
  "golem",
  "Stands 10 foot tall and is made from stone, not an easy target. ",
  50,
  "Grunt",
  "Grunting and rocks crumbling")

golemFriend = Friend(
  "Clay",
  "golem",
  "Stands 10 foot tall and is made from stone, not an easy target. ",
  50,
  "Grunt",
  "Grunting and rocks crumbling",
  "Me CLAY",
  "Pebble")

golemEnemy = Enemy(
  "Clay",
  "golem",
  "Stands 10 foot tall and is made from stone, not an easy target. ",
  50,
  "Grunt",
  "Grunting and rocks crumbling",
  "Magic")

# harpy = Monster(
#   "Gunhild",
#   "Harpy",
#   "Half bird, half woman and 100% deadly",
#   45,
#   "Caw Caw",
#   "Squawk")

# hydra = Monster(
#   "Doomgalg",
#   "Hydra",
#   "Cut off one head and two more grow in its place",
#   65,
#   "Hisssss",
#   "ROOOAARRR")

monster_list = [slime, rat, centaur, wraith, wyvern, golem]
friend_list =[slimeFriendly, ratFriendly,centaurFriendly,wraithFriend,wyvernFriend,golemFriend]
enemy_list = [slimeEnemy,ratEnemy,centaurEnemy,wraithEnemy,wyvernEnemy,golemEnemy]
random_monster = randrange(len(monster_list))
encounter =(monster_list[random_monster])
friendly_encounter = (friend_list[random_monster])
enemy_encounter = (enemy_list[random_monster])

def welcome_screen():
  print("\n" * 20)

  print("""

  ███╗░░░███╗░█████╗░███╗░░██╗░██████╗████████╗███████╗██████╗░░██████╗
  ████╗░████║██╔══██╗████╗░██║██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔════╝
  ██╔████╔██║██║░░██║██╔██╗██║╚█████╗░░░░██║░░░█████╗░░██████╔╝╚█████╗░
  ██║╚██╔╝██║██║░░██║██║╚████║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗░╚═══██╗
  ██║░╚═╝░██║╚█████╔╝██║░╚███║██████╔╝░░░██║░░░███████╗██║░░██║██████╔╝
  ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░

  𝕾𝖔 𝖙𝖍𝖊 𝖆𝖉𝖛𝖊𝖓𝖙𝖚𝖗𝖊 𝖇𝖊𝖌𝖎𝖓𝖘
  """)
  print("\n" * 5)
  input("Press Enter To Continue...")
  

welcome_screen()
encounter =(monster_list[random_monster])
print(f"While walking along you see \n ")
encounter.describe()
sleep(1)
talk_or_hit = input ("what would you like to do with the monster?\n\n1.Befriend it\n2.Fight it\n ")
if talk_or_hit == "1":
  
  print(f"\nYou approach {friendly_encounter.get_name()} and it says {friendly_encounter.get_greeting()}")
  sleep(1)

  print(f"You offer out your hand and {friendly_encounter.get_name()}\nGives you a high five and says {friendly_encounter.get_highfive()}")

  get_gift = input(f"{friendly_encounter.get_name()} wants to give you a gift.\nDo you Accept (Y/N)\n").upper()
 
  while True:
    if get_gift == "Y":
      print(f"{friendly_encounter.get_name()} the {friendly_encounter.get_species()} gives you a {friendly_encounter.get_gift()}\n\nYou have made a friend!")
      break
    elif get_gift =="N":
      print(f"{friendly_encounter.get_name()} the {friendly_encounter.get_species()} walks away looking rather sad, you hurt his feelings")
      break
    else:
      print("That is an invalid answer")

elif talk_or_hit == "2":
  attack_method = input("How would you like to attack?\n: Sword\n: Bow\n: Magic\n\n").title()
  while True:
    if attack_method == enemy_encounter.get_weakness():
      print(f"\nyour attack thwarts {enemy_encounter.get_name()} with a mighty blow , \nyou are Victorious")
      break

    elif attack_method != enemy_encounter.get_weakness():
      print(f"\nyou attack {enemy_encounter.get_name()} with a mighty blow , \nSadly it does nothing and the Beast strikes you down")
      break

    elif attack_method != "Sword" or attack_method != "Bow" or attack_method != "Magic":
      print("That attack isnt in your arsenal, Try again")



