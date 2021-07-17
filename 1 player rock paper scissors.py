# Rock paper scissors

import random

li_1 = ["Paper", "Rock"]
li_2 = ["Rock", "Scissors"]
li_3 = ["Scissors", "Paper"]

def result(move_1, move_2):

    if move_1 == move_2:
        return "Draw"
    else:
        if move_1 in li_1 and move_2 in li_1:
            return li_1[0]
        if move_1 in li_2 and move_2 in li_2:
            return li_2[0]
        if move_1 in li_3 and move_2 in li_3:
            return li_3[0]
        

n_games = int(input("How many games do you want to play? "))

computer_count = 0
user_count = 0
draw_count = 0

for i in range(n_games):
    
    move = str(input("Enter r for Rock, p for Paper, or s for Scissors: "))

    if move == "r":
        move_1 = "Rock"
    elif move == "p":
        move_1 = "Paper"
    else:
        move_1 = "Scissors"
    
    num = random.randint(1, 3)
    if num == 1:
        move_2 = "Rock"
    elif num == 2:
        move_2 = "Paper"
    else:
        move_2 = "Scissors"

    print("I give:", move_2)
    if result(move_1, move_2) == move_2:
        print("I win")
        computer_count += 1
    elif result(move_1, move_2) == move_1:
        print("You win")
        user_count += 1
    else:
        print(result(move_1, move_2))
        draw_count += 1

print("You won:", user_count, "times")
print("I won:", computer_count, "times")
print("There were", draw_count, "draws")

if computer_count > user_count:
    print("I won the tournament!")
elif computer_count < user_count:
    print("You won the tournament!")
else:
    print("It's a tie!")
