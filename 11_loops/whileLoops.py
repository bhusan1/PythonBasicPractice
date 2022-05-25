#Guess number game -- loops until they get right number
number=7

#while loop example
while True:
    user_input = input("Would like to play: (Y/n) ")

    if user_input == "n":
        break

    user_number = int(input("Guess a number: "))
    if user_number == number:
        print("You guessed the number correctly!!")
    elif number - user_number in (1,-1):  # you can use 'in' keyword this way
        print ("You were off by one.")
    elif abs(number - user_number) == 2: # or you can use '==' this way
        print ("You were off by 2.")
    else:
        print("You guessed wrong!!")