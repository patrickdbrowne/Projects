# # from email.mime import base
# # from tracemalloc import start
# # from typing import List
# # from urllib import request
# # import requests
# # import json
# # import socket
# # import html
# # import random

# # from requests.api import request

# # TIME ZONE API
# # place = input("which timezone do u want?\n")

# # IANA_options = requests.get("https://www.timeapi.io/api/TimeZone/AvailableTimeZones").json()
# # print(IANA_options)
# # index = -1

# # not_city = ["africa", "america", "antarctica", "asia", "atlantic", "australia", "brazil", "canada", "chile", "etc", "europe", "indian", "mexico", "pacific", "us"]
# # #checks the input against each value in the list
# # for valid_place in IANA_options:
# #     # a value is not in a string if str.find() == -1
# #     if valid_place.lower().find(place.lower()) != -1:

# #         index = IANA_options.index(valid_place)
# #         break
# #     else:
# #         continue

# # #If the place was found in the list, then it's used to fetch the time
# # if index >= 0:
# #     parameters = {
# #         "timeZone": IANA_options[index],
# #     }
# #     response = requests.get("https://www.timeapi.io/api/Time/current/zone", params=parameters)
    
# #     # returns sentence
# #     # if user inputs a continent or country, then the first valid answer in the json 
# #     # file will be assumed. E.g., instead of America, the bot will respond with America/Adak
# #     if place.lower() in not_city:
# #         print("the time in", IANA_options[index], "is", response.json()['time'])
# #     else:
# #         print("the time in", place.capitalize(), "is", response.json()['time'])


# # # WEATHER API
# # weather_key = "f5a120d67a0246e2ad311505220801"
# # # parameters for calling weather json. refer to documentation for "q" since it can hold multiple 
# # # data types
# # weather_parameters = {
# #     "key": weather_key,
# #     "q": "Papua New Guinea",
# # }
# # print(socket.gethostbyname(socket.gethostname()))

# # # optional parameters include:
# # # - "hour" ("hour":5 is 5am)
# # # - "days" ("days":5 is number of days of forecast)
# # request_weather = requests.get("http://api.weatherapi.com/v1/forecast.json", params=weather_parameters).json()

# # # collects the location's wind, precipitation, humidity, and average temperature
# # print(u"""
# # The weather in {} is {}:
# # - wind: {} km/h
# # - precipitation: {} mm
# # - humidity: {}
# # - average temperature: {}\N{DEGREE SIGN}C
# # """.format(request_weather["location"]["name"], request_weather["current"]["condition"]["text"].lower(), request_weather["current"]["wind_kph"], request_weather["current"]["precip_mm"], request_weather["current"]["humidity"], request_weather["current"]["temp_c"]))

# # print(request_weather)


# # DEFINITIONS API

# # word = input("definition of word: ")
# # request_word = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word))

# # print(request_word.status_code)
# # definition = False
# # example = False

# # # First check if word exists, since invalid words have the type dictionary, and valid are in lists
# # if isinstance(request_word, dict):
# #     print("Sorry, Scholar! I can't seem to find a definition for {}.".format(word))

# # else:
# #     # Checking if the word has a definition
# #     if "definition" in request_word[0]["meanings"][0]["definitions"][0].keys():
# #         most_common_definition = request_word[0]["meanings"][0]["definitions"][0]["definition"]
# #         definition = True

# #     # Checking if the word has an example
# #     if "example" in request_word[0]["meanings"][0]["definitions"][0].keys():
# #         example_of_word = request_word[0]["meanings"][0]["definitions"][0]["example"]
# #         example = True

# #     # Prints this if word has both an example and definition
# #     if definition and example:
# #         print("""The most common definition of {} is {} For example, {}""".format(word, most_common_definition, example_of_word))

# #     # Prints this if word only has definition
# #     if definition and not example:
# #         print("""The most common definition of {} is {} I can't seem to find any examples...""".format(word, most_common_definition))

# # users_message = 'define wagly woo "oha m goha" '
# # # gets first "
# # start_word = users_message.index("\"") + 1
# # users_word = users_message[start_word:]
# # # finds second " in start_word
# # end_word = users_word.index("\"")

# # print(users_word[:end_word])
# # make sure place is not None
# # place = input("place: ")
# # request_country = requests.get("https://restcountries.com/v3.1/name/{}".format(place)).json()

# # if isinstance(request_country, list):
# #     official_name = request_country[0]['name']['official']
# #     location_link = request_country[0]['maps']['googleMaps']

