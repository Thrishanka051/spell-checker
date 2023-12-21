import time, os
import os.path
from os import path
from difflib import SequenceMatcher
import datetime

# ---> FUNCTIONS

# filter every word from the list
def wordFilter (usedWord):
	newWord = ""	
	for letter in usedWord:
		if (letter.isdigit()):
			continue
		elif (letter.isupper()):
			letter = letter.lower()
			newWord = newWord + letter
		elif (letter.isalpha() == False):
			continue
		else:
			newWord = newWord + letter	
	return newWord

# add a word to the dictionary
def addToDictionary (object):
	englishWords.append(object)
	englishWords.sort()
	with open("EnglishWords.txt", "w") as fileMod:
		for listItem in englishWords:
			fileMod.write("%s\n" % listItem)

# writes in the output file
def outputFile (a, b, c, d, e, i, g, h,theList):
	
	chooseFile = input("Please write the filename for the output.\n")
			
	f = open (chooseFile, "w+")
	f.write ("The total number of words: " + str(a) + "\n")
	f.write ("The number of words spelt correctly: " + str(b) + "\n")
	f.write ("The number of incorrectly spelt words: " + str(c) + "\n")
	f.write ("The number of words added to the dictionary: " + str(d) + "\n")
	f.write ("The number of words changed by user accepting the suggested word: " + str(e) + "\n")
	f.write ("The date and time the input was spellchecked: " + i.strftime("%Y-%m-%d %H:%M:%S") + "\n")
	f.write ("The amount of time elapsed to spellcheck the input: " + str(h - g) + "\n\n")
	for item in theList:
		f.write (item + " ")
	f.close()

# main function 
def wordChecker (usedList):
	#counters:
	totalWords = 0
	correctWords = 0
	incorrectWords = 0
	addedWords = 0
	changedWords = 0
	counter = -1

	print ("\n")
	for word in usedList:
		counter += 1
		filteredWord = wordFilter(word)
		usedList[counter] = filteredWord
		print (usedList[counter])

	counter = -1 

	# checks every word in the sentence
	for word in usedList:
		counter += 1
		if (word in englishWords):
			correctWords += 1
		else:
			while (True):
				wordAction = input("\nThe word " + '"' + word + '"' + " is not in the dictionary.\n\n"+ "Choose your action:\n(1) Ignore the word\n(2) Mark the word\n(3) Add the word to the dictionary\n(4) Get a suggestion\n")
				if (wordAction == '1'):
					incorrectWords +=1
					break
				elif (wordAction == '2'):
					usedList[counter] = "?" + word + "?"
					incorrectWords += 1
					break
				elif (wordAction == '3'):
					addToDictionary (word)  # add a word to the disctionary
					correctWords += 1
					addedWords += 1
					break
				elif (wordAction == '4'):
					maxx = 0 
					counterRatio = -1
					for possibleWord in englishWords:
						counterRatio += 1
						ratio = SequenceMatcher(None, word, possibleWord).ratio()
						if (ratio > maxx):
							maxx = ratio
							wordFound = counterRatio
					print ("Did you mean " + '"' + englishWords[wordFound] + '"' + "?")
					while (True):
						acceptWord = input("Press y to accept the word or n to reject it.\n")
						if (acceptWord == 'y'):
							usedList[counter] = englishWords[wordFound]
							correctWords += 1
							changedWords += 1
							break
						elif (acceptWord == 'n'):
							incorrectWords += 1
							break
						else:
							print ("Invalid input. Try again!\U0001F914")
					break
				else:
					print ("Invalid input. Try again!\U0001F914")
		dateAndTime = datetime.datetime.now()
		endTime = time.time()
		totalWords += 1

	# prints the statistics
	print ("The total number of words: " + str(totalWords) + "\n")
	time.sleep(0.5)	
	print ("The number of words spelt correctly: " + str(correctWords) + "\n")
	time.sleep(0.5)
	print ("The number of incorrectly spelt words: " + str(incorrectWords) + "\n")
	time.sleep(0.5)
	print ("The number of words added to the dictionary: " + str(addedWords) + "\n")
	time.sleep(0.5)
	print ("The number of words changed by user accepting the suggested word: " + str(changedWords) + "\n")
	time.sleep(0.5)
	print ("The date and time the input was spellchecked: " + dateAndTime.strftime("%Y-%m-%d %H:%M:%S") + "\n")
	time.sleep(0.5)
	print ("The amount of time elapsed to spellcheck the input: " + str(endTime - startTime) + "\n\n")

	outputFile(totalWords, correctWords, incorrectWords, addedWords, changedWords, dateAndTime, startTime, endTime, usedList)

	while(True):
		checkFinish = input("\nYour sentence has been spell checked succesfully!\U0001F44C\nDo you wish to return to main menu(1)\U0001F519 or to quit the program(0)?\U0001F51A")
		if (checkFinish == '1'):
			break
		elif (checkFinish == '0'):
			print ("Quitting the program. . .")
			time.sleep(1.5)
			os._exit(0)
		else: 
			print ("Invalid input. Try again!\U0001F914")



# ---> THE PROGRAM

os.system('clear') # clear the terminal every time the program starts

print ("\nWelcome to the Spellchecker!\U0001F603\n")
time.sleep(0.8)

with open("EnglishWords.txt") as fileE:
			englishWords = fileE.read().split()

while (True):
	decisionInput = input("Please choose if you want to:\n-> spell check a sentence (1)\n-> spell check a file (2)\n-> quit the program (0).\n")
	startTime = time.time()

	# spell check a sentence
	if (decisionInput == '1'):
		sentence1 = input("Enter a sentence: ")  # input from keyboard
		wordsList = sentence1.split()
		wordChecker (wordsList)

	# spell check a file
	elif (decisionInput == '2'):
		while (True):
			fileName = input("Please enter the file name: ")
			if (path.exists(fileName)):  # check  if the file exists
				with open("sentencefile.txt") as file:  # input from .txt file
					sentence2 = file.read()
				wordsList2 = sentence2.split()
				file.close()
				wordChecker (wordsList2)
				break  #get out of the loop
			else:
				while (True):
					toMenu = input("The file does not exists. Do you want to try again? (1) Or to return to main menu? (2)\n")
					if (toMenu == '1'):
						break
					elif (toMenu == '2'):
						break
					else:
						print ("Invalid input! Try again.\U0001F914")
				if (toMenu == '2'):
					break

	# quit the program
	elif (decisionInput == '0'):
		print ("Quitting the program. . .")
		time.sleep(1.5)
		break

	# invalid input
	else:
		print("Invalid input, please try again!\U0001F914")

# ---> THE END 