from random import randrange

print("Hello to Guessing Game. You need to enter a number between 0 and 100 and computer will try to guess your number in 7 tries.")
number = 0
is_correct_input = False
while not(is_correct_input):
    number = input("Enter your number: ")
    if not(number.strip().isdigit()):
        print("You did not enter a number [" + number + "]. Try again:")
        continue
    elif int(number) > 100 or int(number) < 0:
        print("You did not enter a number bettween 0-100 [" + number + "]. Try again:")
        continue
    is_correct_input = True

number = int(number)
number_of_tries = 7
the_end = False
round = 0
guessing_number = 0
min = 0
max = 100

print("Starting with guessing ....")
while not(the_end):
    round += 1
    print("Round " + str(round) + ".")
    guessing_number = randrange(min,max)
    print("Is your number " + str(guessing_number) + "?")
    number = int(number)
    if guessing_number == number:
        print("Congratulations :) Computer gueesed your number in " + str(round) + " round")
        the_end = True
    elif (number_of_tries - 1) == 0:
        print("The End, Computer did not manage to guess your number.")
        the_end = True
    elif guessing_number > number:
        number_of_tries =- 1
        max = guessing_number - 1
        print("Your number is smaller. Maybe hmm ....")
    elif guessing_number < number:
        number_of_tries =- 1
        min = guessing_number + 1
        print("Your number is larger. Maybe hmm ....")