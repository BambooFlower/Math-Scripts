import random
import numpy as np

n_simulations = 100000

# Ant movement function
def ant_direction(): 
    # -1 is left, 1 is right for the x-axis 
    # -1 is down, 1 is up for the y-axis 
    direction = [random.uniform(-1, 1), random.uniform(-1, 1)]
    if abs(direction[0]) > abs(direction[1]): 
        direction[1] = 0
        if direction[0] > 0: 
            direction[0] = np.ceil(direction[0])
        else:
            direction[0] = np.floor(direction[0])
    else: 
        direction[0] = 0
        if direction[1] > 0: 
            direction[1] = np.ceil(direction[1])
        else:
            direction[1] = np.floor(direction[1])
            
    return direction         
    
# Boundary 
def boundary(): 
    x = input("Enter the x coordinate of the boundary's center: ")
    y = input("Enter the y coordinate of the boundary's center: ")
    radius = input("Enter the radius of the boundary: ")
    is_ellipse = input("Do you want an ellipsoidal boundary? (Yes/No) ")
    if (is_ellipse.lower() == 'yes') or (is_ellipse.lower() == 'y'): 
        a = input("Enter the value for half the width (a): ")
        b = input("Enter the value for half the height (b): ")
    elif (is_ellipse.lower() == 'no') or (is_ellipse.lower() == 'n'):
        print("The bourndary is a circle")
        a = 1
        b = 1
    else: 
        is_ellipse = input("Do you want an ellipsoidal boundary? (Yes/No) ")
    
    boundary_list = [x, y, radius, a, b]
        
    return boundary_list

time_list = []
all_numbers = False
while all_numbers == False: 
    input_boundary = boundary()
    try: 
        boundary = list(map(float, input_boundary))
        all_numbers = True
    except ValueError:
        print("Every input needs to be a number")
        
required_time = 0
ellipse_x = boundary[0]
ellipse_y = boundary[1]
radius = boundary[2]
a = boundary[3]
b = boundary[4]
    
for i in range(n_simulations): 
    time = 0
    found_food = False
    position = [0, 0]    

    while found_food == False: 
        direction = ant_direction()
        direction = [x*10 for x in direction]
        time += 1

        zipped = zip(position, direction)
        position = [x + y for (x, y) in zipped]
        
        # Food located on a square of side 20 with center the origin
        # if abs(position[0]) == 20 or abs(position[1]) == 20: 
        #     found_food = True
        #     time_list.append(time)
            
        # Food located diagonally on a line passing through (10, 0) and (0, 10)
        # Don't run it the Expected time is Inf
        # if (position[0] + position[1]) == 10: 
        #     found_food = True
        #     time_list.append(time)
        
        # Food located on a custom (ellipsoidal) boundary 
        x = position[0]
        y = position[1]
        
        if ((x - ellipse_x)/a)**2 + ((y - ellipse_y)/b)**2 >= radius**2:        
            found_food = True
            time_list.append(time)
    
    required_time += time_list[i]

print(f'''The ant will take on average {required_time/n_simulations} seconds to 
      reach the food''')
    
