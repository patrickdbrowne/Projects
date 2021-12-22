"""
USE PYTHON 3.9 OTHERWISE THE PROGRAM WILL NOT WORK (shoulda used a virtual environment)
Minewalker is a game where the player aims to cross a field without
a mine.
"""
import msvcrt, random, os, time, ast
from random import randint
from termcolor import colored

class Main():
    """
    Minewalker
    """
    def __init__(self, x=10, y=10, mines=15, player=' 0 ', colour=None, trail=' # ', wait=3, climit=3, rstart=True, mode='custom') -> None:
        """
        Constructor
        """
        self.array = []
        self.yValue = y
        self.xValue = x
        self.numMines = mines
        self.user = colored(player, colour)
        self.running = True
        self.running = True
        self.key = ''
        self.yPosition = randint(0, self.yValue - 1)
        self.xPosition = 0
        self.blankField= []
        self.trail = trail
        self.coordinates = []
        self.wait = wait
        self.starting = True
        self.yes = ["yes", "ye", "y"]
        self.yUser = random.randint(0, self.yValue-1)
        self.checking = False
        self.xCheck = 0
        self.yCheck = 0
        self.climit = climit
        self.xstart = 0
        self.ystart = 0
        self.yend = 0
        self.xend = 2
        self.rstart = rstart
        self.mode = mode
        self.hScores = None
        self.start_time = time.time()
        self.total_time = 0
        self.name = ''
        self.base = [[], [], [], []]
        self.score = []
        self.content = ''
    def minefield(self) -> list:
        """
        Returns the minefield
        """

        # This appends the number of rows
        # to the array
        for row in range(self.yValue):
            self.subarray = []

            # The following loop appends the number
            # of columns to each row, denoted by '_'
            for column in range(self.xValue):
                self.subarray.append(' _ ')

            # This appends each row to the array,
            # creating a new row
            self.array.append(self.subarray)

        # iterates through each row, assigning
        # a bomb to a random position in that row
        for mine in range(self.numMines):
            self.randomColumn = random.randint(0, self.xValue-1)
            self.rownum = self.array[mine % self.yValue]
            self.rownum[self.randomColumn] = colored(' @ ', 'red')

            # appends the coordinates of the mine to a list. Coordinates are from top left to bottom right
            self.coordinates.append((self.randomColumn, mine % self.yValue))

        if self.rstart == False:
            self.yPosition = 0
            self.xPosition = 0

        # Removes a bomb if its in the user's starting position. This happens rarely. while is to ensure it
        # does not happen again even after adding another mine.
        while (self.xPosition, self.yPosition) in self.coordinates:
            # Removes user's position from list if it exists
            self.coordinates.remove((self.xPosition, self.yPosition))

            self.randomColumn = random.randint(0, self.xValue-1)
            self.rownum = self.array[self.yUser]
            self.rownum[self.randomColumn] = colored(' @ ', 'red')
            self.coordinates.append((self.randomColumn, self.yUser))

        # Checks for mines in the last column and removes them
        for (x, y) in self.coordinates.copy():
            if self.xValue-1 == x:
                self.array[y][x]= ' _ '
                self.coordinates.remove((x, y))
            else:
                continue

        # Places the user on a random row in the first column or in the
        # top-left corner

        self.array[self.yPosition][self.xPosition] = self.user

        self.refresh()

    def refresh(self):
        """
        Refreshes the minefield and prints it to the console
        It prints the array's elements as a table.
        """

        # clears previous output
        os.system('cls')
        for row in self.array:
            for element in row:
                print(element, end='')
            print('\n', end='')

        # Displays the normal field after the timer
        if self.starting == True:
            time.sleep(self.wait)
            for x, y in self.coordinates:
                # replaces each bomb with normal ' _ ' symbol to hide it after timer
                self.array[y][x] = ' _ '
            self.starting = False
            self.refresh()

        # Checks to see if the player wins by checking its on the last column
        if self.xPosition == self.xValue - 1:
            self.win()

        # checks if the player is on a mine by seeing if its matched coordinates.
        if (self.xPosition, self.yPosition) in self.coordinates:
            self.game_over()

        if self.checking == True:
            self.check()
        self.player()

    def player(self):
        """
        Creates player and moves them around the board with inputs
        """

        # Conditions to determine the new position of the user while in index

        self.key = ord(msvcrt.getch())
        if self.key == 119:
            self.yPosition -= 1
        if self.key == 97:
            self.xPosition -= 1
        if self.key == 115:
            self.yPosition += 1
        if self.key == 100:
            self.xPosition += 1
        if self.key == 32:
            if self.climit > 0:
                self.check()

        # brings user up by 1 to cancel
        if self.yPosition > self.yValue - 1:
            self.yPosition -= 1
        if self.yPosition < 0:
            self.yPosition += 1
        if self.xPosition > self.xValue - 1:
            self.xPosition -= 1
        if self.xPosition < 0:
            self.xPosition += 1

        # Checks whether user is in each row of the field. If it is
        # then it replaces the user with a hashtag (or trail) before
        # replacing another element with the user to look like its
        # moving.
        for row in self.array:
            if self.user in row:
                row[row.index(self.user)] = self.trail
            else:
                continue

        self.array[self.yPosition][self.xPosition] = self.user
        self.refresh()

    def check(self):
        """
        Checks the surrounding squares around the user for bombs with the space bar
        """

        # Checks if the coordinates of the surrounding squares of the user
        # has mines or vacant squares.

        # These conditions control index error when the function is used
        if self.xPosition == 0:
            self.xstart = 0
        if self.xPosition != 0:
            self.xstart = -1

        if self.yPosition == 0:
            self.ystart = 0
            self.yend = 2
        if 0 < self.yPosition < self.yValue - 1:
            self.ystart = -1
            self.yend = 2
        if self.yPosition == self.yValue - 1:
            self.ystart = -1
            self.yend = 1

        # A loop to 'discover' the squares around the user's current position
        for yValue in range(self.ystart, self.yend):
            self.yCheck = self.yPosition + yValue
            for xValue in range(self.xstart, self.xend):
                self.xCheck = self.xPosition + xValue
                # checks if its in index range in list
                if (self.xCheck, self.yCheck) in self.coordinates:
                    self.array[self.yCheck][self.xCheck] = colored(' @ ', 'red')
                else:
                    self.array[self.yCheck][self.xCheck] = self.trail

        # Changes current position of the user to its symbol
        self.array[self.yPosition][self.xPosition] = self.user

        # climit is 'check limit' which just makes sure the user can use this function
        # a certain number of times
        self.climit -= 1
        self.refresh()

    def game_over(self):
        """
        Ends the game when someone lands on a mine
        """
        self.display_end()
        print('Game Over!')
        self.repeat()

    def repeat(self):
        """
        Asks user whether the want to repeat the game
        """

        answer = input("Would you like to repeat?\n")
        if answer.lower() in self.yes:
            os.system('cls')
            UI().settings()
        else:
            self.hScores = open('High_Scores.txt', 'r')
            self.content = ast.literal_eval(self.hScores.read())
            print("Thanks for Playing !!")
            print("Here are the current High Scores:\n")
            for difficulty in self.content:
                if difficulty == self.content[0]:
                    print("EASY")
                    print("--------------------")
                elif difficulty == self.content[1]:
                    print("\nMEDIUM")
                    print("--------------------")
                elif difficulty == self.content[2]:
                    print("\nHARD")
                    print("--------------------")
                elif difficulty == self.content[3]:
                    print("\nIMPOSSIBLE")
                    print("--------------------")
                
                for ranking in range(5):
                    try:
                        print(f"Number {ranking+1}: {sorted(difficulty)[ranking][1]}, {round(sorted(difficulty)[ranking][0], 2)}")
                    except:
                        print(f"Number {ranking+1}: None")
            

            quit()

    def display_end(self):
        """
        Displays the board when the game ends
        """
        os.system('cls')

        for x, y in self.coordinates:
            # replaces each bomb with normal ' _ ' symbol to hide it after timer
            self.array[y][x] = colored(' @ ', 'red')

        for row in self.array:
            for element in row:
                print(element, end='')
            print('\n', end='')

    def win(self):
        """
        Ends the game and exposes the mines
        """
        self.total_time = time.time() - (self.start_time + self.wait)
        self.display_end()
        print('You Win!')
        self.high_score()
    
    def high_score(self):

        self.name = input("What is your syndicate name? ")
        # writes list to file if non-existent
        if not os.path.isfile('High_Scores.txt'):
            self.hScores = open('High_Scores.txt', 'w')
            self.hScores.write(str(self.base))
            self.hScores.close()
        
        self.score = [self.total_time, self.name]
        self.hScores = open("High_Scores.txt", "r")
        self.content = ast.literal_eval(self.hScores.read())
        self.hScores.close()

        # places the scores in different lists inside the array based
        # on level of difficulty
        if self.mode == 'easy':
            self.content[0].append(self.score)
            
        elif self.mode == 'medium':
            self.content[1].append(self.score)

        elif self.mode == 'hard':
            self.content[2].append(self.score)

        elif self.mode == 'impossible':
            self.content[3].append(self.score)
        else:
            self.repeat()
        
        self.hScores = open("High_Scores.txt", "w")
        self.hScores.write(str(self.content))
        self.hScores.close()

        self.repeat()


