import random 

def dice_roll():
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    
    roll = die_1 + die_2
    
    return roll 
    
    
n_simulations = 10000
high_roll = 0
required_roll = 10

for i in range(n_simulations): 
    roll = dice_roll()
    
    if roll >= required_roll: 
        high_roll += 1
        
print(f'''The probability of two dice summing to {required_roll} or more is {
    high_roll/n_simulations}''')