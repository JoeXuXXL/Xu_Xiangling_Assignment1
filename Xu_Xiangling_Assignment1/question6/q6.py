import numpy as np
import random
import time

#below are for classes need to be used in this code
class ship:
	#constructor: setup name with given input, 
	#and also hull and shield strength and laser damage
	#create a list with its name to store log of battle
	#the missle is for subclass
	#initialize important variable that will be used latter
	def __init__(self, setname):
		self.name = setname
		self.shield = 1800
		self.hull = 800
		self.laser = 500
		self.missile = 3000
		self.damage = 0
		self.attcreport = 0
		self.damreport = 0
		self.histtitle = "Battle history of " + str(self.name)\
+ ", the " + self.shiptype() + ": "
		self.history = [self.histtitle]

	#for identifying ship type
	def shiptype(self):
		return "standard spaceship"

	#determine if the ship is destroyed
	#update in log and print out
	def selfdestroy(self):
		if self.hull == 0:
			self.history.append(self.name + " has been destroyed!") 

	#the function for applying damage taken of the ship when called
	#with inputting the value of damage, and who attacks the ship
	def damed(self, damage, attacker):
	#flow control for determine which part of the ship
	#is supposed to take damage, and how much damage it
	#supposed to take, and update the new status of the ship
	#there are three possible sceneries
		if self.shield >= damage:
			self.shield -= damage
		elif (self.shield > 0) and (self.shield < damage):
			self.penetrate = damage - self.shield
			self.hull = self.hull - self.penetrate/2
			self.shield = 0
		else:
			self.hull = self.hull - damage/2
			self.shield = 0
	#make sure hull strength cannot be negative
		if self.hull <= 0:
			self.hull = 0

	#this function is for dealing with what kind of weapon 
	#being used by the ship and the target of the ship to attack
	#also in responsible for updating battle log
	def attc(self,wtype,targroup):
	#obtaining the damage of the weapon, and 
	#type of the weapon with flow control
	#setup hitfactor for speeder's dodge ability
		self.hitfactor = random.random()
		self.weapon = 0

		if wtype == self.laser:
			self.weapon = "laser"
			self.damage = self.laser
		elif wtype == self.missile:
			self.weapon = "missile"
			self.damage = self.missile

	#start to aim other ships with random.choice() from 
	#the list of battle ships
		target = random.choice(targroup)
	#the while loop makes sure the ship won't attack itself
	#by repeating drawing names
		while (target.name == self.name) or (target.hull <= 0):
			target = random.choice(targroup)
			
	#once target is chosen, update the battle log for the attacker
		self.attcreport = str(self.name) + " shoot " + target.name +\
"(" + target.shiptype() + ") with " + self.weapon
		self.history.append(self.attcreport)

	#check the target type if it is speeder and if
	#the hitfactor satisfies the condition for dodging
	#and ensure the speeder won't dodge after being destroyed
		if (target.shiptype() == "speeder") and\
(self.hitfactor <= 0.5) and (target.hull>0):
	#update the battle log for the target ship
			target.damreport = str(target.name) + " dodges " \
+ str(self.name) + "'s" + "(" + self.shiptype() + ") " +\
self.weapon + " attack"
			target.history.append(target.damreport)
	#if above condition is not satisfied, then apply damed 
	#function to the target ship and update the battle log
	#for the target
		else:
			target.damed(self.damage,self.name)
	#update the battle log for the target
			target.damreport = str(target.name) + " is shot by " \
+ str(self.name) + "(" + self.shiptype() + ")" + " with " + self.weapon
			target.history.append(target.damreport)

	#the function that starts a round by updating battle log
	#-1 is used in the self battle log as an identifier 
	#which helps to slice a short version of self.history
	#as the battle in process, in order to improve the view
	def roundstart(self,whichround):	
		self.history.append(-1)
		self.history.append("-----Round " + str(whichround)\
+ "----->")

	#this function is to start the attack in a round to a list
	#useful for latter of subclass warship
	def roundattack(self,whichround,targroup):
		if self.hull > 0:
			self.attc(self.laser,targroup)
		else:
			pass
	#to end a round of attack, delete the identifier -1
	#from battle log and update status and hitory 
	#in a battle round to self.history
	def roundend(self,whichround):
		self.status = "status: hull strength: "\
+ str(self.hull) + "ps  |  shield strength: " + str(self.shield) + "ps "
		self.history.append(self.status)
		self.selfdestroy()
		self.history.append("<-----Round " + str(whichround)\
+ "-----")
		self.hist = self.getparthist()
		self.history.remove(-1)
		return self.hist
		
	#print out the battle log with round number
	#short version log, only show what happen is this round
	def getparthist(self):
		self.parthist = []
		self.parthist.append(self.name + ", the " + self.shiptype())
		self.parthist.append(self.history\
[(self.history.index(-1)) + 1:])
		return self.parthist

	#print out the whole history of the battle at the end
	def getwholehistory(self):
		return self.history

