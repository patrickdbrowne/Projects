
#The idea is to use a messaging app on the emulator, click on the entry bar when texting someone, then turn on the 
#Script so words are individually sent to the victim very quickly. Test it on Notepad.

import pyautogui as pg
import keyboard as k
import time

class MassDestruction():
    def __init__(self):
        """ This opens file with the bee movie script and makes a list to iterate through
        The key parameter is the kye that has to be pressed to stop and start the writing """

        self.BeeMovieScript = open("Finished_Projects\Pyautogui\MassDestruction\HistorysGreatestWeapon.txt", "r")
        self.BeeMovieWords = self.BeeMovieScript.read().split()
        self.BeeMovieScript.close()
        self.stopped = False
        FAILSAFE = True
        time.sleep(3)
        self.destroy()

    def destroy(self):
        """ Iterates through all words in the list """

        while bool(self.BeeMovieWords) is True:
            if k.is_pressed("1") and self.stopped is False:
                self.change()
            
            self.stopped = False
            pg.typewrite(self.BeeMovieWords[0])
            #pg.leftClick()
            pg.press("enter")
            self.BeeMovieWords.pop(0)

    def change(self):
        """ This is to stop typing all the words whtoen space is hit """
        
        k.wait("1")
        self.stopped = True
        self.destroy()
        
        

MassDestruction()

# Put your cursor here when running the program because it might type here if something goes wrong:According
# aviation,thereis