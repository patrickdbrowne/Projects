from tkinter import *
from tkinter.tix import TEXT
from urllib import response
import requests
import ast
import subprocess
import os
from tkinter import messagebox
import pyttsx3

# global so it can be accessed in the actions.py file when needed
# global category
# global blacklist


BG_GREY = "#ABB289"
BG_COLOUR = "#17202A"
TEXT_COLOUR = "#EAECEE"

BG_DARK_BLUE = "#1D3557"
BG_BLUE = "#457B9D"
BG_LIGHT_BLUE = "#A8DADC"
BG_WHITE = "#F1FAEE"
BG_RED = "#E63946"

FONT = "Helvetica 14"
FONT_ENTRY = "Roboto 30"
FONT_BOLD = "Helvetica 13 bold"
FONT_BOLD_CHECKBOX = "Helvetica 16 bold"

# class MenuBar(Menu):
#     """Menubar in the ChattyBot application"""
#     def __init__(self, window):
#         Menu.__init__(self, window)

#         file = Menu(self, tearoff=False)
#         file.add_command(label="New")  
#         file.add_command(label="Open")  
#         file.add_command(label="Save")  
#         file.add_command(label="Save as")    
#         file.add_separator()
#         file.add_command(label="Exit", underline=1, command=self.quit)
#         self.add_cascade(label="File",underline=0, menu=file)
        
#         edit = Menu(self, tearoff=0)  
#         edit.add_command(label="Undo")  
#         edit.add_separator()     
#         edit.add_command(label="Cut")  
#         edit.add_command(label="Copy")  
#         edit.add_command(label="Paste")  
#         self.add_cascade(label="Edit", menu=edit) 

#         help = Menu(self, tearoff=0)  
#         help.add_command(label="About", command=self.about)  
#         self.add_cascade(label="Help", menu=help)  

#     def exit(self):
#         self.exit

#     def about(self):
#             messagebox.showinfo('PythonGuides', 'Python Guides aims at providing best practical tutorials')

