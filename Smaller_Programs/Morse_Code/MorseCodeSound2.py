from Translation_Class import Translations # This file youre reading has to be before the file you want to import, and you address it by . Its like a tree
import winsound
import time

def dot():
    winsound.Beep(1000, 100) #Makes a beep sound (frequency, millisecond)

def dash():
    winsound.Beep(1000, 500)


print("Press '*' to recieve a list of Morse Code translations")

#This continues loop indefinitely until user discontinues it
while True:
  text = input("What phrase do you want in Morse Code?\n")
    
#dictionary of translations from the imported class
  dictionary = Translations().morse_code()

#This prints the dictionary whenever the user types '*' into the 'text' input
  while text == "*":
    for i in dictionary:
      print(i, dictionary[i])
    text = input("What phrase do you want in Morse Code?\n")

#The following section filters input to what's in the dictionary above. This is so there's no errors in the code.
#This also turns the text to lowercase so it can be referred to in the dictionary. the 'for i in text.lower()' doesn't refer to
#0, 1, 2, etc. it actually refers to each letter in the string, which is why 'dictionary[text[i]]' is unnecessary 

  i = -1
  text = text.lower()
  while i != len(text) - 1:
    text = text.lower()
    try:
      i += 1
      z = dictionary[text[i]]
    except:
      text = input("Please enter a valid statement with only letters and numbers.\n")
      i = -1

  #This is a seperate section to make sure the input is not ""
  while bool(text) is False:
    text = input("Please enter a valid statement with only letters and numbers.\n")

  translation = ""
  
  for i in text:
    translation += str(dictionary[i])
    
  print(translation)
  
  #This section is for sound
  for t in translation:
      if t == ".":
          dot()
      elif t == "-":
          dash()
      elif t == " ":
          time.sleep(1)
      time.sleep(0.5)


#This continues or breaks the 'While True' loop above depending on the input
  repeat = input("\nWould you like to repeat this? (Y/N)\n")

#This is incase the user enter '*' for the dictionary
  while repeat == "*":
      for i in dictionary:
        print(i, dictionary[i])
      repeat = input("Would you like to repeat this? (Y/N)\n")

  if repeat == "Y" or repeat == "y":
      continue
  else:
      break
