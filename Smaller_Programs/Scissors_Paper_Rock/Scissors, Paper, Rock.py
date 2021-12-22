import random

start = input("Welcome to the game of Scissors, Paper, Rock. Press [Enter} to start.")

# Dictionary of truly random outcomes computer can refer to. The keys are random integers, referring to values of scissors, paper, and rock.
outcomes = {
    1: "scissors",
    2: "paper",
    3: "rock"
    }
#An infinite loop when user presses [Enter].
while bool(start) is False:
    print("\nYou will play against the computer. Press [Enter] again at anytime to exit the game. Your score will be displayed.")
    answer = input("Enter scissors, paper or rock.\n")
    i = 0 #This counts number of rounds played and shows the above input once, and the 'input("")' for the rest of the time.
    x = 0 #This counts number of times the user has won. It increases by one each time the user wins
    p = 0 #This is to stop extra input when invalid statement is made
    a = 0 #This counts number of times you drew
    b = 0 #This counts number of times you lost
    while bool(answer) is True:
        while i > 0 and p == 0:
            answer = input("")
            break
        # Makes a loop when input is not [Enter]
        if bool(answer) is False:
            break
        p = 0
        i += 1 # Number of rounds increases by 1 each time
        answer = answer.lower() # This is to refer to the dictionary without any issues
        computer = random.randint(1, 3) # Computer generates random integer and uses this integer to refer to the key of the dictionary
        computers_answer = outcomes[computer]

        # Possible outcomes if user enters scissors
        if answer == "scissors":
            if computers_answer == "scissors":
                print(computers_answer)
                print("Draw!")
                a += 1
            elif computers_answer == "paper":
                print(computers_answer)
                print("You Win!")
                x += 1
            elif computers_answer == "rock":
                print(computers_answer)
                print("You Lose!")
                b += 1
                
        # Possible outcomes if user enters paper         
        elif answer == "paper":
            if computers_answer == "scissors":
                print(computers_answer)
                print("You Lose!")
                b += 1
            elif computers_answer == "paper":
                print(computers_answer)
                print("Draw!")
                a += 1
            elif computers_answer == "rock":
                print(computers_answer)
                print("You Win!")
                x += 1

        # Possible outcomes if user enters rock         
        elif answer == "rock":
            if computers_answer == "scissors":
                print(computers_answer)
                print("You Win!")
                x += 1
            elif computers_answer == "paper":
                print(computers_answer)
                print("You Lose!")
                b += 1
            elif computers_answer == "rock":
                print(computers_answer)
                print("Draw!")
                a += 1
                
        # If user hits [Enter] and exits
        elif bool(answer) is False:
            break
        # If user enters a different value
        while answer != "scissors" and answer != "paper" and answer != "rock" and bool(answer) is True:
            answer = input("Please enter a valid statement:\n")
            p += 1
            if bool(answer) is False:
                i -= 1
            else:
                continue
    # Exits
    if bool(answer) is False:
        break

while True:
    try:
        z = int(x/i * 100) # percentage of times you won
        a = int(a/i * 100)
        b = int(b/i * 100)
        
        print("You have played " + str(i) + " rounds, " + str(x) + " of which you have won! This means you won or drew " + str(z + a) + "%, and lost " + str(b) + "% of the time.")
        break

    except:
        print("You have played " + str(i) + " rounds.") # For a division by zero error
        break    
    