class ChattyBot(Menu):

    def __init__(self):
        
        self.window = Tk()
        self.users_name = "User"

        # Runs virtual environment and runs NLU server. subprocess.run waits for it to finish. ";" indicates multiple commands UNCOMMENT THESE TWO WHEN TESTING/ USING
        NLU_server = subprocess.Popen('rasa run --enable-api', shell=True)
        actions_server = subprocess.Popen('cd actions && rasa run actions', shell=True)


        # subprocess.run(['NLU_server'], stdout=subprocess.PIPE, input='rasa run --enable-api')
        # # Runs actions server
        # subprocess.run(['Actions_server'], stdout=subprocess.PIPE, text=True, input='conda activate env', shell=True)
        # subprocess.run(['Actions_server'], stdout=subprocess.PIPE, text=True, input='cd actions', shell=True)
        # subprocess.run(['Actions_server'], stdout=subprocess.PIPE, text=True, input='rasa run actions', shell=True)

        # Runs virtual environment and actions server

        # NLU server
        self.url = "http://localhost:5005/webhooks/rest/webhook"
        
        self.engine = pyttsx3.init()
        self.voice = False

        # Number of files in the "conversations" directory to keep track of conversations
        self.number = len(os.listdir(".\conversations")) + 1
        self.popup_name()


    def run(self):
        """Runs application"""

        self.window.mainloop()

    def _setup_main_window(self):
        """Configures root window"""

        self.window.title("ChattyBot")
        # Icon in window
        self.window.iconbitmap("little_robot_sh.ico")
            
        # # create the file object)
        # edit = Menu(menu)

        # # adds a command to the menu option, calling it exit, and the
        # # command it runs on event is client_exit
        # edit.add_command(label="Undo")

        # #added "file" to our menu
        # menu.add_cascade(label="Edit", menu=edit)


        # help = Menu(menu)
        # help.add_cascade(label="Help", menu=help)

        # send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GREY, command=lambda: self._on_enter_pressed(None))
        # send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        # If true, then window can be resized
        self.window.resizable(width=False, height=False)



        # # head label
        # # pady moves label down a bit
        # head_label = Label(self.window, bg=BG_COLOUR, fg=TEXT_COLOUR, text="Welcome", font=FONT_BOLD, pady=10)
        # # Number between 0 and 1. 1 indicates takes whole width of window
        # head_label.place(relwidth=1)

        # divider between head label and user inputs
        line = Label(self.window, width=450, bg=BG_BLUE)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget - 20 characters wide, 2 characters high, padding
        # padding x in tupple is to stop the text sliding under the scroll bar
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_WHITE, fg=BG_DARK_BLUE, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        # Disable so only text can be displayed
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar - only for text widget
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        # command changes y-position of widget to view more
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label - for entry box background
        self.bottom_label = Label(self.window, bg=BG_BLUE, height=80)
        self.bottom_label.place(relwidth=1, rely=0.825)

        # Making a frame for entry box and cursor caret type
        entry_frame = Frame(self.bottom_label, bg=BG_DARK_BLUE, cursor="xterm")
        entry_frame.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        
        # text entry box
        self.msg_entry = Entry(self.bottom_label, bg=BG_DARK_BLUE, fg=TEXT_COLOUR, font=FONT_ENTRY, borderwidth=0, insertbackground=BG_WHITE)
        self.msg_entry.place(relwidth=0.69, relheight=0.06, rely=0.008, relx=0.03)

        # Label for entry box - move cursor to the right
        # self.entry_label = Label(self.window, bg=BG_BLUE)
        # self.entry_label.place(relwidth=0.05, relheight=0.06, rely=0.008, relx=0)
        # automatically selected when app is opened
        self.msg_entry.focus()
        # Allows message to be sent via enter key in addition send button
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button - calls function via lambda
        send_button = Button(self.bottom_label, text="Send", font=FONT_BOLD, fg=BG_WHITE, activeforeground=BG_DARK_BLUE, width=20, bg=BG_BLUE, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
        # # Create value for an option in "Settings"
        # setting_value = StringVar(self.window, "Settings")
        
        # settings = OptionMenu(self.window, setting_value, "Export Conversation", "Exit")
        # settings.place(relx=0, rely=0, relheight=0.1875, relwidth=0.25)
        var = StringVar()
        label = Label(self.window, textvariable=var)
        # Menubutton automatically highlights when mouse hovers button, so active background makes it same colour
        self.menubutton = Menubutton(self.window, text="Settings", borderwidth=1, relief="ridge", indicatoron=False, font=FONT_BOLD, bg=BG_BLUE, fg=BG_WHITE, activeforeground=BG_WHITE, activebackground=BG_BLUE)
        self.menu = Menu(self.menubutton, tearoff=False)
        self.menubutton.configure(menu=self.menu)
        self.menu.add_radiobutton(label="Export Conversation", variable=var, value="Export Conversation", command=self._export_convo)
        self.menu.add_radiobutton(label="Edit Joke Settings", variable=var, value="Edit Joke Settings", command=self._joke_settings)
        self.menu.add_radiobutton(label="Edit Voice Settings", variable=var, value="Edit Voice Settings", command=self._voice_settings)
        self.menu.add_radiobutton(label="Exit", variable=var, value="Exit", command=self.exitApp)

        # label.pack(side="bottom", fill="x")
        self.menubutton.place(relx=0, rely=0, relheight=0.07, relwidth=0.25)

        # Help button for main menu
        self.help = Button(self.window, text="Help", font=FONT_BOLD, width=20, bg=BG_BLUE, fg=BG_WHITE, borderwidth=1, activeforeground=BG_WHITE, relief="ridge", activebackground=BG_BLUE, command=self._help_screen)
        self.help.place(relx=0.25, rely=0, relheight=0.07, relwidth=0.25)

        # Voice button for main menu
        self.voice_button = Button(self.window, text="Voice: Off", font=FONT_BOLD, width=20, bg=BG_BLUE, fg=BG_WHITE, activeforeground=BG_WHITE, borderwidth=1, relief="ridge", activebackground=BG_BLUE, command=self._toggle_voice)
        self.voice_button.place(relx=0.5, rely=0, relheight=0.07, relwidth=0.25)

        # Clear conversation button for main menu
        self.convo_button = Button(self.window, text="Clear Conversation", font=FONT_BOLD, width=20, bg=BG_BLUE, fg=BG_WHITE, activeforeground=BG_WHITE, borderwidth=1, relief="ridge", activebackground=BG_BLUE, command=self._clear_text)
        self.convo_button.place(relx=0.75, rely=0, relheight=0.07, relwidth=0.25)

  
        # give widget attributes with .configure(). dimensions correspond with screen aspect ratio 4:3
        self.window.configure(width=733.33, height=550, bg=BG_COLOUR)

    def _voice_settings(self):
        """Shows voice settings to change gender of voice, voice volume, and voice rate"""
        # Creates a window which can be destroyed
        self.voice_settings_window = Toplevel()
        self.voice_settings_window.wm_title("Change Voice Settings!")
        self.voice_settings_window.resizable(width=False, height=False)

        # Image icon on help screen in program
        self.voice_settings_window.iconbitmap(r".\\address_book.ico")

        # Disables menu button for "edit joke settings" so no more than 1 window appears
        self.menu.entryconfig(2, state=DISABLED)
        self.voice_settings_window.protocol("WM_DELETE_WINDOW", self._voice_settings_window_close)

        self.voice_settings_window.configure(width=733.33, height=550, bg=BG_WHITE)
    
    def _voice_settings_window_close(self):
        """Enables the voice index in main menu when corresponding window closes"""
        self.voice_settings_window.destroy()
        self.menu.entryconfig(2, state=NORMAL)

    def _joke_settings(self):
        """Shows joke settings to change black list etc."""
        # Creates a window which can be destroyed
        self.jokes_setting_window = Toplevel()
        self.jokes_setting_window.wm_title("Joke Settings!")
        self.jokes_setting_window.resizable(width=False, height=False)

        # Image icon on help screen in program
        self.jokes_setting_window.iconbitmap(r".\\address_book.ico")

        self.jokes_setting_window.configure(width=733.33, height=550, bg=BG_WHITE)
        # Blacklist subtitle
        self.blacklist = Label(self.jokes_setting_window, text="Blacklist:", font=FONT_ENTRY, fg=BG_DARK_BLUE, bg=BG_WHITE)
        self.blacklist.place(rely=0.05, relx=0.05)

        # Categories subtitle
        self.categories = Label(self.jokes_setting_window, text="Categories:", font=FONT_ENTRY, fg=BG_DARK_BLUE, bg=BG_WHITE)
        self.categories.place(rely=0.05, relx=0.5)

        # Making a checkbox for types of jokes the user wants - Checkboxes are in intervals of 15.833...% vertically

        # BLACKLIST
        # NSFW checkbox
        self.nsfw_value = IntVar()
        self.nsfw_checkbutton = Checkbutton(self.jokes_setting_window, text="NSFW", variable=self.nsfw_value, onvalue=0, offvalue=1, fg=BG_DARK_BLUE, bg=BG_WHITE, activeforeground=BG_DARK_BLUE, activebackground=BG_WHITE, padx=5, font=FONT_BOLD_CHECKBOX)
        self.nsfw_checkbutton.place(rely=0.1857142857, relx=0.05)

        # Religious checkbox
        self.religious_value = IntVar()
        self.religious_checkbutton = Checkbutton(self.jokes_setting_window, text="Religious", variable=self.religious_value, onvalue=0, offvalue=1, fg=BG_DARK_BLUE, bg=BG_WHITE, activeforeground=BG_DARK_BLUE, activebackground=BG_WHITE, padx=5, font=FONT_BOLD_CHECKBOX)
        self.religious_checkbutton.place(rely=0.3214285714, relx=0.05)

        # Political checkbox
        self.political_value = IntVar()
        self.political_checkbutton = Checkbutton(self.jokes_setting_window, text="Political", variable=self.political_value, onvalue=0, offvalue=1, fg=BG_DARK_BLUE, bg=BG_WHITE, activeforeground=BG_DARK_BLUE, activebackground=BG_WHITE, padx=5, font=FONT_BOLD_CHECKBOX)
        self.political_checkbutton.place(rely=0.4571428571, relx=0.05)

        # Racist checkbox
        self.racist_value = IntVar()
        self.racist_checkbutton = Checkbutton(self.jokes_setting_window, text="Racist", variable=self.racist_value, onvalue=0, offvalue=1, fg=BG_DARK_BLUE, bg=BG_WHITE, activeforeground=BG_DARK_BLUE, activebackground=BG_WHITE, padx=5, font=FONT_BOLD_CHECKBOX)
        self.racist_checkbutton.place(rely=0.5928571429, relx=0.05)

        # Sexist checkbox
        self.sexist_value = IntVar()
        self.sexist_checkbutton = Checkbutton(self.jokes_setting_window, text="Sexist", variable=self.sexist_value, onvalue=0, offvalue=1, fg=BG_DARK_BLUE, bg=BG_WHITE, activeforeground=BG_DARK_BLUE, activebackground=BG_WHITE, padx=5, font=FONT_BOLD_CHECKBOX)
        self.sexist_checkbutton.place(rely=0.7285714286, relx=0.05)

        # Explicit checkbox
        self.explicit_value = IntVar()
        self.explicit_checkbutton = Checkbutton(self.jokes_setting_window, text="Explicit", variable=self.explicit_value, onvalue=0, offvalue=1, fg=BG_DARK_BLUE, bg=BG_WHITE, activeforeground=BG_DARK_BLUE, activebackground=BG_WHITE, padx=5, font=FONT_BOLD_CHECKBOX)
        self.explicit_checkbutton.place(rely=0.8642857143, relx=0.05)
        
        
        # CATEGORIES - automatically checked
        # Programming checkbox
        self.programming_value = IntVar()
        self.programming_checkbutton = Checkbutton(self.jokes_setting_window, text="Programming", variable=self.programming_value, onvalue=0, offvalue=1, fg=BG_DARK_BLUE, bg=BG_WHITE, activeforeground=BG_DARK_BLUE, activebackground=BG_WHITE, padx=5, font=FONT_BOLD_CHECKBOX)
        self.programming_checkbutton.place(rely=0.1857142857, relx=0.5)

        # Miscellaneous checkbox
        self.miscellaneous_value = IntVar()
        self.miscellaneous_checkbutton = Checkbutton(self.jokes_setting_window, text="Miscellaneous", variable=self.miscellaneous_value, onvalue=0, offvalue=1, fg=BG_DARK_BLUE, bg=BG_WHITE, activeforeground=BG_DARK_BLUE, activebackground=BG_WHITE, padx=5, font=FONT_BOLD_CHECKBOX)
        self.miscellaneous_checkbutton.place(rely=0.3214285714, relx=0.5)

        # Pun checkbox
        self.pun_value = IntVar()
        self.pun_checkbutton = Checkbutton(self.jokes_setting_window, text="Pun", variable=self.pun_value, onvalue=0, offvalue=1, fg=BG_DARK_BLUE, bg=BG_WHITE, activeforeground=BG_DARK_BLUE, activebackground=BG_WHITE, padx=5, font=FONT_BOLD_CHECKBOX)
        self.pun_checkbutton.place(rely=0.4571428571, relx=0.5)

        # Spooky checkbox
        self.spooky_value = IntVar()
        self.spooky_checkbutton = Checkbutton(self.jokes_setting_window, text="Spooky", variable=self.spooky_value, onvalue=0, offvalue=1, fg=BG_DARK_BLUE, bg=BG_WHITE, activeforeground=BG_DARK_BLUE, activebackground=BG_WHITE, padx=5, font=FONT_BOLD_CHECKBOX)
        self.spooky_checkbutton.place(rely=0.5928571429, relx=0.5)

        # Christmas
        self.christmas_value = IntVar()
        self.christmas_checkbutton = Checkbutton(self.jokes_setting_window, text="Christmas", variable=self.christmas_value, onvalue=0, offvalue=1, fg=BG_DARK_BLUE, bg=BG_WHITE, activeforeground=BG_DARK_BLUE, activebackground=BG_WHITE, padx=5, font=FONT_BOLD_CHECKBOX)
        self.christmas_checkbutton.place(rely=0.7285714286, relx=0.5)

        # Dark checkbox
        self.dark_value = IntVar()
        self.dark_checkbutton = Checkbutton(self.jokes_setting_window, text="Dark", variable=self.dark_value, onvalue=0, offvalue=1, fg=BG_DARK_BLUE, bg=BG_WHITE, activeforeground=BG_DARK_BLUE, activebackground=BG_WHITE, padx=5, font=FONT_BOLD_CHECKBOX)
        self.dark_checkbutton.place(rely=0.8642857143, relx=0.5)
        self.dark_checkbutton.toggle()

        # Disables menu button for "edit joke settings" so no more than 1 window appears
        self.menu.entryconfig(1, state=DISABLED)
        self.jokes_setting_window.protocol("WM_DELETE_WINDOW", self._jokes_settings_window_close)
        
        # self.blacklist_choices = ("nsfw", "religious", "political", "racist", "sexist", "explicit") <-- CASE SENSITIVE
        # self.category_choices = ("Programming", "Miscellaneous", "Pun", "Spooky", "Christmas")

    def _jokes_settings_window_close(self):
        """Enables the jokes index in main menu when corresponding window closes"""
        global category
        global blacklist
        # Checks the value of each checkbox and sends it to the jokes class in actions.py - updates blacklist and categories in jokes
        # default values
        category = ["Programming,Miscellaneous,Pun,Spooky,Christmas"]
        blacklist = ["nsfw,religious,political,racist,sexist,explicit"]
        # Create category list to post to jokes api as necessary
        category_copy = ""
        blacklist_copy = ""

        # Adds word to list if it's in string and turned off
        if self.programming_value.get() == 0:
            category_copy += "Programming," # Remove "Programming," etc.
        if self.dark_value.get() == 0:
            category_copy += "Dark,"
        if self.miscellaneous_value.get() == 0:
            category_copy += "Miscellaneous,"
        if self.pun_value.get() == 0:
            category_copy += "Pun,"
        if self.spooky_value.get() == 0:
            category_copy += "Spooky,"
        if self.christmas_value.get() == 0:
            category_copy += "Christmas"
        if len(category_copy) > 0:
            if category_copy[-1] == ",":
                category_copy = category_copy[:-1]
        
        # Adds word to list if it is on
        # Create blacklist list to post to jokes api as needed
        if self.nsfw_value.get() == 0:
            blacklist_copy += "nsfw,"
        if self.religious_value.get() == 0:
            blacklist_copy += "religious,"
        if self.political_value.get() == 0:
            blacklist_copy += "political,"
        if self.racist_value.get() == 0:
            blacklist_copy += "racist,"
        if self.sexist_value.get() == 0:
            blacklist_copy += "sexist,"
        if self.explicit_value.get() == 0:
            blacklist_copy += "explicit"
        if len(blacklist_copy) > 0:
            if blacklist_copy[-1] == ",":
                blacklist_copy = blacklist_copy[:-1]
        
        # Changing global variables
        blacklist.append(blacklist_copy)
        blacklist.pop(0)

        category.append(category_copy)
        category.pop(0)

        action_blacklist = blacklist
        action_category = category

        print(action_blacklist)
        print(action_category)

        # print(blacklist, category)

        self.jokes_setting_window.destroy()
        self.menu.entryconfig(1, state=NORMAL)

    def _clear_text(self):
        """Clear the conversation on screen"""
        self.text_widget.configure(state=NORMAL)
        self.text_widget.delete("1.0", END)
        self.text_widget.configure(state=DISABLED)

    def _export_convo(self):
        """Export the conversation on screen into a text file - """
        conversation = self.text_widget.get("1.0", END)
        with open(".\conversations\conversation{}.txt".format(self.number), "w") as file:
            file.write(conversation)

        self.number += 1

    def _help_screen(self):
        """Displays help screen with instructions to inform user how to use program"""
        # Creates a window which can be destroyed
        self.help_window = Toplevel()
        self.help_window.wm_title("How to Use ChattyBot!")
        self.help_window.resizable(width=False, height=False)

        # Image icon on help screen in program
        self.help_window.iconbitmap(r".\\address_book.ico")

        self.help_window.configure(width=733.33, height=550, bg=BG_WHITE)

        # Disable help button so as to not produce more "help" screens
        self.help.configure(state=DISABLED)

        self.help_window.protocol("WM_DELETE_WINDOW", self._help_window_close)

    def _help_window_close(self):
        """ when help window closes, the help button is enabled so it can be reopened. 
        Prevents multiple instances of the same window."""
        self.help_window.destroy()
        self.help.configure(state=NORMAL)

    def _on_enter_pressed(self, event):
        """Retrieves message"""
        msg = self.msg_entry.get()
        self._insert_message(msg, self.users_name)
    
    def _insert_message(self, msg, sender):
        """Displays user's message in text area"""
        # If user returns ""
        if not msg:
            return
        
        # Delete message in the textbox
        self.msg_entry.delete(0, END)

        # format user's message to display
        msg1 = "{}: {}\n\n".format(sender, msg)
        # change state of text box momentarily so string can be appended there, then disable it so it can't be typed on later
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        # Connects to my RASA program
        NLU_Object = {
        "message": msg,
        "sender": self.users_name,
        }

        # gives message to rasa server
        str_message_data = requests.post(self.url, json=NLU_Object)
        # turns returned stringed dictionary into a dictionary
        message_data = ast.literal_eval(str_message_data.text)

        # Iterates through multiple message objects that need to have it's texts displayed in succession
        for response in range(len(message_data)):
            bot_response = message_data[response]["text"]
            msg2= "ChattyBot: {}\n\n".format(bot_response)
            # change state of text box momentarily so string can be appended there, then disable it so it can't be typed on later
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg2)
            self.text_widget.configure(state=DISABLED)

            # Always allows user to see last message sent (scrolls down)
            self.text_widget.see(END)

        # Orates the bot's message if the voice button is turned on
        if self.voice:
            self.engine.say(bot_response)
            self.engine.runAndWait()

    def _toggle_voice(self):
        """Toggles the voice in the chatbot and text in button"""
        if self.voice:
            self.voice_button.config(text="Voice: Off")
            self.voice = False
        else:
            self.voice_button.config(text="Voice: On")
            self.voice = True

    def popup_name(self):
        """A pop up window to get the user's name"""

        # Creates a window which can be destroyed
        self.win = Toplevel()
        self.win.wm_title("Name")

        # Name label
        self.name_label = Label(self.win, text="What's your name?")
        self.name_label.grid(row=0, column=0)

        # Entry box
        self.name_box = Entry(self.win, text="")
        self.name_box.bind("<Return>", self._get_name)
        self.name_box.grid(row=1,column=0)

    def _get_name(self, event):
        """Gets user name then destroys window"""
        self.name = self.name_box.get()
        # Stops anything from happening if user doesn't enter anything
        if self.name == "":
            return

        elif self.name != "":
            self.users_name = self.name
            
            # Creates main program once name has been entered
            # creates layout of window widget
            self._setup_main_window()

            self.win.destroy()

    def exitApp(self):
        """Exit app"""
        exit()



if __name__ == "__main__":   
    app = ChattyBot()
    app.run()