# #     # To get currency for any country. The second part is equivalent to "AUD" in australia
# #     print(list(request_country[0]['currencies'].keys()))
# #     currency = request_country[0]['currencies'][list(request_country[0]['currencies'].keys())[0]]
# #     area = request_country[0]['region']
# #     demonym = request_country[0]['demonyms']['eng']['m']
# #     population = request_country[0]['population']
# #     continent = request_country[0]['continents'][0]
# #     capital = request_country[0]['capital'][0]

# #     # Again, the second component is specific to each country
# #     main_language = request_country[0]['languages'][list(request_country[0]['languages'].keys())[0]]

# #     place = place.capitalize()


# #     print("""
# #     {}, or officially known as {}, is in the region {} and in the continent {}.
# #     {}'s currency is the {} ({} {}). Not only that, but did you know there are {} {}'s living there at the moment?! 
# #     Additionally, {}'s Capital is {} with the main language being {}.
# #     And even though we can't travel there because of COVID, what's stopping us from digitally visiting there with google? {}.
# #     """.format(place, official_name, area, continent, place, currency['name'], currency['symbol'], list(request_country[0]['currencies'].keys())[0], population, demonym, place, capital, main_language, location_link))

# #     print()
# # else:
# #     print("howdy buddy. We can't find any info on {}".format(place))

# # link = "https://api.covid19api.com/summary"

# # request_COVID = requests.get(link).json()

# # # if place == None
# # global_new_cases = request_COVID["Global"]["NewConfirmed"]
# # global_total_cases = request_COVID["Global"]["TotalConfirmed"]
# # global_total_deaths = request_COVID["Global"]["TotalDeaths"]
# # global_total_recoveries = request_COVID["Global"]["TotalRecovered"]
# # month_dict = {
# #     '01':'January',
# #     '02':'February',
# #     '03':'March',
# #     '04':'April',
# #     '05':'May',
# #     '06':'June',
# #     '07':'July',
# #     '08':'August',
# #     '09':'September',
# #     '10':'October',
# #     '11':'November',
# #     '12':'December'
# #     }

# # date = request_COVID["Date"]
# # year = date[0:4]
# # month = month_dict[date[5:7]]
# # day = date[8:10]


# # print("""
# # Today, there were {} confirmed cases globally! In total, there are {} cases, {} deaths, and {} recoveries in the world.
# # This data was last updated on {} {}, {}.""".format(global_new_cases, global_total_cases, global_total_deaths, global_total_recoveries, day, month, year))

# # # if place != None
# # place = "russia"
# # # Keys are not country names, so I need to identify index of country's info
# # list_countries = request_COVID["Countries"]
# # country_index = None

# # for index in list_countries:
# #     if place.lower() in index["Country"].lower():
# #         country_index = list_countries.index(index)
# #         break
# #     else:
# #         continue

# # if country_index != None:

# #     # print(request_COVID["Countries"][country_index])
# #     place_new_cases = request_COVID["Countries"][country_index]["NewConfirmed"]
# #     place_total_cases = request_COVID["Countries"][country_index]["TotalConfirmed"]
# #     place_total_deaths = request_COVID["Countries"][country_index]["TotalDeaths"]
# #     place_total_recoveries = request_COVID["Countries"][country_index]["TotalRecovered"]
# #     print("""
# #     In {}, there were {} cases today! So far, there are {} cases, {} deaths, and {} recoveries in {}.
# #     This data was last updated on {} {}, {}""".format(place, place_new_cases, place_total_cases, place_total_deaths, place_total_recoveries, place, day, month, year))
# # elif country_index == None:
# #     print("Uh oh! Looks like I can't find any COVID data for {}. Have you checked the spelling?".format(place))
# # import html

# # amount = int(input("number of Q's: "))

# # link = 'https://opentdb.com/api.php?amount={}&type=boolean'.format(amount)
# # trivia_requests = requests.get(link).json()
# # for question_number in range(amount):
# #     question = html.unescape(trivia_requests['results'][question_number]['question'])
    
# #     # replaces these letters with " symbol
# #     # letters = "&quot;"
# #     # if letters in question:
# #     #     while letters in question:
# #     #         question = question[question.index(0):question.index(letters)] + "\"" + question[question.index(letters) + 6 :-1]
        
