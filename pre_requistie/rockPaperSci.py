



import random

def get_choice():
    options=["rock","paper","sci"]

    computer_choice=random.choice(options)
    player_choice=input("Enter the Player choice (Rock,Paper,Sci)").lower()

    choices={
        "player": player_choice,
        "Computer" :computer_choice
    }

    return choices

def who_win(player,computer):
    print(f"Your choice is {player},Computer Choice is {computer}")

    if(player==computer):
        return "It is a Tie"
    elif((player=="rock" and computer=="sci") or (player=="sci" and computer=="paper") or (player=="paper" and computer=="rock")):
        return "Player Won"
    else :
        return "Computer Won"


res=get_choice()

ans =who_win(res["player"],res["Computer"])

print(ans)