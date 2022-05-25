#Guess number game
number=7
user_input = input("Enter 'y' if you would like to play: ")

#instead of user_input == 'y', use 'in'
#better option use .lower() in user_input
if user_input in ("y", "Y"):
    user_number = int(input("Guess a number: "))
    if user_number == number:
        print("You guessed the number correctly!!")
    elif number - user_number in (1,-1):  # you can use 'in' keyword this way
        print ("You were off by one.")
    elif abs(number - user_number) == 2: # or you can use '==' this way
        print ("You were off by 2.")
    else:
        print("You guessed wrong!!")
else:
    print("Well good luck with other games!!")