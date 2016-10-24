population = 1
food = 0
houses = 0
farms = 0
menu = True
game = False
months = 0
endgame = False
overcrowding = 0
energy = 0
buildmenu = False
playing = True
barracks = 0

def barrier():
	print ("--------------------------------")
	print ("")
	return

def gameover():
	global endgame
	if population < 1:
		print ("Everyone is Dead. Game Over")
		endgame = True
	else:
		endgame = False

def energymanagement():
	global overcrowding
	global energy
	overcrowding = population - (houses*4)
	if overcrowding > 0:
		energy = population - overcrowding
	
	else:
		energy = population
		overcrowding = 0

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
	energymanagement() 
	return food, months, population

def newgame(): ## Sets everything to starting numbers
	global population
	global food
	global houses
	global farms
	global months
	global energy
	global barracks
	print ("You own a farm and a wife. Try to build an empire.")
	print ("")
	population = 4
	food = 0
	houses = 1
	farms = 1
	months = 1
	energy = population
	barracks = 0
	return population, food, houses, farms, months
	
def buildhouse():
	global energy
	global houses
	if energy >= 4:
		houses = houses + 1
		energy = energy - 4
		print ("A house has been built using 4 Energy.")
		print ("Current Energy: %d" %energy)
		print ("Current Houses: %d" %houses)
		barrier()
	else:
		print ("Not Enough Energy to build a House")
		print ("Current Energy: %d" %energy)
		print ("Current Houses: %d" %houses)
		barrier()

def buildfarm():
	global energy
	global farms
	if energy >= 4:
		farms = farms + 1
		energy = energy - 4
		print ("A Farm has been built using 4 Energy.")
		print ("Current Energy: %d" %energy)
		print ("Current Farms: %d" %farms)
		barrier()
	else:
		print ("Not enough Energy to build a Farm")
		print ("Current Energy: %d" %energy)
		print ("Current Farms: %d" %farms)
		barrier()
		
def buildbarracks():
	global energy
	global barracks
	if energy >= 8:
		barracks = barracks + 1
		energy = energy - 8
		print ("A Barracks has been built using 8 Energy.")
		print ("Current Energy: %d" %energy)
		print ("Current Barracks: %d" %barracks)
		barrier()
	else:
		print ("Not enough Energy to build a Barracks")
		print ("Current Energy: %d" %energy)
		print ("Current Barracks: %d" %barracks)
		barrier()


while playing == True:
	print ("\n" *100)
	while menu == True:
		print ('Welcome to the Farm Game')
		print('1. Start Game')
		print('0. Exit')
		UserInput = input("Choice:")
	
		if UserInput == "1":
			print ("\n" * 100)
			newgame()
			game = True
			menu = False
			break
	
		if UserInput == "0":
			print ("\n" * 100)
			print ("Thank you for Playing")
			game = False
			menu = False
			playing = False
			
		else:
			print ("\n" *100)
			print ("Invalid Selection")
			barrier()
	
	while game == True:
		print ("1. Advance Month")
		print ("2. Show Stats")
		print ("3. Open Build Menu")
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
			print ("Stats:")
			print ("")
			print ("Month: %d" %months)
			print ("Population: %d" %population)
			print ("Food: %d" %food)
			print ("Energy: %d" %energy)
			print ("")
			print ("Buildings:")
			print ("")
			print ("Farms: %d" %farms)
			print ("Houses: %d" %houses)
			print ("Barracks: %d" %barracks)
			barrier()
			continue
	
		if UserInput == "3":
			print ("\n" * 100)
			game = False
			buildmenu = True
			break
	
		if UserInput == "0":
			print ("\n" * 100)
			game  = False
			playing = False
			print ("Goodbye")
		

	while buildmenu == True:
		print ("Build Menu:")
		print ("")
		print ("1. Build House")
		print ("2. Build Farm")
		print ("3. Build Barracks")
		#print ("")
		#print ("")
		#print ("")
		#print ("")
		#print ("")
		print ("0. Return")
		UserInput = input("Choice:")
	
		if UserInput == "1":
			print ("\n"*100)
			buildhouse()
			continue
		
		if UserInput == "2":
			print ("\n"*100)
			buildfarm()
			continue
		
		if UserInput == "3":
			print ("\n"*100)
			buildbarracks()
			continue
		
		if UserInput == "0":
			print ("\n"*100)
			buildmenu = False
			game = True
			continue
