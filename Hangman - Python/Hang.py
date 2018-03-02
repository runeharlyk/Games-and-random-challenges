#Hangman
from os import system
from time import sleep
allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å', ' ']

class HangGame():
	characters = allowed
	Guessed = []
	HangingWord = None
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
				return WordInList

	def Start_Game(self):
		self.GameGoing = True
		self.HangingWord = self.Get_Word(self)
		self.Clear_Screen(self)
		while True:
			self.Guess_A_Letter(self)
			self.current_statues = self.Check_Statues(self)
			if self.current_statues == 'Won':
				self.Clear_Screen(self)
				print('You won! Great job! The word was: ')
				for i in range(0,len(self.HangingWord)):
					print(self.HangingWord[i], end="")
				sleep(.1)
				print(' ')
				sleep(4)
				break
			elif self.current_statues == 'Over':
				self.Clear_Screen(self)
				print(dead)
				print('You hanged the man! The word was: ')
				for i in range(0,len(self.HangingWord)):
					print(self.HangingWord[i], end="")
				sleep(.1)
				print(' ')
				sleep(4)
				break

	def Guess_A_Letter(self):
		self.Print_Statue(self)
		self.Last_Letter = input('Guess a letter: \n').lower()
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
		try:
			system('cls')
		except:
			system('clear')
		return

	def Check_Statues(self):
		if self.Lives <= 0:
			print(dead)
			return 'Over'

		for i in range(0,len(self.HangingWord)):
			if self.HangingWord[i] not in self.Guessed:
				return
		return 'Won'

	def CleanUp(self):
		self.GameGoing = False
		self.characters = allowed
		self.Guessed = []
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
while True:
	HangGame.Start_Game(HangGame)
	HangGame.CleanUp(HangGame)
