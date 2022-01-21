from tkinter import *

BG_GRAY = "#ABB289"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:

    def __init__(self):
        self.window = Tk()
        #creates layout of window widget
        self._setup_main_window()
    
    def run(self):
        self.window.mainloop()
    
    def _setup_main_window(self):
        self.window.title("Chat")
        # If true, then window can be resized
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)

if __name__ == "__main__":
    app = ChatApplication()
    app.run()
