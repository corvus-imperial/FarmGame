population = 1
food = 0
houses = 0
farms = 0
menu = True
game = False
months = 0
endgame = False

def gameover():
	global endgame
	if population < 1:
		print ("Everyone is Dead. Game Over")
		endgame = True
	else:
		endgame = False

def month():
	global food
	global months
	global population
	food =  food + (farms*10) ##Generates new food
	food =  food - population ##Negates food for population
	if food < 0 : ##If Not enough food
		print ("People are Starving, %d people have died."% abs(food)) ## prints number of dead
		population =  population +  food ##kill people
		food = 0 ##Keep food from going negative
		gameover() ##Check if anyone is alive
	else:
		print ("You Had Enough Food for Month %d"% months)
	months =  months + 1 ##Advances Month
	return food, months, population

def newgame(): ## Sets everything to starting numbers
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
	
	if UserInput == "1":
		print ("\n" * 100)
		month()
		if endgame == True:
			game = False
		continue
	
	if UserInput == "2":
		print ("\n" * 100)
		print ("")
		print ("stats:")
		print ("Month: %d" %months)
		print ("Population: %d" %population)
		print ("Farms: %d" %farms)
		print ("Food: %d" %food)
		continue
	
	if UserInput == "0":
		print ("\n" * 100)
		game  = False
		print ("Goodbye")
		

	
