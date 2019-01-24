#!/usr/bin/python3

# Inuktitut Syllabics, version 1
# This simple Python app is to practice your knowledge of the qaniujaaqpait
# (Inuktitut syllabary). It is possible to transliterate from qaniujaaqpait
# (Inuktitut syllabary) to qaliujaaqpait (Latin letters) and vice versa, each
# direction with three difficulty levels. The only difference between the levels
# is the number of buttons to choose from. The number of correct and wrong
# answers are displayed on the screen, but are not saved.

# Syllabiques inuktitut, version 1
# Cette application simple en Python est pour pratiquer votre connaissance des
# qaniujaaqpait (syllabiques inuktitut). Il est possible de translitérer des
# qaniujaaqpait (syllabiques inuktitut) vers les qaliujaaqpait (lettres latines)
# et vice versa, chaque direction avec trois niveaux de difficulté. La seule
# différence entre les niveaux est le nombre de boutons de sélection. Le
# nombre de bonnes et de mauvaises réponses sont affichés à l'écran, mais pas
# ne sont pas sauvegardés.

# Inuktitut Silbe, Version 1
# Diese einfache Python-App hat die Funktion Ihr Wissen über das Qaniujaaqpait
# (Inuktitut Silbe) zu vertiefen. Es ist möglich von das Qaniujaaqpait
# (Inuktitut Silbe) in das Qaliujaaqpait (lateinische Buchstaben) sowie
# umgekehrt in jede Richtung zu jeweils drei Schwierigkeitsgraden zu
# transliterieren. Der einzige Unterschied zwischen den Graden ist die Anzahl
# der Auswahlschaltflächen. Die Anzahl der richtigen und falschen Antworten
# werden auf dem Bildschirm angezeigt, aber sie werden nicht gespeichert.



# Some easily tweakable parameters
generalFontSize = 20 # Font size of the text, except the question display
qDispFontSize = 36 # Font size of the question display
menuLabelPadx = 15 # Horizontal padding (in pixels) around the labels in the menu
menuButtonPadx = 2 # Horizontal padding (in pixels) around the buttons in the menu
menuPady = 7 # Vertical padding (in pixels) between the rows in the menu
statMinWidth = 2 # Minimal width (in characters) of the statistics displays



## Definitions of the syllabics in unicode
# a short syllabics
a = '\u140a'
pa = '\u1438'
ta = '\u1455'
ka = '\u1472'
ga = '\u1490'
ma = '\u14aa'
na = '\u14c7'
sa = '\u14f4'
la = '\u14da'
ja = '\u152d'
va = '\u1559'
ra = '\u154b'
qa = '\u1583'
nga = '\u1593'
lbara = '\u15a4'

# a long syllabics
aa = '\u140B'
paa = '\u1439'
taa = '\u1456'
kaa = '\u1473'
gaa = '\u1491'
maa = '\u14ab'
naa = '\u14c8'
saa = '\u14f5'
laa = '\u14db'
jaa = '\u152e'
vaa = '\u155a'
raa = '\u154c'
qaa = '\u1584'
ngaa = '\u1594'
lbaraa = '\u15a5'

# i short syllabics
i = '\u1403'
pi = '\u1431'
ti = '\u144e'
ki = '\u146d'
gi = '\u148b'
mi = '\u14a5'
ni = '\u14c2'
si = '\u14ef'
li = '\u14d5'
ji = '\u1528'
vi = '\u1555'
ri = '\u1546'
qi = '\u157f'
ngi = '\u158f'
lbari = '\u15a0'

# i long syllabics
ii = '\u1404'
pii = '\u1432'
tii = '\u144f'
kii = '\u146e'
gii = '\u148c'
mii = '\u14a6'
nii = '\u14c3'
sii = '\u14f0'
lii = '\u14d6'
jii = '\u1529'
vii = '\u1556'
rii = '\u1547'
qii = '\u1580'
ngii = '\u1590'
lbarii = '\u15a1'

# u short syllabics
u = '\u1405'
pu = '\u1433'
tu = '\u1450'
ku = '\u146f'
gu = '\u148d'
mu = '\u14a7'
nu = '\u14c4'
su = '\u14f1'
lu = '\u14d7'
ju = '\u152a'
vu = '\u1557'
ru = '\u1548'
qu = '\u1581'
ngu = '\u1591'
lbaru = '\u15a2'

# u long syllabics
uu = '\u1406'
puu = '\u1434'
tuu = '\u1451'
kuu = '\u1470'
guu = '\u148e'
muu = '\u14a8'
nuu = '\u14c5'
suu = '\u14f2'
luu = '\u14d8'
juu = '\u152b'
vuu = '\u1558'
ruu = '\u1549'
quu = '\u1582'
nguu = '\u1592'
lbaruu = '\u15a3'

