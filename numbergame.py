import random  #import random library

r = random.randint(1, 10) #create a random number 1-10
g = int(input("Enter a number from 1 to 10")) #user enters a number between 1-10
c = 0 #guess count

while g != r and c <= 3: #while loop for guessing the random number

    if g < r:
        print("Your guess is to low")
        g = int(input("Enter a number from 1 to 10")) #print message for a low guess
        c = c + 1 #count for a guess - is this correct syntax?
    if g > r:
        print("your guess is to high")
        g = int(input("Enter a number from 1 to 10")) #print message for a high guess
        c = c + 1 #count for a guess
    else:
        print("Winner, Winner, Chicken, Dinner!", r) #print message for a win

        break

if c == 3:
    print("Not your day. Game over", r) #print for more than 3 guesses. Game over










