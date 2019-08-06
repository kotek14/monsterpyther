# Kotek14
# CS110A Final

from time import sleep # I think that the Narrator looks cooler with time delays
from random import randint # I use random a lot here

# This block of defines allows me to have nice colorful output
# Proudly stolen from https://www.geeksforgeeks.org/print-colors-python-terminal/
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) # intro
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) # narrator
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) # player hits
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) # player takes damage
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) # death, errors and crits
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) # other information

# Game progression
# Wanted to make the chance 15%, but it was going too slow
def random_loot_upgrades():
	prCyan("Hey! You are making some progress, are you? Let's see what you got after the battle")
	prCyan("Wow, look! %d XP! Too bad it's useless..." % randint(10, 30)) # I wanted
	if randint(1, 100) < 35:
		prCyan("Look! That bastard was guarding a set of armor. (+5 DEF)")
		player['df'] = player['df'] + 5
	if randint(1, 100) < 35:
		prCyan("Look! That bastard was guarding a sword. (+5 ATK)")
		player['atk'] = player['atk'] + 5
	if randint(1, 100) < 35:
		prCyan("Look! That bastard was guarding a health potion. (+20 HP)")
		player['hp_max'] = player['hp_max'] + 20 # That's why I have that hp_max key
	prYellow("---" * 10)

# I could avoid these two functions and embed their return values straight into the monster_encounter function, but decided not to.
def monster_adjective(monster_adj):
	return(monster_adj[randint(0, len(monster_adj) - 1)]) # Was too lazy to count adjectives

def monster_word(monster_dict):
	return(monster_dict[randint(0, len(monster_dict) - 1)]) # Was too lazy to count monsters

# This thing is huge. It's better to read comments below it first
def monster_fight():
	global counter
	prYellow("\n%s has %d HP, %d ATK and %d DEF" % (monster['name'], monster['hp'], monster['atk'], monster['df']))
	prYellow("%s has %d/%d HP, %d ATK and %d DEF" % (player['name'], player['hp'], player['hp_max'], player['atk'], player['df']))
	player_choice = raw_input("(A)ttack or (F)lee? ")
	player_choice = player_choice.lower()
	if player_choice == "flee" or player_choice == "f": # That's some gameplay. You have to run away sometimes
		prYellow("\nYou realize that you will not win and try to flee")
		if randint(0, 100) > 50: # 50% chance to flee
			prYellow("You are lucky. You were able to get away.")
			monster_encounter()
		else:
			prPurple("\nYou unsuccessfully tried to run away, but the monster was faster. You took damage.")
			player['hp'] = player['hp'] - monster['atk'] * 2 # If you fail, the monster crits you 
			if player['hp'] > 0:
				monster_fight()
			else:
				prRed("You are dead. You killed %d monsters" % counter) # Displaying the score in the end
				quit(1) # Code 1 goes for a player's death
	elif player_choice == "attack" or player_choice == "a":
		player_attack = int(player['atk'] * (1.0 - monster['df'] * 0.01)) # Player's ATK minus monster's DEF/100. Nothing special, old RPGs counted the damage this way.
		bonus = randint(-2, 5) # Adding some randomness
		if randint(1, 100) < 10: # 10% chance to crit
			player_attack = player_attack * 2
			prRed("CRITICAL HIT!")
		prGreen("\nYou hit the monster. %s loses %d HP" % (monster['name'], player_attack + bonus))
		monster['hp'] = monster['hp'] - player_attack - bonus
		if monster['hp'] > 0:
			monster_attack = int(monster['atk'] * (1.0 - player['df'] * 0.01))
			bonus = randint(-2, 5)
			prPurple("\nMonster hits you. %s loses %d HP" % (player['name'], monster_attack + bonus))
			player['hp'] = player['hp'] - monster_attack - bonus
			if player['hp'] <= 0:
				prRed("You are dead. You killed %d monsters" % counter) # Displaying the score in the end
				quit(1) # Code 1 goes for a player's death
		else:
			prGreen("You won!")
			counter += 1 # Incrementing the counter. Why not "killed_monsters_counter_to_show_after_players_death"? Too lazy to type.
			prYellow("---" * 10)
			random_loot_upgrades() # Decided to add some progression to the game
	else:
		prRed("It's not like you have more than two options here, come on!")
		monster_fight()

# This function basically resets player's health to its max and creates a monster
def monster_encounter():
	player['hp'] = player['hp_max']
	monster['name'] = monster_adjective(monster_adj) + " " + monster_word(monster_dict) # I decided to add some random names for monsters
	monster['hp'] = player['hp'] + randint(-7, 5)
	monster['atk'] = player['atk'] + randint(-3 * (player['atk'] / 5), 2) # It's all game balance
	monster['df'] = player['df'] + randint(-4, 1)
	prYellow("\nYou encounter a monster named " + monster['name'])
	while (player['hp'] > 0) and (monster['hp'] > 0):
		print("")
		monster_fight()

# Some essential variables. I decided that it's much easier to use global ones for keeping track of player and monsters' parameters
counter = 0
player = {'name': 'placeholder', 'hp': 20, 'atk': 5, 'df': 5, 'hp_max': 20} # I initialize them with placeholder values
monster = {'name': 'placeholder', 'hp': 999, 'atk': 999, 'df': 999} # Because I can
monster_dict = ["Vampire", "Troll", "Centaur", "Basilisk", "Cyclops", "Domovoi", "Dwarf", "Elf", "Faun", "Gnome", "Gargoyle", "Harpy", "Hydra", "Ogre", "Goblin"] # I got this list from the first website that popped up on Google
monster_adj = ["Terrible", "Ugly", "Horrible", "Cruel", "Giant", "Dreadful", "Evil", "Frightening", "Enormous", "Terrifying", "Awful", "Wicked"] # Same. I'm not creative enough to come up with tons of adjectives

# Here we have an optional intro
prYellow("MonsterPyther v0.00001")
prLightPurple("I really don't know what I am doing and probably I should have done something simple")
prLightPurple("The game has no end, so you might want to hit Ctrl+C to stop it. Also, it doesn't save anything")
prLightPurple("Alright, enough whining, the game starts...\n")
intro = raw_input("Do you want an introduction? (Y)ES/(N)o ") 
intro = intro.lower() # When I was testing, I got really tired of hitting Shift
if not intro or intro == "y" or intro == "yes": # Same goes for typing entire words out
	sleep(1)	
	prCyan("A long time ago in a galaxy far, far away there was a hero named...")
	sleep(0.7)
	prCyan(".")
	sleep(0.7)
	prCyan(".")
	sleep(0.7)
	prCyan(".")
	prCyan("Ugh... What is your name?")
	player['name'] = raw_input("My name is ")
	if not player['name']:
		sleep(2)
		prCyan("Alright, alright. *cough* There was an unnamed hero")
		player['name'] = "Unnamed hero"
	else:
		sleep(2)
		prCyan("Alright, alright. *cough* There was a hero named " + player['name'])
	sleep(1)
	prCyan("He used to be an adventurer like me, then he took an arrow in the knee...")
	sleep(1)
	prCyan("But he recovered and was ready to kick some monster ass")
	sleep(1)
	prCyan("Well... I guess that's enough narrative, I don't get paid to do this. Have fun!")
elif intro == "n" or intro == "no":
	player['name'] = raw_input("My name is ")
else:
	prRed("Come on, this user input is validated and considered invalid!!!")
	quit(2) # Code 2 goes for an exit on invalid input
while 1 == 1:
	monster_encounter()
