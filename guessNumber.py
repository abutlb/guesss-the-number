import csv
import os.path
import random
import time


if not os.path.isfile("leaderboard.csv"):
    op = open("leaderboard.csv", "w", newline='')
    headers = ['name', 'score']
    data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
    data.writerow(dict((heads, heads) for heads in headers))
    op.close()


opening_msg = """******************************************
game made by :@abutlb
1.play
2.leaderboard
3.quit
******************************************
"""

begin_msg = """******************************************
welcome to guess the number game
you have to guess the number from 1 to 100 
good good luck and you have 4 tries
write quit for quitting"""

lives = 4


def play_game(lives):
    print(begin_msg)
    number = random.randint(1, 100)
    devided_by_2 = "it can be devided by 2" if number % 2 == 0 else "it can't be devided by 2"
    devided_by_3 = "it can be devided by 3" if number % 3 == 0 else "it can't be devided by 3"
    devided_by_5 = "it can be devided by 5" if number % 5 == 0 else "it can't be devided by 5"
    while lives > 0:
        print("******************************************")
        guessed_number = input("guess the number : ")
        if guessed_number.lower() in "quit":
            quitting()
        if not guessed_number.isnumeric():
            print("not a number!!")
        else:
            guessed_number = int(guessed_number)
            lowORhigh = "lower" if number < guessed_number else "higher"
            alotOrlittle = "a lot " if number-guessed_number > 10 or number-guessed_number < -10 else "a little "
            if number == guessed_number:
                print("you guessed it right ^_^")
                name = input("whats your name? ")
                write_to_leaderboard(name, lives)
                break
            else:
                print(f"go {alotOrlittle}{lowORhigh}!!!") if lives > 1 else print(f"nice try the number is {number}")
                if lives == 4:
                    print(devided_by_2)
                elif lives == 3:
                    print(devided_by_3)
                elif lives == 2:
                    print(devided_by_5)
            lives -= 1
            if lives > 0:
                print(f"you have {lives} tries left")


def write_to_leaderboard(name, score):
    op = open("leaderboard.csv", "r")
    dt = csv.DictReader(op)
    up_dt = []
    for r in dt:
        row = {'name': r['name'],
               'score': r['score']}
        up_dt.append(row)
    op.close()
    up_dt.append({"name": name, "score": score})
    op = open("leaderboard.csv", "w", newline='')
    headers = ['name', 'score']
    data = csv.DictWriter(op, delimiter=',', fieldnames=headers)
    data.writerow(dict((heads, heads) for heads in headers))
    data.writerows(up_dt)
    op.close()


def read_from_leaderboard():
    with open("leaderboard.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        reader = sorted(reader, key=lambda item: item.get("score"), reverse=True)
        if len(reader) == 0:
            print("no players recorded")
        elif len(reader) < 5:
            i = 1
            for player in reader:
                print(f"{i}- {player['name']}  {player['score']}")
                i += 1
        else:
            i = 1
            for player in reader[0:5]:
                print(f"{i}- {player['name']}  {player['score']}")
                i += 1
        csv_file.close()



def quitting():
    print("see you later ^_^")
    time.sleep(2)
    quit()


while True:
    option_number = input(opening_msg).lower()
    if option_number in "1.play":
        play_game(lives)
    elif option_number in "2.leaderboard":
        read_from_leaderboard()
    elif option_number in "3.quit":
        quitting()
    else:
        print("not available option!!!")
