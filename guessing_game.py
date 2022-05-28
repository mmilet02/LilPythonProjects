from random import randrange

print("Hello to Guessing Game. You need to guess a number between 0 and 100.")
number = randrange(0,100)
print("Secret Number was generated. Good Luck")
is_guessed = False
input_number = 0
while not(is_guessed):
    input_number = input("Enter your guess: ")
    if not(input_number.strip().isdigit()):
        print("You did not enter a number [" + input_number + "]. Try again:")
        continue
    input_number = int(input_number)
    if input_number == number:
        print("Congratulations :) You gueesed right number -> " + str(number))
        is_guessed = True
    elif input_number > 100 or input_number < 0:
        print("Secret Number is range [0-100]. Try again.")
    elif input_number > number:
        print("Secret Number is lower than your input. Try again.")
    elif input_number < number:
        print("Secret Number is higher than your input. Try again.")