'''
Water - 1
Snake - 0
Gun   - -1
------------------------------------------------------
On adding the computer's choice and my choice,
1.if the result is '1' then I will win.
2.if the result is '0' then I will loose
3.if the result is greater then '1' then I will loose
------------------------------------------------------
=> All possible outcomes and their result are as follows :
Computer   Me
snake    - gun - Win
water    - gun - loose
gun      - gun - Tie
snake    - snake - Tie
water    - snake - win
gun      - snake - loose
snake    - water - Loose
water    - water - Tie
gun      - water - Win
----------------------------
Modules used -
1. random - to make the game more unpredictable
2. time   - for certain delays
'''

import random
game_rules = f'''
-----------____------___________-----_________-----________------
{"Welcome to Snake,Water,Gun Game Instruction module.":^60}
This game is similar to stone,paper,scissor ; here you will find 
Snake, Water and Gun.
The following table shows all the possible cominations and
their results.
Computer   Me       Result
snake    - gun      - Win
water    - gun      - loose
gun      - gun      - Tie
----------------------
snake    - snake    - Tie
water    - snake    - win
gun      - snake    - loose
-------------------------
snake    - water    - Loose
water    - water    - Tie
gun      - water    - Win
------------------------
Hope you understood the game. Now Enjoy...
Thank You!!
Team
-Koi team nahi hai, maje le raha tha.
Game sahi se khelna, wo majak nahi hai...
-------------------------------------------
You will be playing with computer maharaj and let's see who wins..
All the best :)
---__---_---__--_--_--_-_--_----_--__-__-_--_--_______--__--_--
'''



#Importing modules
from random import choice
import time

#Defining Character animation code
def char_animation(msg:str):
    speed = [0.001,0.0002,0.01,0]
    for char in msg:
        print(char,end='')
        time.sleep(random.choice(speed))

#Choices that computer has
all_choices = {'Snake':0,'Water':1,"Gun":-1}

#Game intro
user_name = input("Enter Your Full Name Please : ")
wlc_msg = f"{f'Welcome {user_name} to Snake,Water,Gun Game':-^50}\n\n" \
          f"Instructions :\n" \
          f"{time.asctime(time.localtime())}\n" \
          f"You will be given 8 chances,and at the end," \
          f" one with the highest score will win.\n\n{'Wishing You All The Best':♨^55}\n" \
          f"Are you ready [Press Enter]?? //OR// \n" \
          f"Type --help or h for game rules\n"

char_animation(wlc_msg)

show_rules = input("Enter your choice here : ").strip().lower()
if show_rules in ['help', '--help','h']:
    print(game_rules)

# Take input from user
before_msg = '\nOkay!! Now you are entering the game...\n\nEnter Among These [Snake,Water,Gun]\n' \
             'or enter exit to quit\n'
char_animation(before_msg)

def map_choice(choice: str) -> object:
    choice = choice.strip().lower()
    if 's' in choice: return 'Snake'
    elif 'w' in choice: return 'Water'
    elif 'g' in choice : return "Gun"

#Defining Game_Event Loop
computer_points = 0
user_points = 0
chances = 8

def game_event_loop(chances,computer_choice,user_input):
    global user_points,computer_points

    # result_condition = {-2:False,-1:False,1:True,0:False, 2:False}

    result =  all_choices[computer_choice] - all_choices[user_input]

    print(result)



    # print("Out of exception ", chances, 'cmp choice -', computer_choice)

    print(f"You Chose [{user_input}]")

    if result == 1:
        print(f"Wohoo!! You got a point... I had chosen [{computer_choice}]\n"
              f"Point +1..\n\n")
        user_points +=1

    elif user_input == computer_choice :
        print(f"Woooh!! Its a Tie, I too chose {user_input}\n\n")
    else:
        print(f"OOps!! Better luck next time dude...Ha ha ha..I chose {computer_choice}\n"
              "Computer's Point +1..\n\n")
        computer_points+=1

def game_runner():
    global chances
    while chances :
        user_input = input(f"Enter choice,chances left {chances}: ").strip().lower()
        if user_input in ['exit', 'e', 'ex']:
            print("\n\nExit Requested....\nExiting from the game..")
            quit()

        try:
            user_input = map_choice(user_input)
            computer_choice = random.choice(list(all_choices.keys()))
            game_event_loop(chances, computer_choice, user_input)
            chances -= 1
        except Exception as e:
            print(e)
            print("\nGot an Input Error, please type correctly.\nContinuing Game...\n")
            continue


    else:
        time.sleep(1)
        char_animation('\n\nOhoooooyiii !! All Chances are finished.....\n\n')
        # winner = ( lambda cmp,usr:f'Computer\n\nKoi Baat nahi {user_name} phir se khel lo.. :)\n\n' if cmp>usr else user_name)(computer_points,user_points)
        if computer_points == user_points:
            winner = "It's a tie...Both have same points."
        elif computer_points>user_points:
            winner = f'Computer\n\nKoi Baat nahi {user_name} phir se khel lo.. :)\n\n'
        else:
            winner = user_name


        print(f"And The Winner is ......",end=' ')
        time.sleep(1)
        print(winner)
        print(f"Computer's score - {computer_points}\n{user_name}'s score : {user_points}\n\n")
        play_again = input("Wanna Play Again ?? : ").strip().lower()

        if play_again in ['y','yes']:
            print("\n\nDo you want to have a series ?\nYou can play with me multiple times and the scores will"
                  " keep adding and the final result after each match will be calculated on the basis of "
                  "the sum of the scores of the previous matches.\n")
            match_series = input("Want to Have a Series [y/n] ?: ")

            if match_series in ['y','yes']:

                globals()['user_points'] ,globals()['computer_points'] = 0,0

            chances = 8

            print(f'\n\n{f"Welcoming You Once Again {user_name}":=^50}')
            game_runner()


if __name__ == '__main__':

    game_runner()