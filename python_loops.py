import random
from datetime import datetime, timedelta

#The Range Riddle
#Task One: Code Correction 
for i in range(5, 2, -1):
    print(i)
print()

#Task Two: Your Mood Today
mood = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Silly", "Serene"]
days_of_week = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]

for i in range(len(days_of_week)):
    print(days_of_week[i] + ": " + random.choice(mood))
print()

#Task Three: Going Backwards
for i in range(10, 0, -1):
    print(i)

print()
#Double Scoop with Nested Loops
#Task One: Code Correction 

for i in range(1,4):
    for j in range(1,4):
        print("*", end=" ")
    print()
print()  

#Task Two: Your Mood Tracker
times_of_day = ["Morning", "Afternoon", "Evening"]      
for i in range(len(days_of_week)):
    print(days_of_week[i])
    for j in range(len(times_of_day)):
        print(times_of_day[j] ,":", random.choice(mood))
print()

#Task Three: Multiplication Table
for i in range(1,6):
    for j in range(1,6):
        print(i * j, end=" ") 
    print()
print()

#Mastering Python's For Loop
#Task One: Code Correction
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
print()
#Task Two: Your Mood Swings
for i in range(25):
    if i == 12:
        continue
    print(f"Hour {i}:" , random.choice(mood))
print()

#Task Three: The Persistent Loop 
list_of_numbers = [42, 50, 87, 101, 96, 5]

for number in list_of_numbers:
    if number == 42:
        break
else:
    print("Number Not found!")
print()

#Task One: Increment at the Start
#Prediction: Enter loop bc condition is true, number of marhmallows increments by 1, and the result is printed
# Print statement prints to show increase of marshmallows from 1 to 5
marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")

print()

#Task Two: Increment at the End
marshmallows = 0
while marshmallows < 5:   
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1
print()
#The difference between the two locations of the incrementor changes what's compared at the testing condition
#before entering the loop

#Task Three: Off By One Error Investigation
marshmallows = 0
while marshmallows < 10:   
    print("Added a marshmallow! Now there are " + f"{marshmallows} out of 10" + " marshmallows.")
    marshmallows += 1
print()

#Corrected Error
marshmallows = 0
while marshmallows < 10:   
    marshmallows += 1
    print("Added a marshmallow! Now there are " + f"{marshmallows} out of 10" + " marshmallows.")  
print()
#During the last iteration, the condition is true bc 9 is less than 10, but it immediately is 
#incremented by 1 to fill the bag with 10 marshmallows. In the first scenario, 0 marshmallows is added 
# to the bag so the final iteration makes 10 which is not less than 10

#Task One: Loop Condition Exploration
marshmallows = 10
while marshmallows > 20:
    marshmallows -= 1
    print("Removed a marshmallow! Now there are " + f"{marshmallows} out of 10" + " marshmallows.") 
    if marshmallows == 5:
        break
print()

#The purpose of the condition and break statement is to provide another way to break out of the loop 
#without relying on the loop condition - if the loop was entered (true condition) the loop would go through
#five iterations

# #Task Two: Conditional Exist
marshmallows = 50
while marshmallows >= 40:
    print("Removed a marshmallow! Now there are " + f"{marshmallows} out of 40" + " marshmallows.") 
    marshmallows -= 1
print()

#Task Three: Loop with Multiple Conditions 
marshmallows = 50
while marshmallows >= 40 and marshmallows % 2 == 0:
    print("Removed a marshmallow! Now there are " + f"{marshmallows} out of 40" + " marshmallows.") 
    marshmallows -= 1
print()
#Combining conditions makes the loop more complex because the starting point and iterator has to coordinate
#with more than one starting condition which can increase or decrease the number of iterations

#The Art of Loop Control
#Task One: Using Else with While
number = 20
while number < 25:
    number += 1 
    if not number == 25:
        continue
else:
    print(f"The number {number} was found!")
print()
#The else statement executes when the starting condition becomes false 

#Task Two: Loop Interruption with Break
# current_time = datetime.now()
# while current_time:
#     print(current_time)
#     new_time = current_time + timedelta(hours=5)
#     if current_time == new_time:
#         break
# print()
#In five hours, the current time will equal the new time then break out of the loop
#Otherwise the current time will continue to print 