class UI():
    def __init__(self):
        """ Default values
        """

        self.x = 10
        self.y = 10
        self.mines = 15
        self.player = ' 0 '
        self.colour = None
        self.trail = ' # '
        self.wait = 3
        self.valid = True
        self.climit = 5
        self.rstart = False
        self.mode = ''
        self.colours = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        print(f"""
        Currently, your default settings are as follows:
        Player: {self.player}
        Colour: {self.colour}
        trail: {self.trail}
        Your player and trail can only be one character long. To view all of the available colours,
        click !colours when asked to enter a colour. To use the default settings for any of the
        aesthetic features, hit 'Enter'.
        """)

    def settings(self):
        """
        Defines settings of the game
        """
        # The following mainly changes the aesthetics of the game
        self.change = input("Would you like to change your customisations? (Y/N) ").lower()

        # If the user wants to change their character, colour, or trail
        if self.change in ['y', 'ye', 'yes']:

            # The symbol representing the character
            self.player = f' {input("Symbol for your user: ")} '
            # Checks symbol is one symbol long, as two spaces surround it
            while len(self.player) > 3:
                self.player = f' {input("Your user must be one character long: ")} '
            # If it is only the spaces, then nothing was entered and therefore reverts to default
            if len(self.player) == 2:
                self.player = ' 0 '

            # The colour of the character
            print("You can type '!colours' to see the available colours.")
            while self.valid:
                self.colour = input("Colour: ")
                # Checks its a valid colour
                if self.colour.lower() in self.colours:
                    self.valid = False
                # If nothing was entered, it just shows white text
                elif bool(self.colour) == False:
                    self.colour = None
                    self.valid = False

                elif self.colour == '!colours':
                    print(self.colours)
                # If colour is not in the list
                elif self.colour.lower() not in self.colours:
                    print("Please type a valid colour.")

            # Trail of the character
            self.trail = f' {input("Trail: ")} '
            # Checks trail is only one character long
            while len(self.trail) > 3:
                self.trail = f' {input("Your trail must be one character long: ")} '
            # Checks if nothing was entered, reverting the trail to default
            if len(self.trail) == 2:
                self.trail = ' # '

        # The following changes the settings based on the level of difficulty
        self.setting = input("What difficulty would you like to play (Easy, Medium, Hard, Impossible, Custom). ").lower()
        if self.setting in ['easy', 'medium', 'hard', 'impossible', 'custom']:
            if self.setting == 'easy':
                self.x = 5
                self.y = 5
                self.mines = 5
                self.mode = 'easy'

            elif self.setting == 'medium':
                self.mode = 'medium'

            elif self.setting == 'hard':
                self.x = 20
                self.y = 15
                self.mines = 40
                self.wait = 5
                self.mode = 'hard'

            elif self.setting == 'impossible':
                self.x = 20
                self.y = 15
                self.mines = 70
                self.wait = 1
                self.mode = 'impossible'

            elif self.setting == 'custom':
                try:
                    self.x = int(input("How many units wide would you like the field to be? "))
                    self.y = int(input("How many units high would you like the field to be? "))
                    self.mines = int(input("How many mines would you like to have in the game? "))
                    self.wait = int(input("How many seconds would you like for the mines to be on the screen? "))
                    self.climit = int(input("How many times would you like to use the 'checking' function? "))
                    self.rstart = input("Type 'R' if you would like to start in a random position, otherwise hit 'Enter' ").lower()
                    if self.rstart == 'r':
                        self.rstart = True
                    else:
                        self.rstart = False
                    self.mode = 'custom'
                except:
                    print("Please enter a valid argument.")
                    self.settings()
            self.start()
        else:
            print("Please enter a valid argument.")
            self.settings()


    def start(self):
        Main(player=self.player, colour=self.colour, trail=self.trail, x=self.x, y=self.y, mines=self.mines, wait=self.wait, climit=self.climit, rstart=self.rstart, mode=self.mode).minefield()

if __name__ == '__main__':
    print("""
        Welcome to MineWalker.

        The aim of the game is to cross a field of mines and reach the other side.
        You will be given a certain amount of time to memorise the position of the mines,
        after which you will need to cross the field. Use the keys WASD to move around the board.
        Use the SpaceBar to use your checking function. Remember, you can only use this 3 times (unless
        you're in custom).""")
    UI().settings()