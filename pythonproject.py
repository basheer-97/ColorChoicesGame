import random
print("\n Winning Rules of the Colour choices Game is as follows: \n Enter a number from one to five and match computer choice to win the game.") 
computer_score = 0
player_score = 0 
def playagain():
    choice=input('Do you want to play again(y/n):')
    if choice=='y':
        return True
    else:
        return False

while True: 
    print("\n Red = 1 \n Yellow = 2 \n Orange = 3 \n Green = 4 \n Blue = 5 \nTake a turn ") 
 
    # take the input from user 
    player_choice = int(input("User turn, please enter your choice: ")) 
  
   
    # looping until user enters invalid input 
    while player_choice > 5 or player_choice<1: 
        player_choice = int(input("enter valid input: "))
          
  
    if player_choice == 1: 
        choice_col = 'red'
    elif player_choice == 2: 
        choice_col = 'yellow'
    elif player_choice == 3: 
        choice_col= 'orange'
    elif player_choice== 4: 
        choice_col = 'green'    
    elif player_choice==5:
        choice_col = 'blue'
    else:
        print("invalid choice")
        break  
    # print user choice  
    print("User colour choice is: " , choice_col) 
    print("\n Now its computer turn to choose a colour.......") 
  
    
    computer_choice = random.randint(1, 5) 
      
   
    while computer_choice == player_choice: 
        computer_choice = random.randint(1, 5) 
  
    if computer_choice == 1: 
        compu_choice_col = 'red'
    elif computer_choice == 2: 
        compu_choice_col = 'yellow'
    elif computer_choice == 3: 
        compu_choice_col = 'orange'
    elif computer_choice == 4: 
        compu_choice_col = 'green'    
    else: 
        compu_choice_col = 'blue'
          
    print("Computer color choice is: ", compu_choice_col) 

    # conditions for winning 
    if(choice_col == compu_choice_col):
        player_score += 1
        print("player_score: ",player_score)
        print("computer_score: ",computer_score)
    else:
        computer_score += 1
         
        print("player_score: ", player_score)
        print("computer_score: ",computer_score)
    if not playagain():
        break

if computer_score == player_score:
    print("Game is Tied")
    print("\n Thanks for playing") 
elif computer_score < player_score:
    print("Player is Victorious")
    print("<== User wins ==>")
    print("\n Thanks for playing")
elif computer_score > player_score:
    print("\n<== Computer wins ==>")
    print("\nPlayer is Defeated")
    print("\nThanks for playing")  
