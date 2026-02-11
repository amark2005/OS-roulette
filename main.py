import random

def main():
    os_list = ["amar", "vicky", "pradeep"]
    a = ""
    selectx = []
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
        print(i)
    while True:
        index = random.randint(0, len(os_list) - 1)
        selectx.append(os_list[index])
        if len(selectx) >= player:
            break
    for i in selectx:
        print(f"The selected ones are: {i}")
    selectx = list(set(selectx))
if __name__ == "__main__":
    main()