import random
import numpy as np
import matplotlib.pyplot as plt


# The host will reveal a door that doesn't contain the prize
def get_non_prize_door(host, num_doors, player_choice):
  i = 1
  while (i == host or i== player_choice ):
    i = (i+1)%(num_doors)
  
  return i

# Have the player switch to the other unopened door
def switch_function(shown_door, num_doors, player_choice):
  i = 1
  while (i == shown_door or i== player_choice ):
    i = (i+1)%(num_doors)
  
  return i


# Play the game 
def monty_hall_game(switch, num_tests):
  win_switch_cnt = 0
  win_no_switch_cnt = 0
  lose_switch_cnt = 0
  lose_no_switch_cnt = 0

  # Get the doors
  doors = [0,1,2] 

  # Get the number of doors
  num_doors = len(doors) 
  
  
  for i in range(0,num_tests):
    # Randomly choose the door with the wanted prize
    door_with_prize = random.randint(0, num_doors-1) 

    # The host knows which door has the prize
    host = door_with_prize 

    # The player initially chooses a random door that they believe has the prize
    player_choice = random.randint(0, num_doors-1) 
    original_player_choice = player_choice
    shown_door = get_non_prize_door(host, num_doors, player_choice)

    if switch == True:
      player_choice = switch_function(shown_door,num_doors, player_choice)
    
    if player_choice == host and switch == False:
      # The player wins from not switching
      print('Player Wins (No Switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice ,', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      win_no_switch_cnt = win_no_switch_cnt + 1

    elif player_choice == host and switch == True:
      # The player wins from switching
      print('Player Wins (Switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      win_switch_cnt = win_switch_cnt +1

    elif player_choice != host and switch == False:
      # The player loses from not switching
      print('Player Lost (No Switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      lose_no_switch_cnt = lose_no_switch_cnt + 1

    elif player_choice != host and switch == True:
      # The player loses from switching
      print('Player Lost (Switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      lose_switch_cnt = lose_switch_cnt + 1


  return win_no_switch_cnt,win_switch_cnt,lose_no_switch_cnt,lose_switch_cnt, num_tests




# Play the game
num_tests = []
win_percentage = []
switch = True

for i in range(1,100):
  num_tests.append(i) 
  y = monty_hall_game(switch, i) 
  win_percentage.append(y[1]/ y[4]) 


# Visually show the number of tests and the win percentage 

# Expected winning porbability 
x = np.linspace(0, 100, 100000)

@np.vectorize
def constant_function(xyz):
    return 0.66

plt.plot(x,constant_function(x), dashes=[6, 2], color = "red")


plt.plot( num_tests, win_percentage  )
plt.title('Monty Hall Problem')
plt.xlabel('Number of Tests',fontsize=18)
plt.ylabel('Win Percentage',fontsize=18)
plt.show()

print('The win percentage for test playing ', y[4], ' games is:' ,y[1]/ y[4])