# WARNING: it raises your volume to the max and rick rolls, so change it to "volumedown" when testing

class RickRoll():
    import pyautogui as pg 
    # import modules before __init__ and say self.pg or self.pyautogui
    import time as t

    def __init__(self, link=None):
        """ init stage """
        
        if link is None:
            self.link = "https://www.youtube.com/watch?v=oHg5SJYRHA0"
        else:
            self.link = link
        self.pg.FAILSAFE = False
        self.troll()

    def troll(self):
        """ plays the link provided or rick roll """

        self.pg.hotkey("win", "r")
        self.pg.typewrite("microsoft-edge:")
        self.pg.press("enter")
        self.t.sleep(3)
        self.pg.hotkey("alt", "d", interval=0.1)
        self.pg.typewrite(self.link)
        self.pg.press("enter")
        for x in range(100):
            self.pg.press("volumeup")
        self.t.sleep(1)
        self.pg.press("f")




RickRoll()
        

