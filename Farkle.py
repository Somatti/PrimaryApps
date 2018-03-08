"""
Let's create a program that allows our user to play a hand of Farkle.

Farkle is a dice rolling game. If at anytime, a roll you make scores 0 points, you lose the hand and you lose the points you scored for that hand.
A hand begins by rolling 6 dice. Scoring will be listed below.

In order to get on the scoreboard, you must first score 500 points.

Once you are on the scoreboard, you may choose to stop rolling at any time assuming the last roll you made didn't Farkle.

Scoring:

a 1 represents 100 points, a 5 represents 50 points.

a three of a kind represents a score multiplier by that number like this:

Three 2's = 200 points
Three 3's = 300 points
Three 4's = 400 points
Three 5's = 500 points
Three 6's = 600 points

Other combinations that can score you points include:

Two Triples = 2500 points
Three pairs = 1500 points
1-2-3-4-5-6 = 1500 points
Four of a kind = 1000 points
Four of a kind and a pair = 1500 points
Five of a kind = 2000 points
Six of a kind = 3000 points

You don't have to use scored dice if you don't want to.
If all six dice have scored you points, you can continue scoring that hand with a new set of 6 dice.
"""

"""
We want to create a Class for Dice.
We can create 6 dice and put them into a list that acts as our hand. We can use random to get their values for a hand roll.
Then we ask our user which dice they want to score and remove those dice from the list/hand to allow the user to continue rolling.

When the user chooses to stop rolling, whatever running total they have will be added to their score.
If they ever Farkle, their turn ends and we will reset their running total to 0.
"""

# Once the initial set up of this game is complete, I will look into ways we can complicate the game even further.
# - Maybe between hands, we will set up a 'computer' hand that will make decisions based on statistical chance. -

import random

class createDice:
	def _init__(self, value = 0):
		self.value = value
		
	def randomize(self):
		self.value = random.randint(1,6)
		
hand = []
d1 = createDice()
d2 = createDice()
d3 = createDice()
d4 = createDice()
d5 = createDice()
d6 = createDice()
score = 0
runningTotal = 0

""" Step one - Create a new hand -This should create an array/list that contains our 6 dice from the start. """		
def newHand(hand):
	
	hand = [d1, d2, d3, d4, d5, d6]
	
	for dice in hand:
		dice.randomize()
	
	return hand

""" Step 2 - We need a way to roll the hand of dice to get values """		
def rollHand(hand):
	
	for dice in hand:
		dice.randomize()
	
	hand = handSort(hand)
	
	print("You rolled: ")
	for dice in hand:
		print(dice.value),
	print("")
	
""" Standard sort function for our list of objects. I think it will make it easier to score our hand like this. """
def handSort(hand):
	for item in range(1, len(hand)):
		marker = item
		currentObject = hand[item]
		currentValue = hand[item].value
		while marker > 0 and hand[marker-1].value > currentValue:
			hand[marker] = hand[marker-1]
			marker -= 1
		hand[marker] = currentObject
	
	return hand