# Syllabic endings
h = '\u1426'
p = '\u1449'
t = '\u14bc'
k = '\u1483'
g = '\u14a1'
m = '\u14bb'
n = '\u14d0'
s = '\u1505'
l = '\u14ea'
j = '\u153e'
v = '\u155d'
r = '\u1550'
q = '\u1585'
ng = '\u1595'
lbar = '\u15a6'

# All of them together
syllabics = [
	[a,  pa,  ta,  ka,  ga,  ma,  na,  sa,  la,  ja,  va,  ra,  qa,  nga,  lbara],
	[aa, paa, taa, kaa, gaa, maa, naa, saa, laa, jaa, vaa, raa, qaa, ngaa, lbaraa],
	[i,  pi,  ti,  ki,  gi,  mi,  ni,  si,  li,  ji,  vi,  ri,  qi,  ngi,  lbari],
	[ii, pii, tii, kii, gii, mii, nii, sii, lii, jii, vii, rii, qii, ngii, lbarii],
	[u,  pu,  tu,  ku,  gu,  mu,  nu,  su,  lu,  ju,  vu,  ru,  qu,  ngu,  lbaru],
	[uu, puu, tuu, kuu, guu, muu, nuu, suu, luu, juu, vuu, ruu, quu, nguu, lbaruu],
	[h,  p,   t,   k,   g,   m,   n,   s,   l,   j,   v,   r,   q,   ng,   lbar]
]

# And their latin equivalent
latins = [
	["a",  "pa",  "ta",  "ka",  "ga",  "ma",  "na",  "sa",  "la",  "ja",  "va",  "ra",  "qa",  "nga",  "\u019aa"],
	["aa", "paa", "taa", "kaa", "gaa", "maa", "naa", "saa", "laa", "jaa", "vaa", "raa", "qaa", "ngaa", "\u019aaa"],
	["i",  "pi",  "ti",  "ki",  "gi",  "mi",  "ni",  "si",  "li",  "ji",  "vi",  "ri",  "qi",  "ngi",  "\u019ai"],
	["ii", "pii", "tii", "kii", "gii", "mii", "nii", "sii", "lii", "jii", "vii", "rii", "qii", "ngii", "\u019aii"],
	["u",  "pu",  "tu",  "ku",  "gu",  "mu",  "nu",  "su",  "lu",  "ju",  "vu",  "ru",  "qu",  "ngu",  "\u019au"],
	["uu", "puu", "tuu", "kuu", "guu", "muu", "nuu", "suu", "luu", "juu", "vuu", "ruu", "quu", "nguu", "\u019auu"],
	["-h", "-p",  "-t",  "-k",  "-g",  "-m",  "-n",  "-s",  "-l",  "-j",  "-v",  "-r",  "-q",  "-ng",  "-\u019a"]
]

# The size of these lists, and the maximum length of the strings in latins
nbLetterRows = len(latins)
nbLetterCols = min([len(row) for row in latins]) # They all have the same length, but min is just in case changes have to be made
maxLatinWidth = max([max([len(word) for word in row]) for row in latins]) # The complicated but general way of writing 4 (this is assuming the latin strings are longer than the on-screen size of the syllabics, which is a fair assumption)


# Prints the table of syllabics as a reference
def printSyllabics():
	tab = "  " # Small tabulation
	
	# Prints the table header
	for c in ["  ", " ", "p", "t", "k", "g", "m", "n", "s", "l", "j", "v", "r", "q", "ng", "\u019a"]:
		print(c, end = tab)
	print("") # '\n'
	
	# Prints each row
	firstCol = ["a ", "aa", "i ", "ii", "u ", "uu", "- "]
	for row in zip(firstCol, syllabics):
		print(row[0], end = tab)
		for c in row[1]:
			print(c, end = tab)
		print("") # '\n'



# Modules needed
from tkinter import *
from random import choice, randrange
from math import log10, floor

# Computes the number of digits to the left of the period
def nbDigits(x): return floor(log10(x)) + 1