# #     print(question, "Is this True or False?")
# #     answer = input("").lower()
# #     if answer == trivia_requests['results'][question_number]['correct_answer'].lower():
# #         print("Correct!")
# #     elif answer != trivia_requests['results'][question_number]['correct_answer'].lower():
# #         print("Incorrect!")
# #         print("The statement was {}".format(trivia_requests['results'][question_number]['correct_answer']))
# # print("Thanks for playing!!")

# # Defines output to be in a JSON format, rather than XML or JSONP
# # Jokes are sources from https://sv443.net/jokeapi/v2/ posted under the MIT License
# # Some jokes might be offensive

# # Valid categories are: Any, Misc, Programming, Dark, Pun, spooky, christmas. Default settings:
# # category = "Programming,Miscellaneous,Pun,Spooky,Christmas"
# # blackList = "nsfw,religious,political,racist,sexist,explicit"

# # # In GUI, if explicit is on, then
# # # blackList = ""
# # # category = [options entered]
# # # --Shows warning that it could be offensive to the audience--

# # if blackList == "":
# #     request_jokes = requests.get("https://v2.jokeapi.dev/joke/{}".format(category))
# # elif blackList != "":
# #     request_jokes =  requests.get("https://v2.jokeapi.dev/joke/{}?blacklistFlags={}".format(category, blackList))

# # # Adjusts output depending if there is one or two parts to a joke
# # if request_jokes.status_code != 200:
# #     print("Oops! Something has gone wrong with our Jokes API. Why don't you try something else in the meantime?")

# # elif request_jokes.json()['type'] == 'twopart':
# #     setup = request_jokes.json()['setup']
# #     delivery = request_jokes.json()['delivery']
# #     print("{}\n{}".format(setup, delivery))

# # elif request_jokes.json()['type'] == 'single':
# #     joke = request_jokes.json()['joke']
# #     print(joke)

# # triviaLink = "https://opentdb.com/api.php?amount=1&type=multiple"

# # trivia = requests.get(triviaLink).json()

# # # First checks for valid JSON return
# # if trivia['response_code'] != 0:
# #     print('Uh oh! Something went wrong with the backend. Why not try again?')
# # else:
# #     typeOfTrivia = trivia['results'][0]['category'].lower()
# #     # This makes the sentence flow nicer for categories with "Entertainment:" in it
# #     if "entertainment" in typeOfTrivia:
# #         typeOfTrivia = typeOfTrivia[15:]
    
# #     question = html.unescape(trivia['results'][0]['question'])
# #     correctAnswer = trivia['results'][0]['correct_answer']
# #     wrongAnswer1 = trivia['results'][0]['incorrect_answers'][0]
# #     wrongAnswer2 = trivia['results'][0]['incorrect_answers'][1]
# #     wrongAnswer3 = trivia['results'][0]['incorrect_answers'][2]

# #     # Assigns the correct and incorrect answers to random options, so there's 
# #     # No pattern for winning.
# #     Answers = [correctAnswer, wrongAnswer1, wrongAnswer2, wrongAnswer3]
# #     randomChoices = random.sample(Answers, len(Answers))
# #     randomChoices_dict = {
# #         "A": randomChoices[0],
# #         "B": randomChoices[1],
# #         "C": randomChoices[2],
# #         "D": randomChoices[3]
# #     }

# #     print("Here's some {} trivia for you: {}".format(typeOfTrivia, question))
# #     print("""
# # A. {}
# # B. {}
# # C. {}
# # D. {}""".format(randomChoices[0], randomChoices[1], randomChoices[2], randomChoices[3]))

# #     userAnswer = input("\nIs your answer A, B, C, or D:\n")
# #     # Detects answer from the letter using dictionary
# #     if randomChoices_dict[userAnswer] == correctAnswer:
# #         print("Correct! You're so smart")
# #     else:
# #         print("Unlucky that's wrong... The correct answer is {}".format(correctAnswer))

# # print(requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/hello").json())







# ############################################
# # searching = True
# # artist_name = "Pink Floyd"
# # # Returns artist's details
# # searchResults = spotifyObject.search(artist_name,1,0,"artist")
# # print(searchResults)
# # artist = searchResults['artists']['items'][0]
# # artistID = artist['id']
# # artist_name= artist['name']

# # ## Extract artist data and fill database
# # df_artists = []
# # df_artists = df_artists.append({'artist_id': artist['id'],
# #                                 'artist_name':artist['name'],
# #                                 'genres':artist['genres'],
# #                                 'folowers':artist['followers']['total'],
# #                                 'popularity':artist['popularity']}, 
# #                                 ignore_index=True
# #                                 )
                                
