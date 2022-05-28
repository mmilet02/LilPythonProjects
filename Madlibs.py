#   Game Rule:
#   One player acts as the “reader” and asks the other players, who haven't seen the story, to fill in the blanks
#   with adjectives, nouns, exclamations, colors, adjectives, and more. These words are inserted into the blanks
#   and then the story is read aloud to hilarious results.
print("Welcome to Madlibs!")

def madlib1():
    animals= input('enter a animal name : ')
    profession = input('enter a profession name: ')
    cloth = input('enter a piece of cloth name: ')
    things = input('enter a thing name: ')
    name= input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('food name: ')
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

def madlib2():
   
    adjactive = input('enter adjective : ')
    color = input('enter a color name : ')
    thing = input('enter a thing name : ')
    place = input('enter a place name : ')
    person= input('enter a person name : ')
    adjactive1 = input('enter a adjactive : ')
    insect= input('enter a insect name : ')
    food = input('enter a food name : ')
    verb = input('enter a verb name : ')
    print('Last night I dreamed I was a ' + adjactive + ' butterfly with ' + color + ' splocthes that looked like ' + thing + '. I flew to ' + place + ' with my bestfriend and ' + person + ' who was a '+ adjactive1+ ' ' + insect +'. We ate some ' + food + ' when we got there and then decided to ' + verb + ' and the dream ended when I said lets ' + verb + '.')

def madlib3():
    person = input('enter person name: ')
    color = input('enter color : ')
    foods = input('enter food name : ')
    adjective = input('enter aa adjective name: ')
    thing = input('enter a thing name : ')
    place = input('enter place : ')
    verb = input('enter verb : ')
    adverb = input('enter adverb : ')
    food = input('enter food name: ')
    things = input('enter a thing name : ')
   
    print('Today we picked apple from ' + person + "'s Orchard. I had no idea there were so many different varieties of apples. I ate " + color + ' apples straight off the tree that tested like ' + foods + '. Then there was a ' + adjective + ' apple that looked like a ' + thing + '. When our bag were full, we went on a free hay ride to ' + place + ' and back. It ended at a hay pile where we got to ' + verb + ' ' + adverb + '. I can hardly wait to get home and cook with the apples. We are going to make appple ' + food + ' and ' + things +' pies!.')

print("Hello to Madlibs :)\nEnter version of the game (1-3):")
correct_input = False
number = 0
while not(correct_input):
    number = input()
    if not(number.strip().isdigit()):
        print("You did not enter a number [" + number + "]. Version of the game has to be one of these [1, 2, 3]. Try again:")
        continue

    number = int(number)
    if  number > 3 or number < 1:
        print("You enter invalid version [" + str(number) + "]. Version of the game has to be one of these [1, 2, 3]. Try again:")
        continue
    correct_input = True

print("hhhhhhhh" + str(number))
if number == 1:
    madlib1()
if number == 2:
    madlib2()
if number == 3:
    madlib3()

print("End!")