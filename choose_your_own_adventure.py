name = input("Type your name : ")
print("Welcome", name, " to this adventure")
answer = input(
    "You are on a dirt road , it has come to an end you can go left or right.Which way would you like to go ? (left/right) "
).lower()

if answer == "left":
    answer = input(
        "You come to a river,you can walk around it or swim accross? Type walk to walk around and swim toaccross? (swim/walk) "
    )

    if answer == "swim":
        print("You swam accross and were eaten by an alligator ")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the gane .")

    else:
        print("Not a valid option.You lose. ")


elif answer == "right":
    answer = input(
        "YOu come to a bridge,it looks wobbly,do you want to cross it or head back (cross/back)?"
    )

    if answer == "back":
        print("You go back and lose  ")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger.Do you talk them ? (yes/no)"
        )
        if answer == "yes":
            print("You talked to a stranger and he give you gold.You WIN!")

        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")

        else:
            print("Not a valid option")

    else:
        print("Not a valid option.You lose. ")


else:
    print("Not a valid option.You lose")


print(f"Thank you for trying {name}")
