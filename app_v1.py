import random


def main():
    print("=========== 席替えアプリ =============")
    with open("members.txt", mode="r")as f:
        members = f.read().split("\n")

    new_members = random.sample(members, len(members))
    for position in range(0, len(new_members)):
        if position == 0:       print("Table1:", end=" ")
        if position <= 5:       print(new_members[position], end=" ")

        if position == 5:       print("\nTable2:", end=" ")
        if 5 < position <= 10:  print(new_members[position], end=" ")

        if position == 10:      print("\nTable3:", end=" ")
        if 10 < position <= 15: print(new_members[position], end=" ")


if __name__ == "__main__":
    main()