# # # ALBUM DETAILS
# # albumResults = spotifyObject.artist_albums(artistID, limit=50)
# # albumResults = albumResults['items']
# # z = 0

# # # Loop over album
# # for album in albumResults:
    
# #     ## Extract album data and fill database
# #     albumID = album['id']
# #     album_name =  album['name']
    
# #     df_albums = df_albums.append({'artist_name':album['artists'][0]['name'],
# #                                     'artist_id':album['artists'][0]['id'],
# #                                     'album_id': album['id'],
# #                                     'album_name':album['name'],
# #                                     'release_date':album['release_date'],
# #                                     'total_tracks':album['total_tracks'],
# #                                     'type':album['album_group']},
# #                                     ignore_index=True
# #                                     )
    
# #     df_albums= df_albums.astype({'total_tracks':int})
    
# #     print("ALBUM: " + album['name'])

# #     # TRACK DETAILS
# #     trackResults = spotifyObject.album_tracks(albumID)
# #     trackResults = trackResults['items']
    
# #     ## Loop over tracks
# #     for track in trackResults:
        
# #         artists_names =[]
# #         artists_ids = []
        
# #         for artist in track['artists']:
# #             artists_names.append(artist['name'])
# #             artists_ids.append(artist['id'])
        
# #         ## Extract track data and fill database
# #         if (artistID in artists_ids or artist_name in artists_names):
# #             z+=1
# #             df_tracks = df_tracks.append({'album_id':albumID,
# #                                             'album_name':album_name,
# #                                             'artist_id': artists_ids,  
# #                                             'artists_name': artists_names, 
# #                                             'song_id': track['id'],
# #                                             'song_name':track['name']},
# #                                             ignore_index=True
# #                                             )
            
# #             print(str(z) + ": " + track['name'])
    
# #     print()
# # print('Number of songs:', z)
# # print()
# # print("---------------------")
# # print()
# # Created an account on spotify to get a client id and client secret
# import requests

# # My spotify credentials for this project
# CLIENT_ID = '3f4f8323f25d456c843cd66d1bf7b691'
# CLIENT_SECRET = '232ec99a73b1453aa66487bec3bad0a5'

# AUTH_URL = 'https://accounts.spotify.com/api/token'

# # Post the details to get an access token so we can use various endpoints later on
# auth_response = requests.post(AUTH_URL, {
#     'grant_type': 'client_credentials',
#     'client_id': CLIENT_ID,
#     'client_secret': CLIENT_SECRET,
# })

# # convert the response to JSON
# auth_response_data = auth_response.json()

# # save the access token - this is what is used for get requests
# access_token = auth_response_data['access_token']

# headers = {
#     # American spelling...
#     "Authorization": "Bearer {}".format(access_token)
# }
# params = {
#     "include_groups": "album",
#     "limit": 50
# }

# # base URL of all Spotify API endpoints
# BASE_URL = 'https://api.spotify.com/v1/'
# # Track ID from the URI. user just needs to copy and paste the "copy artist link" and 
# # program does the rest
# # artist ID from the URI - end bit of copy and pasting track ID from spotify. put in instructions to change...
# artist_id = input("id: ")
# start_URI = 32
# end_URI = 54
# artist_id = artist_id[start_URI:end_URI]
# print(artist_id)


# # format to request album data of artist - only albums no single songs, max 50 albums
# artist_data = requests.get("{}artists/{}".format(BASE_URL, artist_id), headers=headers).json()
# print(artist_data)

# album_data = requests.get("{}artists/{}/albums".format(BASE_URL, artist_id), headers=headers, params=params).json()
# # print(album_data)

# name = artist_data['name']
# genre = artist_data['genres'][0]
# if name.lower() in ["pink floyd", "nirvana", "oasis", "arctic monkeys", "the beatles", "twenty one pilots", "bob dylan", "the rolling stones", "genesis", "cream", "eric clapton"]:
#     print("{} is known for its {} music. This is one of my personal favourites! Here are some albums you may want to check out:".format(name, genre))
# else:
#     print("{} is known for its {} music! Here are some of their snazzy albums:".format(name, genre))

# # format to request album data of artist - only albums no single songs, max 50 albums
# # r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums', headers=headers, params=params)
# # d = r.json()

# # Prevents duplicate albums from appearing
# albums = [] # to keep track of duplicates

# # loop over albums and get all tracks
# output = ""
# for album in album_data['items']:
#     album_name = album['name']

