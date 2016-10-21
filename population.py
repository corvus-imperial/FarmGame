population = 1
food = 0
houses = 0
farms = 0
menu = True
game = False
months = 0

def month(): ##Resources used during a month
	global food
	global months
	global population
	food =  food + (farms*10)
	food =  food - population
	if food < 0 :
		print ("People are Starving, %d people have died."% food)
		population =  population +  food
		## Put stuff here for if population reaches Zero
	else:
		print ("You Had Enough Food for Month %d"% months)
	months =  months + 1
	return food, months, population

def newgame(): ##Set Stats for New Game
	global population
	global food
	global houses
	global farms
	global months
	print ("You own a farm and a wife. Try to build an empire.")
	population = 2
	food = 0
	houses = 1
	farms = 1
	months = 1
	return population, food, houses, farms, months

while menu == True:
	print ('Welcome to the Farm Game')
	print('1. Start Game')
	print('2. Exit')
	UserInput = input("Choice:")
	
	if UserInput == "1":
		print ("\n" * 100)
		newgame()
		game = True
		menu = False
		break
	
	if UserInput == "2":
		print ("\n" * 100)
		print ("Thank you for Playing")
		game = False
		menu = False
	
	
while game == True:
	print ("")
	print ("1. Advance Month")
	print ("2. Show Stats")
	print ("0. Exit")
	UserInput = input("Choice:")
	
	if UserInput == "1": ##Advance Month
		print ("\n" * 100)
		month()
		continue
	
	if UserInput == "2": ##Show Stats
		print ("\n" * 100)
		print ("")
		print ("Stats:")
		print ("")
		print ("Month: %d" %months)
		print ("Population: %d" %population)
		print ("Farms: %d" %farms)
		print ("Food: %d" %food)
		continue
	
	if UserInput == "0": ##Exit
		print ("\n" * 100)
		game  = False
		print ("Goodbye")
		


##Add Energy system
	##1 Energy per population
	##energy deminishes if overcrowded
	##build house, man farm, recruit use energy
	
## Game menu has stuff to do before advancing month.
	##build house
	##recruit - based on happiness of population
	##work farm - stop farms auto producing food. 
	##Arm population/make weapons
	
## Random Events - happens on advance months
	##plague - kills population
	##infestation - diminish food
	##Tornado - Destroys Housing and kills people
	##Fire - Destroys Housing and food (way to upgrade houses to stone to avoid)
	##Invasion - Kills population if defence is low