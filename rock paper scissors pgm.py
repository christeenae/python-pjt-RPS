import random
def play():
    print("we are gonna play rock-paper-scissor")
    user= input("In this game we have 'r' for rock ,'p' for paper ,'s' for scissors now what's your choice:")
    computer=random.choice(['r','p','s'])

    if user== computer:
        return "It's a tie"
        
    if is_win(user,computer):
            return "You Won!"

    return "You Lost!"

 
def is_win(player,opponent):
              if(player=='r' and opponent=='s')or (player=='s' and opponent=='p') or(player=='p' and opponent=='r'):
                 return True

print(play())
