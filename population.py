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
		print ("")
		print ("Current Houses: %d" %houses)
	else:
		print ("Not Enough Energy to build a House")
		print ("")
		print ("Current Houses: %d" %houses)

def buildfarm():
	global energy
	global farms
	if energy >= 4:
		farms = farms + 1
		energy = energy - 4
		print ("A Farm has been built using 4 Energy.")
		print ("")
		print ("Current Farms: %d" %farms)
	else:
		print ("Not enough Energy to build a Farm")
		print ("")
		print ("Current Farms: %d" %farms)
		
def buildbarracks():
	global energy
	global barracks
	if energy >= 8:
		barracks = barracks + 1
		energy = energy - 8
		print ("A Barracks has been built using 8 Energy.")
		print ("")
		print ("Current Barracks: %d" %barracks)
	else:
		print ("Not enough Energy to build a Barracks")
		print ("")
		print ("Current Barracks: %d" %barracks)


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
			
		else:
			print ("\n" *100)
			print ("Invalid Selection")
			barrier()
		

	while buildmenu == True:
		print ("Current Energy: %d" %energy)
		barrier()
		print ("Build Menu:")
		print ("")
		print ("1. Build House (4 Energy)")
		print ("2. Build Farm (4 Energy)")
		print ("3. Build Barracks (8 Energy)")
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
		
		else:
				print ("\n" *100)
				print ("Invalid Selection")
				barrier()