"""
Step 3 - We need to check the values of the dice to determine if our user Farkled. 
If they didn't, we need to ask our user which dice they would like to score. 
Then we need to ask the user if they would like to continue rolling. 

** Note - I initially tried doing this with Dictionaries, but I think for this particular problem, having a list simplifies the issue when we need to determine scoring **

Steps to checking scores:
6 of a kind - check if the value to any key in our dict equals 6.
5 of a kind - check if the value to any key in our dict equals 5, if so, check if there's another key. If there is, check to see if the key is a 1 or a 5.
4 of a kind - check if the value to any key in our dict equals 4, if so, check if there's another key with a value of 2. If there isn't check if any keys are 1's or 5's.
Two triples - check to see if there are two keys in our dict, check if the first key and second key both have a value of 3.
Three doubles - check to see if there are three keys in our dict, check if all three keys have a value of 2.
3 of a kind - check if the value to any key in our dict equals 3. if so, check if there's another key. If there is, check to see if it's a 1 or a 5.
1's and 5's - check to see if there are any 1s of 5s rolled and if so, how many?

After determining what kind of scoring points we have:
Our user must take ATLEAST one item that scores points - 
	so we need to ask the user if they want to score one of their combos. 
	if so, remove that many dice from our hand that we will return.
	Then we need to ask our user if they want to score any 1's. Remove those dice from the hand if so.
	Then we need to ask our user if they want to score any 5's. Remove those dice from the hand as well.

	Then we need to check the length of our hand(our hand is not the dictionary. It's the list we created holds our Dice objects)
	If there are no items left in the hand, we give our user a new 6 dice and prompt them that they get to continue rolling. We can indicate that our use 'Chained another hand'
	*BUT* Before rolling those dice, we must first tell our user how many dice they have left and prompt them if they would like to continue rolling.

"""
def scoreHand(hand):
	handVals = []
	scoredDice = {}
	outcomes = [1, 2, 3, 4, 5, 6]
	for object in hand:
		handVals.append(object.value)
		
	for i in range(1, 7):
		results = [[x, handVals.count(x)] for x in set(outcomes)]
	
	#This makes sure that our scored results accepts three pairs
	for item in results:
		if item[1] == 2:
			scoredDice[item[0]] = item[1]
	#If the score isn't 3 pairs, then we need to reset our dictionary to allow other scores to be possible	
	if len(scoredDice) != 3:
		scoredDice = {}
		#This allows us to make a Straight 1-2-3-4-5-6 a possible result.
		if results[0][1] == 1 and results[1][1] == 1 and results[2][1] == 1 and results[3][1] == 1 and results[4][1] == 1 and results[5][1] == 1:
			
			for item in results:
				scoredDice[item[0]] = item[1]
		#If we didn't roll three pairs or a straight, then our dictionary will contain a key we rolled MORE than 2 of, and/or the keys will be 1 and/or 5.
		else:
		
			for item in results:
				if item[1] > 2:
					scoredDice[item[0]] = item[1]
				elif item[0] == 1 and 0 < item[1] < 3:
					scoredDice[item[0]] = item[1]
				elif item[0] == 5 and 0 < item[1] < 3:
					scoredDice[item[0]] = item[1]
	
	keylist = list(scoredDice.keys())
	
	print(keylist)
	print(results)
	print(scoredDice)
	
	
	#This variable will make sure our user took some amount of points from the hand(part of the rules.)
	pointCondition = len(scoredDice)
	
	#if len(scoredDice) == 0:
		
	#	print("You Farkled! You scored 0 points for this hand!")
		
	#elif straight(keylist) == True:
	
	#	print("You scored a straight! +3000 Points."
		
	#elif two_triples(scoredDice, keylist) == True:
	
	#	print("You scored two Triples! +2500 points.")
		
	#elif three_pairs(scoredDice, keylist) == True:
	
	#	print("You scored three Pairs! +1500 points.")
		
		
	
"""
Create a function that allows our user to choose which dice(if they are scorable points) to remove from their hand.
Points are added to their running total.
Remove those objects from 'hand'
Ask if they want to continue rolling.
"""



#For 6-of-a-kind, 5-of-a-kind, and 4-of-a-kind, we will iterate over the dictionaries looking for a value of 6, 5, and 4. We will then return the KEY so we know which key to remove after scoring
def six_of_a_kind(dict, keylist):
	result = None
	for key in keylist:
		if dict[key] == 6:
			result = key
	
	return result

def five_of_a_kind(dict, keylist):
	result = None
	for key in keylist:
		if dict[key] == 5:
			result = key
	
	return result
	
def four_of_a_kind(dict, keylist):
	result = None
	for key in keylist:
		if dict[key] == 4:
			result = key
	
	return result

#We need to make sure there is only 2 keys in the Dictionary and then we need to verify the values for both keys are 3
def two_triples(dict, keylist):
	result = False
	if len(keylist) == 2:
		if dict[keylist[0]] == 3 and dict[keylist[1]] == 3:
			result = True
	
	return result

#Same deal with two_triplets but 3 keys and value must be 2
def three_pairs(dict, keylist):
	result = False
	if len(keylist) == 3:
		if dict[keylist[0]] == 2 and dict[keylist[1]] == 2 and dict[keylist[2]] == 2:
			result == True

	return result

#If your dictionary has six keys, we know our user rolled 6 different numbers, 1-2-3-4-5-6.
def straight(keylist):
	result = False
	if len(keylist) == 6:
		result = True
	
	return result

def triples(dict, keylist):
	result = None
	for key in keylist:
		if dict[key] == 3:
			result = key
			
	return result


#def check_number(dict, keylist):
