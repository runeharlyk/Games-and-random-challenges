#Hangman
from os import system
from time import sleep
import random
allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å', ' ']
Words = ['alligator', 'ant', 'bear', 'bee', 'bird','camel','cat','cheetah','chicken','chimpanzee','cow','crocodile','deer','dog','dolphin','duck','eagle','elephant','fish','fly','fox','frog','giraffe','goat','goldfish','hamster','horse','hippopotamus','kangaroo','kitten','lion','lobster','monkey','octopus','owl','panda','pig','puppy','rabbit','rat','scorpion','seal','shark','sheep','snail','snake','spider','squirrel','tiger','turtle','wolf','zebra']
class HangGame():
	characters = allowed.copy()
	Multiplayer = None
	Category = None
	HangingWord = None
	Guessed = [' ']
	Last_Letter = ''
	Lives = 6
	current_statues = 'Over'

	def Get_Word(self):
		while True:
			raw = input('Write your word, and don\'t show it to your opponent!\n').lower()
			if raw != '':
				WordInList = list(raw)
				for i in range(0, len(WordInList)):
					if WordInList[i] not in self.characters:
						self.CleanUp(self)
						print('You suck! Only alphabetic characters')
						self.Get_Word(self)
				self.HangingWord = WordInList
				break

	def Start_Game(self):
		self.Clear_Screen(self)
		if self.Multiplayer == None:
			self.Multiplayer = self.Get_Players(self)
		self.GameGoing = True
		if self.Multiplayer:
			self.Get_Word(self)
		else:
			self.HangingWord = list(random.choice(Words))
		self.Clear_Screen(self)
		while True:
			self.Guess_A_Letter(self)
			self.current_statues = self.Check_Statues(self)
			if self.current_statues == 'Won':
				self.Clear_Screen(self)
				print('You won! Great job! The word was: ')
				sleep(.5)
				print(''.join(self.HangingWord))
				sleep(4)
				break
			elif self.current_statues == 'Over':
				self.Clear_Screen(self)
				print(dead)
				print('You hanged the man! The word was: ')
				sleep(0.5)
				print(''.join(self.HangingWord))
				sleep(4)
				break

	def Guess_A_Letter(self):
		self.Print_Statue(self)
		print("Guess a letter: \n>>>",end='')
		self.Last_Letter = input().lower()
		if len(self.Last_Letter) == 1:
			if self.Last_Letter in self.characters and self.Last_Letter not in self.Guessed:
				self.characters.remove(self.Last_Letter)
				if self.Last_Letter in self.HangingWord:
					self.Guessed.append(self.Last_Letter)
				else:
					self.Lives -= 1
					self.Guessed.append(self.Last_Letter)

	def Print_Statue(self):
		self.Clear_Screen(self)
		if self.Lives == 6:
			print(lives6)
		if self.Lives == 5:
			print(lives5)
		if self.Lives == 4:
			print(lives4)
		if self.Lives == 3:
			print(lives3)
		if self.Lives == 2:
			print(lives2)
		if self.Lives == 1:
			print(lives1)
		for i in range(0,len(self.HangingWord)):
			if self.HangingWord[i] in self.Guessed:
				print(self.HangingWord[i] + ' ', end="")
			elif self.HangingWord[i] == ' ':
				print("  ", end="")
			else:
				print('_ ', end="")
		print('\n\n\t\t    Lives: ' + str(self.Lives) + '\n\n', end="")
		for i in range(int(len(self.characters)/6)+1):
			print('\t\t', end="")
			print(", ".join(self.characters[i*6:(i+1)*6]) + "\n")

	def Clear_Screen(self):
		Val = system('cls')
		if Val != 0:
			system('clear')

	def Check_Statues(self):
		if self.Lives <= 0:
			print(dead)
			return 'Over'
		for i in range(0,len(self.HangingWord)):
			if self.HangingWord[i] not in self.Guessed:
				return
		return 'Won'

	def Get_Players(self):
		while True:
			Raw = input('Do you want to play Single- or Multiplayer (S/M)').lower()
			if Raw == 's':
				return False
			elif Raw == 'm':
				return True
			else:
				print('"S" or "M"')

	def CleanUp(self):
		self.GameGoing = False
		self.characters = allowed.copy()
		self.Guessed[:] = [' ']
		self.HangingWord = None
		self.Last_Letter = ''
		self.Lives = 6
		self.Clear_Screen(self)
dead = """___________
|  /     |
| /      0
|/      -I-
|       / \\
|
| """
lives1 = """___________
|  /     |
| /      0
|/      -I-
|       /
|
| """
lives2 = """___________
|  /     |
| /      0
|/      -I-
|
|
| """
lives3 = """___________
|  /     |
| /      0
|/      -I
|
|
| """
lives4 = """___________
|  /     |
| /      0
|/       I
|
|
| """
lives5 = """___________
|  /     |
| /      0
|/
|
|
| """

lives6 = """___________
|  /     |
| /
|/
|
|
| """
if __name__=='__main__':
	print('Welcome to Hangman the game...')
	sleep(2)
	print('>>>The creator of this version of the hangman game is Rune Harlyk.')
	sleep(2)
	print('>>>Source code:')
	print('https://github.com/runeharlyk/Games-and-random-challenges/blob/master/Hangman%20-%20Python/Hang.py')
	sleep(2)
	print('\nHave fun :D')
	sleep(3)
	while True:
		HangGame.Start_Game(HangGame)
		HangGame.CleanUp(HangGame)
