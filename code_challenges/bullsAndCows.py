# -*- coding: utf-8 -*-
"""
Ex 18 - Game “cows and bulls” . 

The game works like this:
- Randomly generate a 4-digit number. 
- Ask the user to guess a 4-digit number. 
- For every digit that the user guessed correctly in the correct place, they have a “cow”. 
- For every digit the user guessed correctly in the wrong place is a “bull.” 
- Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
- Once the user guesses the correct number, the game is over. 
- Keep track of the number of guesses the user makes throughout the game 
and tell the user at the end.

"""
import random

numb_len = 4


def compare_numbers(numb1,numb2):
    (bulls, cows) = (0,0)
    
    for i in range(numb_len):
        if numb1[i] in numb2:
            if numb1[i] == numb2[i]:
                cows += 1
            else:
                bulls += 1
    return (bulls, cows)


def read_user_guess():
    while True:
        print("Suggest a number: ")
        user_guess = input()
        user_guess = [int(x) for x in user_guess]
        if len(user_guess) != numb_len:
            break;
        elif user_guess[0] == 0:
            break;
        else:
            return user_guess


def generate_number():
    # return random.randint(1000,9999)
    number = []
    count = 0
    while count < numb_len:
        if count == 0:
            numb = random.randint(1, 9)
        else: 
            numb = random.randint(0, 9)
        if numb not in number:
            number.append(numb)
            count += 1
    return number
    
if __name__=="__main__":
    number = generate_number()
    print("my number is: ", number)
    
    count = 0
    while True:
        
        user_guess = read_user_guess()
        
        (bulls, cows) = compare_numbers(number, user_guess)
        
        print("You have {} bulls and {} caws".format( bulls, cows))
        count +=1 
        
        
        if cows == 4 and bulls == 0:
            print("Horaaaay ! You guessed correctly with only {} tries.".format(count))
            break;
        if count == 100:
            break
    
        
        
        
        