#Task Three: Skipping Iterations with Continue
number = 0
while number <= 20:
    if number % 3 == 0:
        number += 1
        continue
    print(number)
    number += 1
print()
#The purpose of the continue keyword is to skip the rest of the code in an iteration 
#In this case, numbers that are divisible by 3 are incremented by 1 then no other code is executed until
#the even number is printed 

number = 0
while number <= 20:
    if number % 2 == 0:
        pass
    print(number)
    number += 1
print()
#The pass keyword is helpful because it serves as a placeholder for code that will be written in the future 

#Python's Random Game Night 
#Task One: Dice Rolling Simulator

# Initialize a dictionary to keep track of dice roll frequencies
roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Let's roll the dice 10 times
for x in range(10):
    dice_roll = random.randint(1, 6)
    # Update the roll_count dictionary
    roll_count[dice_roll] += 1
    print("You rolled a " + str(dice_roll) + "!")
print()
# Print out the frequency of each number
for number, frequency in roll_count.items():
    print(f"Number {number} was rolled {frequency} times.")
print()

#Task Two: Random Choice Game 
list_numbers = [10, 20, 30, 40, 50, 60, 80, 100]

chosen_number = int(input("Choose an integer between 10 and 100. It must be divisible by 10: "))
computer_choice = random.choice(list_numbers)
for x in range(1,4):
    if computer_choice == chosen_number:
       
        continue
        print(f"Congratulations, you guessed {computer_choice} correctly!")
    else:
        print(f"Try again, you guessed {chosen_number} incorrectly! The computer chose {computer_choice}!")
        print()
    chosen_number = int(input("Choose an integer between 10 and 100. It must be divisible by 10: "))
    computer_choice = random.choice(list_numbers)
    print(f"You guessed {chosen_number} incorrectly! The computer chose {computer_choice}!")
    
print("You lost the game!")
print()
#Task Three: Shuffling a Deck 
cards = ["Ace","K","Q","J", 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Ordered Deck: {cards}")
random.shuffle(cards)
print(f"Shuffled Deck: {cards}")
print()
#The shuffle method can be used for music applications to shuffle songs and for gaming applications to randomize
#piece on a virtual chess board for example 

#The Random Challenge Course
#Task One: The Guessing Game


for x in range(3):
    given_number = int(input("Enter a number between 1 and 10: "))
    random_number = random.randint(1, 100)

    if(given_number == random_number):
        print(f"Congratulations! You guessed {random_number} correctly!")
    elif(given_number < random_number):
        print(f"{given_number} is incorrect. It was too low!")
    else:
        print(f"{given_number} is incorrect. It was too high!")

    
print()

#Task Two: Magic 8-Ball 
piece_of_advice = ["Did you ask AI?", "Have you stopped at the library to research?", "Use Google Scholar", 
"Eat nutritiously", "Build a network of people who earn more than you", "Consider education, formal or informal"]

chosen_advice = random.choice(piece_of_advice)
print(f"Random Advice: {chosen_advice}")

#Loop Lists: The Rhythm of Repetition 
# Task One: The for Loop DJ Set
import random

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
counter = 0
for x in range(4):
    counter += 1
    chosen_genre = random.choice(genres)
    print(f"Track {counter}: {chosen_genre}")
print()
# Task Two: The Remix Artist with while
counter = 0
while counter < 4:
    counter += 1
    chosen_genre = random.choice(genres)
    if chosen_genre == "Jazz":
        break
    else:
        print(f"Track {counter}: {chosen_genre}")
print()

#Task Three: Light Show Technician Loop
counter = 0
for genre in genres:
    counter += 1
    if not genre == "Rock":
        print(f"Track {counter}: Ready for Light Show!")
    else: 
        continue
print()

#Advanced Looping Techniques
#Task One: The Selective DJ
genre_slice = genres[2:4]
for x in range(2):
    print(f"Genre {x+1} : {genre_slice[x]}")
print()

#Task Two: The One-Liner Band with List Comprehensions
new_genres_list = [genre + " Music" for genre in genres]
print(new_genres_list)
print()       

#Task Three: Numerical Beats with range
counter = 10
while counter >= 1:
    if counter == 1:
        print(counter)
        print("The beat drops now!")
    else:
        print(counter)
    counter -= 1
print()