#     # This skips over albums already covered
#     trim_name = album_name.split('(')[0].strip()
#     if trim_name.upper() in albums or int(album['release_date'][:4]) > 1983:
#         continue
#     albums.append(trim_name.upper()) # use upper() to standardize
    
#     # this takes a few seconds   
#     print(album_name)
#     output += album_name

# import spotipy
# import json
# import webbrowser

# # Private information - use environment variables
# clientID = '3f4f8323f25d456c843cd66d1bf7b691'
# clientSecret = '232ec99a73b1453aa66487bec3bad0a5'
# redirectURI = 'http://google.com/'

# # Create OAuth Object
# oauth_object = spotipy.SpotifyOAuth(clientID,clientSecret,redirectURI)

# # Create token
# token_dict = oauth_object.get_access_token()
# token = token_dict['access_token']

# # Create Spotify Object
# spotifyObject = spotipy.Spotify(auth=token)

# user = spotifyObject.current_user()
# # To print the response in readable format.
# print(json.dumps(user,sort_keys=True, indent=4))

# # searches for song in browser

# # Get the Song Name.
# searchQuery = input("Enter Song Name: ")
# # Search for the Song.
# searchResults = spotifyObject.search(searchQuery,1,0,"track")
# # Get required data from JSON response.
# tracks_dict = searchResults['tracks']
# tracks_items = tracks_dict['items']
# song = tracks_items[0]['external_urls']['spotify']
# # Open the Song in Web Browser
# webbrowser.open(song)

# import modules
from tkinter import *

# # configure workspace
# ws = Tk()
# ws.title("First Program")
# ws.geometry('250x150')
# ws.configure(bg="#567")

# # function territory
# def welcome():
#     name = nameTf.get()
#     return Label(ws, text=f'Welome {name}', pady=15, bg='#567').grid(row=2, columnspan=2)

# # label & Entry boxes territory
# nameLb = Label(ws, text="Enter Your Name", pady=15, padx=10, bg='#567')
# nameTf = Entry(ws)

# # button territory
# welBtn = Button(ws, text="ClickMe!", command=welcome)

# # Position Provide territory
# nameLb.grid(row=0, column=0)
# nameTf.grid(row=0, column=1)
# welBtn.grid(row=1, columnspan=2)

# # infinite loop 
# ws.mainloop()




# ws = Tk()

# Label(ws, text="Tea", font=(24)).pack()
# def update():
#     a = var1 == "PY_VAR0"
#     return Label(ws, text=a, font=(15)).pack()
# var1 = IntVar()
# Checkbutton(ws, text="Milk", variable=var1, command=update).pack()
# var2 = IntVar()
# Checkbutton(ws, text="Sugar", variable=var2).pack()
# var3 = IntVar()
# Checkbutton(ws, text="Ginger", variable=var3).pack()
# var4 = IntVar()
# Checkbutton(ws, text="Lemon", variable=var4).pack()

# Button(ws, text="var1", command=update).pack()
# Label(ws, text=var1, font=(15)).pack()

# print(var1)

# ws.mainloop()

# from tkinter import *
# from tkinter import messagebox

# class MenuBar(Menu):
#     def __init__(self, ws):
#         Menu.__init__(self, ws)

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


# class MenuDemo(Tk):
#     def __init__(self):
#         Tk.__init__(self)
#         menubar = MenuBar(self)
#         self.config(menu=menubar)

# if __name__ == "__main__":
#     ws=MenuDemo()
#     ws.title('Python Guides')
#     ws.geometry('300x200')
#     ws.mainloop()

# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# def popup_bonus():
#     win = tk.Toplevel()
#     win.wm_title("Window")

#     l = tk.Label(win, text="Input")
#     l.grid(row=0, column=0)

#     b = ttk.Button(win, text="Okay", command=win.destroy)
#     b.grid(row=1, column=0)

# def popup_showinfo():
#     showinfo("Window", "Hello World!")

# class Application(ttk.Frame):

#     def __init__(self, master):
#         ttk.Frame.__init__(self, master)
#         self.pack()

#         self.button_bonus = ttk.Button(self, text="Bonuses", command=popup_bonus)
#         self.button_bonus.pack()

#         self.button_showinfo = ttk.Button(self, text="Show Info", command=popup_showinfo)
#         self.button_showinfo.pack()

# root = tk.Tk()

# app = Application(root)

# root.mainloop()

from testGlobal import blacklist
from testGlobal import category

print(blacklist, "            ", category)