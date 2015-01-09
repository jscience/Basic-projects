import random

print ('Welcome to Camel!')
print ('You have stolen a camel to make your way across the great Mobi desert.')
print ('The natives want their camel back and are chasing you down! Survive your')
print ('desert trek and out run the natives.')

done = False

miles_traveled = 0
thirst = 0
camel_tired = 0
natives = -20
canteen = 3
oasis = random.randrange(20)


while done == False:                        #while loop displays player's options 
    print('A. Drink from your canteen.')    #as long as the game is still going
    print('B. Ahead moderate speed.')
    print('C. Ahead full speed.')
    print('D. Stop for the night.')
    print('E. Status check.')
    print('Q. Quit.')
    user_choice = input('Your choice? ')    #User chooses action to take
    print('')                               #Aesthetic preference. Can be deleted
    
    if user_choice.upper() == 'Q':          #Quits game
        done = True

    elif user_choice.upper() == 'A':        #Lets user drink, subtracts one drink from canteen
        if canteen > 0:
            canteen -= 1
            thirst = 0
        else:
            print("You're out of water!")

    elif user_choice.upper() == 'B':        #User moves moderately quickly, expends resources moderately quickly
        miles_traveled += random.randrange(5,13)
        print('You have traveled ', miles_traveled, 'miles.')
        thirst += 1
        camel_tired += 1
        natives += random.randrange(10,15)

    elif user_choice.upper() == 'C':        #User moves quickly and expends resources quickly
        miles_traveled += random.randrange(10,21)
        print('You have traveled ', miles_traveled, ' miles.')
        thirst += 1
        camel_tired += random.randrange(1,4)
        natives += random.randrange(10,15)
        
    elif user_choice.upper() == 'D':
        camel_tired = 0
        print('Your camel is happy to take a break')
        natives += random.randrange(10,15)
    
    elif user_choice.upper() == 'E':
        print('Miles traveled: ', miles_traveled)
        print('Drinks left in canteen: ', canteen)
        print('The natives are ', miles_traveled - natives, ' miles behind you')

    if not done and thirst > 4:
        print('You are thirsty.')
    if not done and thirst > 6:
        print('You died of thirst.')
        done = True
    if not done and camel_tired > 5:
        print('Your camel is getting tired')
    if not done and camel_tired > 8:
        print('Your camel is dead.')
        print('The natives caught you!')
        done = True
    if not done and natives >= miles_traveled:
        done = True
        print('The natives caught you!')
    elif not done and natives > (miles_traveled-15):
        print('The natives are getting close!')
    if not done and miles_traveled > 200:
        print('You escaped successfully!')
        done = True
    if not done and oasis == 14:
        print('You found the hidden oasis')
        print('Your camel is rested and your thirst is quenched!')
        thirst = 0
        camel_tired = 0
        canteen = 5
        
print('Type yes to quit')
quit = input('Are you done? ')
          
if quit.upper() == 'YES':
    done = True
else:
    done = False
          