#subclass warship
class warship(ship):

		#for identifying ship type
	def shiptype(self):
		return "warship"

	#redefine roundattack() for warship, so that can fire 
	#missle 30% of time with random.random()
	def roundattack(self,whichnumber,targroup):
		if self.hull > 0:
			ship.roundattack(self,whichnumber,targroup)
			if random.random() <= 0.3:
				self.attc(self.missile,targroup)
		else:
			pass
#subclass speeder
class speeder(ship):

	#for identifying ship type
	#the dodging function needs this line
	def shiptype(self):
		return "speeder"		

#this model spaceship is for define variable in prelog()
#make it easier to change parameter of ship._init_()
model = ship("model")

#below are useful function for this code

#setup all the spaceships that are going to fight in the battle
def setup():
	ship1 = ship("Axiom")
	ship2 = ship("Vanguard")
	ship3 = ship("Nemesis")
	ship4 = warship("Joe")
	ship5 = speeder("Viola")
	shiplist = [ship1, ship2, ship3, ship4, ship5]
	return shiplist

#what users see when run the code at the beginning
def prelog(shiplist):
	print " "
	print "This is a spaceship battle simulation program"
	print " "
	print "There are three kinds of space ships: "
	print "The standard spaceship is a normal ship,"
	print "while the warship has a powerful missile that will fire 30% of the time."
	print "And the speeder has 50% chance to dodge incoming attack."
	print " "
	print "All ships have a hull with", model.hull,"points of strength."
	print "and a shield with", model.shield, "points of strength."
	print "All ships are equiped with a laser with", model.laser,"points of damage."
	print "Although warship's missile can cause", model.missile,"points of damage."
	shiplist = setup()
	print " "
	print "In this simulation, there will be", len(shiplist),"spaceships fight each other."
	print "They are: "
	for i in range(len(shiplist)):
		print shiplist[i].name, " the ", shiplist[i].shiptype()	
	print " "
	return
	
#this function determines in which order that the ships
#will attack in a round randomly, for fairness
def randraw(mylist):
	listcopy = mylist
	random.shuffle(listcopy)
	ranbatlist = listcopy
	return ranbatlist

#this function is for declaring winner
def declare(mylist):
#in battling, the input will be a list with exactly one entry
#so this can return the last survivor
	winner = mylist[0]
	print "The winner is ", winner.name, ", the ", winner.shiptype(),"!!!"
	print "Congratulation to", winner.name, "!!!!!"
	return

#the function that find and delete any ships that are destroyed 
#from the input assesslist so that they won't fire and get shot
#x for count the ships that are destroyed, useful for latter 
#battaling() function
def batdestroy(assesslist,x):
		survlist = []
		for k in range(len(assesslist)):
			if assesslist[k].hull == 0:
				x += 1
#the purpose of survlist is to bypass the limitation of for loop
#in comparison with assesslist.remove(), output the new count and list
			else:
				survlist.append(assesslist[k])
		newlist = survlist		
		return newlist, x

#this is the function for start the battle
def battle(shiplist):
#initialize the parameters, deadnum 
#for counting ships that are destroyed
#setup batlist by randraw(), count for # of rounds
#in accordance to shiplist, at the beginning of the battle
	roundnum = 1
	deadnum = 0
#the useless is a useless variable that take the 
#extraoutput from batdestroy() for the code
	useless = 0
	batlist = randraw(shiplist)
	raw_input("Press Enter to start the battle!")
	print " "
	print "ready for round 1..."
	print " "
	print " "
	time.sleep(1)
#use while loop to fight round by round
#looping until only one remains
	while deadnum < (len(shiplist) - 1):
		batlist, deadnum = batdestroy(batlist,deadnum)
#randomize the battle list again after deleting
#the destroyed ships from the list
		batlist = randraw(batlist)
#due to the limitation of this while loop
#need an extra if to ensure the last survivor 
#won't attack destroyed ships
		if deadnum < (len(shiplist) - 1):
#show which round it is, and other readability
			print " "
			print " "
			print "Round ", roundnum
			print " "
#below use 3 for loops ensure all entries in battle
#history are accurate and without missing part
			for k in range(len(batlist)):
#update the battle log at the start of each round
				batlist[k].roundstart(roundnum)
			for k in range(len(batlist)):
#let ships attack each other in random order
				batlist[k].roundattack(roundnum,batlist)
#after all attacks are done, end the round
#print out battle log as battle in process
			for k in range(len(batlist)):
				print batlist[k].roundend(roundnum)
				print " "
#counting rounds and asking for input to proceed
#to control the speed of the battle so that users can read
			roundnum += 1
			raw_input("Press Enter to continue...")
#when the battle is over, use batdestroy to batlist to create
#a length 1 list, which contains the winner
#and print out the whole history for all ships from shiplist
	winner, useless = batdestroy(batlist,0)
	print " "
	print " "
	print "Fight is over, below is the complete battle history:"
	print " "
	for k in range(len(shiplist)):
		print " "
		print	shiplist[k].getwholehistory()
		print " "
#declare the winner from the list winner
	declare(winner)

#this part is to simulate the battle with defined functions and classes
shiplist = setup()
prelog(shiplist)
battle(shiplist)
print " "
print "The simulation is ended"