# Menu interface class: Contains all the buttons and label
# Members:
#	Labels:
#		label1:		Latins to syllabics
#		label2:		Syllabics to latins
#	Buttons:
#		button1e:	Latins to syllabics, easy
#		button1m:	Latins to syllabics, medium
#		button1h:	Latins to syllabics, hard
#		button2e:	Syllabics to latins, easy
#		button2m:	Syllabics to latins, medium
#		button2h:	Syllabics to latins, hard
# Methods:
#	__init__:		Creates the object and places all the widgets
#	__del__:		Destroys the object and all the widgets
class menuInterface:
	def __init__(self, master):
		# First row
		self.label1 = Label(master, text = a + " \u2192 a")
		self.label1.grid(row = 0, column = 0, padx = menuLabelPadx, pady = menuPady)
		
		self.button1e = Button(master, text = "Easy", command = lambda: app.menuToGame(1, 1))
		self.button1e.grid(row = 0, column = 1, padx = menuButtonPadx, pady = menuPady)
		
		self.button1m = Button(master, text = "Medium", command = lambda: app.menuToGame(1, 2))
		self.button1m.grid(row = 0, column = 2, padx = menuButtonPadx, pady = menuPady)
		
		self.button1h = Button(master, text = "Hard", command = lambda: app.menuToGame(1, 3))
		self.button1h.grid(row = 0, column = 3, padx = menuButtonPadx, pady = menuPady)
		
		
		# Second row
		self.label2 = Label(master, text = "a \u2192 " + a)
		self.label2.grid(row = 1, column = 0, padx = menuLabelPadx, pady = menuPady)
		
		self.button2e = Button(master, text = "Easy", command = lambda: app.menuToGame(2, 1))
		self.button2e.grid(row = 1, column = 1, padx = menuButtonPadx, pady = menuPady)
		
		self.button2m = Button(master, text = "Medium", command = lambda: app.menuToGame(2, 2))
		self.button2m.grid(row = 1, column = 2, padx = menuButtonPadx, pady = menuPady)
		
		self.button2h = Button(master, text = "Hard", command = lambda: app.menuToGame(2, 3))
		self.button2h.grid(row = 1, column = 3, padx = menuButtonPadx, pady = menuPady)
	
	
	# Object destructor: Destroys every widget if they are not already destroyed
	def __del__(self):
		try:
			self.label1.destroy()
		except Exception:
			pass
		
		try:
			self.button1e.destroy()
		except Exception:
			pass
		
		try:
			self.button1m.destroy()
		except Exception:
			pass
		
		try:
			self.button1h.destroy()
		except Exception:
			pass
		
		try:
			self.label2.destroy()
		except Exception:
			pass
		
		try:
			self.button2e.destroy()
		except Exception:
			pass
		
		try:
			self.button2m.destroy()
		except Exception:
			pass
		
		try:
			self.button2h.destroy()
		except Exception:
			pass





