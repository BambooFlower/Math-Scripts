import random

n_simulations = 1000000
inside_circle = 0

for i in range(n_simulations): 
    # The point is generated in the unit square
    point = [random.uniform(0, 1), random.uniform(0, 1)]
    
    if point[0]**2 + point[1]**2 < 1: 
        inside_circle += 1
        
print(f'''The estimated value of pi after 10000 using Buffon's method is {
    4*inside_circle/n_simulations}''')