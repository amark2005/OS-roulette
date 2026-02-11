import random as rand
import time


def main():
    os_list = []
    a = ""
    selectx = []
    entermsg="Please Enter to Continue..."
    try:
        player = int(input("Enter the number of players: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    while True:
        print("Enter the OS: ")
        a = input()
        if not a:
            break
        os_list.append(a)
    print("the os list is...")
    for i in os_list:
        time.sleep(0.5)
        print(i)
    input(entermsg)
    while True:
        index = rand.choice(os_list)
        selectx.append(index)
        if len(selectx) >= player:
            break
    for i in selectx:
        time.sleep(0.3)
        print(f"The selected ones are: {i}")
    selectx = list(set(selectx))
    time.sleep(0.5)
    print(selectx)
    input(entermsg)
    elimination_nominee=list(set(os_list)-set(selectx))
    time.sleep(0.3)
    print("Elimination Round begins...")
    time.sleep(0.3)
    print("These os are entering Elimination Round")
    for i in elimination_nominee:
        time.sleep(0.5)
        print(i)
    input(entermsg)
    eli_win=rand.choice(elimination_nominee)
    selectx.append(eli_win)
    time.sleep(0.7)
    print(f"The elimination round winner is {eli_win}")
    input(entermsg)
    time.sleep(0.5)
    print("The Final round Nominees are")
    for i in selectx:
        time.sleep(0.5)
        print(i)
    time.sleep(0.3)
    input(entermsg)
    time.sleep(0.5)
    print('The Winner is')
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print(rand.choice(selectx))
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
main()