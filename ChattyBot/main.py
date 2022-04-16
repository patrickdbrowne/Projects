from tkinter import *
from tkinter.tix import TEXT
from urllib import response
import requests
import ast
import subprocess
import os
from tkinter import messagebox
import pyttsx3

BG_GREY = "#ABB289"
BG_COLOUR = "#17202A"
TEXT_COLOUR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

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
        line = Label(self.window, width=450, bg=BG_GREY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)

        # text widget - 20 characters wide, 2 characters high, padding
        # padding x in tupple is to stop the text sliding under the scroll bar
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOUR, fg=TEXT_COLOUR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        # Disable so only text can be displayed
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar - only for text widget
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        # command changes y-position of widget to view more
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label - for entry box background
        bottom_label = Label(self.window, bg=BG_GREY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)

        # text entry box
        self.msg_entry = Entry(bottom_label, bg="#2C3E50", fg=TEXT_COLOUR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        # automatically selected when app is opened
        self.msg_entry.focus()
        # Allows message to be sent via enter key in addition send button
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button - calls function via lambda
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GREY, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
        
        # # Create value for an option in "Settings"
        # setting_value = StringVar(self.window, "Settings")
        
        # settings = OptionMenu(self.window, setting_value, "Export Conversation", "Exit")
        # settings.place(relx=0, rely=0, relheight=0.1875, relwidth=0.25)
        var = StringVar()
        label = Label(self.window, textvariable=var)
        # Menubutton automatically highlights when mouse hovers button, so active background makes it same colour
        menubutton = Menubutton(self.window, text="Settings", borderwidth=1, relief="ridge", indicatoron=False, font=FONT_BOLD, bg=BG_GREY, fg="black", activebackground=BG_GREY)
        menu = Menu(menubutton, tearoff=False)
        menubutton.configure(menu=menu)
        menu.add_radiobutton(label="Export Conversation", variable=var, value="Export Conversation", command=self._export_convo)
        menu.add_radiobutton(label="Edit Joke Settings", variable=var, value="Edit Joke Settings")
        menu.add_radiobutton(label="Edit Voice Settings", variable=var, value="Edit Voice Settings") 
        menu.add_radiobutton(label="Exit", variable=var, value="Exit", command=self.exitApp)

        # label.pack(side="bottom", fill="x")
        menubutton.place(relx=0, rely=0, relheight=0.07, relwidth=0.25)

        # Help button for main menu
        self.help = Button(self.window, text="Help", font=FONT_BOLD, width=20, bg=BG_GREY, borderwidth=1, relief="ridge", activebackground=BG_GREY)
        self.help.place(relx=0.25, rely=0, relheight=0.07, relwidth=0.25)

        # Voice button for main menu
        self.voice_button = Button(self.window, text="Voice: Off", font=FONT_BOLD, width=20, bg=BG_GREY, borderwidth=1, relief="ridge", activebackground=BG_GREY, command=self._toggle_voice)
        self.voice_button.place(relx=0.5, rely=0, relheight=0.07, relwidth=0.25)

        # Clear conversation button for main menu
        self.convo_button = Button(self.window, text="Clear Conversation", font=FONT_BOLD, width=20, bg=BG_GREY, borderwidth=1, relief="ridge", activebackground=BG_GREY, command=self._clear_text)
        self.convo_button.place(relx=0.75, rely=0, relheight=0.07, relwidth=0.25)

  
        # give widget attributes with .configure(). dimensions correspond with screen aspect ratio 4:3
        self.window.configure(width=733.33, height=550, bg=BG_COLOUR)

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
