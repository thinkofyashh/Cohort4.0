print("hello world")


print("hello world")







def get_choices() :
    player_choice=input("Enter the Player input for the choice :")


    computer_choice="Scissors"

    choices:dict= {"player " : player_choice ,"computer": computer_choice}

    return choices



def greetings():
    return "Hi , Welcome "


res=greetings()

print(res)

print(get_choices())