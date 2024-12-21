import random


# def guess(x):

#     random_number = random.randint(1, x)
#     guess = 0

#     while guess != random_number:
#         guess = int(input(f"Guess Number is between 1 and {x}: "))
#         if guess < random_number:
#             print("Your Guess Number is too Low Try again")
        
#         elif guess > random_number:
#             print("Your Guess Number is too High try again")


#     print(f"Congratulations. You have guessed the number {random_number} correctly!")


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! The computer guessed your number, {guess}, correctly!')

    
    guess(10)






    