# Game interface class: Contains all the buttons and label, and updates the text when necessary
# Members:
#	Non-widget variables:
#		nbPts:		Number of points made
#		nbErrs:		Number of errors made
#		nbRows:		Number of rows in the button grid
#		nbCols:		Number of columns in the button grid
#		source:		List of source letters (those that appear on qDisp)
#		dest:		List of destination letters (those that appear on the buttons)
#	Labels:
#		pointDisp:	Displays the number of points made
#		errorDisp:	Displays the number of errors made
#		qDisp:		Displays the symbol to translate
#	Buttons:
#		back:		Back button to return to the menu
#		buttons:	List of lists of buttons showing symbols to choose from
# Methods:
#	__init__:		Creates the object and places all the widgets
#	__del__:		Destroys the object and all the widgets
#	update:			Changes the texts and registers the points
class gameInterface:
	def __init__(self, master, nbRows, nbCols, source, dest):
		# Variables
		self.nbPts = 0 # Number of points
		self.nbErrs = 0 # Number of errors
		self.nbRows = nbRows
		self.nbCols = nbCols
		self.source = source
		self.dest = dest
		
		# First row
		self.back = Button(master, text = "\u21e6", command = app.gameToMenu) # Back button
		self.back.grid(row = 0, column = 0)
		
		self.pointDisp = Label(master, text = self.nbPts, fg = "green", width = statMinWidth, relief = "ridge")
		self.pointDisp.grid(row = 0, column = 1)
		
		self.errorDisp = Label(master, text = self.nbErrs, fg = "red", width = statMinWidth, relief = "ridge")
		self.errorDisp.grid(row = 0, column = 2)
		
		# Question display
		self.qDisp = Label(master, font = "-size " + str(qDispFontSize), width = maxLatinWidth)
		self.qDisp.grid(rowspan = nbRows, columnspan = 3)
		
		# Buttons
		self.buttons = []
		for i in range(nbRows):
			self.buttons.append([])
			for j in range(nbCols):
				self.buttons[i].append(Button(master, width = maxLatinWidth)) # TODO: See if it is possible to do this without indexing
				self.buttons[i][j].grid(row = i + 1, column = j + 3) # The 1 and 3 are hard coded because they depend on the other widgets
	
	
	# Object destructor: Destroys every widget if they are not already destroyed
	def __del__(self):
		try:
			self.pointDisp.destroy()
		except Exception:
			pass
		
		try:
			self.errorDisp.destroy()
		except Exception:
			pass
		
		try:
			self.qDisp.destroy()
		except Exception:
			pass
		
		try:
			self.back.destroy()
		except Exception:
			pass
		
		for row in self.buttons:
			for button in row:
				try:
					button.destroy()
				except Exception:
					pass
	
	
	def update(self, correct):
		# Registers the point or the error and updates their display (the explicit if and elseif are used to avoid giving a point or an error the first time update is called)
		if correct == True:
			self.nbPts += 1
			self.pointDisp.configure(text = self.nbPts, relief = "raised", width = max(statMinWidth, nbDigits(self.nbPts))) # The width is adjusted to fit the number if it becomes too large
			self.errorDisp.configure(relief = "ridge")
		elif correct == False:
			self.nbErrs += 1
			self.errorDisp.configure(text = self.nbErrs, relief = "raised", width = max(statMinWidth, nbDigits(self.nbErrs))) # The width is adjusted here as well
			self.pointDisp.configure(relief = "ridge")
		
		# Place random stuff on all the buttons and make them wrong answers
		picked = [] # Keeps track of what has already been picked to avoid duplicates # TODO: Study the possibility to use random.sample instead. Also, if I really have a lot of time on my hands, make it so that it doesn't cause any problem if there are more buttons than available symbols
		for row in self.buttons:
			for button in row:
				char = choice(choice(self.dest)) # Chooses a first random character
				while char in picked: # As long as it's already picked
					char = choice(choice(self.dest)) # Picks another one # NOTE: This loop will be infinite if there are more buttons than available symbols. It's also probably not very efficient if there are a lot of buttons
				picked.append(char) # Remembers the chosen symbol
				button.configure(text = char, command = lambda: self.update(False)) # Writes the text on the button and make it a wrong answer
		
		# Chooses one letter and one of the buttons, and makes them the correct answer
		i = randrange(nbLetterRows)
		j = randrange(nbLetterCols)
		char = self.dest[i][j] # Chooses a first random character
		while char in picked: # As long as it's already picked
			i = randrange(nbLetterRows)
			j = randrange(nbLetterCols)
			char = self.dest[i][j] # Picks another one # NOTE: This loop will be infinite if there are the same number of buttons and available symbols
		choice(choice(self.buttons)).configure(text = char, command = lambda: self.update(True)) # Changes a random button
		self.qDisp.configure(text = self.source[i][j]) # Sets the question display to the analogous text in the source set





# App class: Only used to keep references to the menu and the game so that transition between the two be possible
# Members:
#	menu:		Menu interface object
#	game:		Game interface object
#	master:		Master tkinter object
# Methods:
#	menuToGame:	Removes the menu and sets up the game
#	gameToMenu:	Removes the game and sets up the menu
class appClass:
	def __init__(self, master):
		self.master = master
		self.menu = menuInterface(master)
	
	
	# Removes the menu and sets up the game
	# Input:
	#	direction:	1 for inuktitut to latin, 2 for latin to inuktitut, else for an exception
	#	difficulty:	1 for easy, 2 for medium, 3 for hard, else for an exception
	def menuToGame(self, direction, difficulty):
		self.menu.__del__()
		del self.menu
		
		# Manually sets the lists for the direction
		if direction == 1:
			source = syllabics
			dest = latins
		elif direction == 2:
			source = latins
			dest = syllabics
		else:
			raise ValueError("menuToGame: direction does not have an allowed value")
		
		# Manually sets the number of rows and columns for the difficulty
		if difficulty == 1:
			nbRows = 3
			nbCols = 1
		elif difficulty == 2:
			nbRows = 3
			nbCols = 2
		elif difficulty == 3:
			nbRows = 3
			nbCols = 3
		else:
			raise ValueError("menuToGame: difficulty does not have an allowed value")
		
		self.game = gameInterface(self.master, nbRows, nbCols, source, dest)
		self.game.update(None)
	
	
	# Removes the game and sets up the menu
	def gameToMenu(self):
		self.game.__del__()
		del self.game
		self.menu = menuInterface(self.master)





### Main part of the script ###

master = Tk()
master.title("Inuktitut Syllabics") # Window title
master.resizable(width = False, height = False) # Makes the window unresizable
master.option_add("*font", str(generalFontSize)) # Sets the font size for all the text in the app (except for the ones that specify another value)

app = appClass(master)

master.mainloop()

