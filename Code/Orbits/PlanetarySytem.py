# Planetary simulation showing planets orbiting aroudn a star using the pygame library
# We solve the computations exactly using the angles between the planets 


import pygame
import math
import sys


# Initialize the game engine
pygame.font.init()

clock = pygame.time.Clock()
myfont = pygame.font.SysFont('Calibri', 20)
target_fps = 60
 
# Set the height and width of the screen
SIZE = [1280, 720]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Orbiting Planets around a Star")


class circle():
    def __init__(self,pos,vel,color,mass,num):
        self.x_vel, self.y_vel = vel
        self.x, self.y = pos
        self.color = color
        self.mass = mass
        self.num = num
        
    def update_velocity(self, x_vel, y_vel, override=False):
        self.x_vel += x_vel
        self.y_vel += y_vel
        if(override):
            self.x_vel = x_vel
            self.y_vel = y_vel
        
    def update_pos(self, pos=(),bouncein=False):
        if(pos != ()):
            self.x,self.y = pos
        else:
            if bouncein:
                if(self.x + self.x_vel > SIZE[0] or
                   self.x - self.x_vel < 0
                   ):
                    if(self.x > SIZE[0]):
                        self.x = SIZE[0] - 1
                    elif(self.x < 0):
                        self.x = 1
                    self.x_vel *= -1
                if(self.y + self.y_vel > SIZE[1] or
                   self.y - self.y_vel < 0
                   ):
                    if(self.y > SIZE[1]):
                        self.y = SIZE[1] - 1
                    elif(self.y < 0):
                        self.y = 1
                    self.y_vel *= -1
            self.x += self.x_vel
            self.y += self.y_vel           
    
    def get_text(self):
        msg = "n:{:.0f},x:{:.2f},y:{:.2f}\tvX:{:.2f},vY:{:.2f}".format(self.num,self.x,self.y,self.x_vel,self.y_vel)
        return msg
        
def draw_dot(screen,color,pos,radius):
    pygame.draw.circle(screen,color,pos,radius)
    
def g_between(Planet,Sun):
    r = math.sqrt((Planet.x-Sun.x)**2 + (Planet.y-Sun.y)**2) # Distance between the planets
    G = 6.67e-11 # Gravitational constant


    if(r > 0):            
        # Force and angle between the planets using Newton's Universal Law of Gravitation
        force = (G*Planet.mass*Sun.mass)/(r**2)
        theta = math.acos(abs(Planet.x-Sun.x)/r)

    
        x_vectorPlanet = force*math.cos(theta)/Planet.mass
        x_vectorSun = force*math.cos(theta)/Sun.mass

        y_vectorPlanet = force*math.sin(theta)/Planet.mass
        y_vectorSun = force*math.sin(theta)/Sun.mass

        
        if(Planet.x > Sun.x):
            x_vectorPlanet = -x_vectorPlanet

        if(Planet.y > Sun.y):
            y_vectorPlanet = -y_vectorPlanet

        
        Planet.update_velocity(x_vectorPlanet,y_vectorPlanet)
        Sun.update_velocity(x_vectorSun,y_vectorSun)
        
        # Print the new position
        msg1 = Planet.get_text()
        # msg2 = Sun.get_text()
        
        sys.stdout.write("\r{}".format(msg1))
        


def draw_text():
    # Helper function to draw information on the screen

    WHITE = (255,255,255)

    # Position and velocity details of the two planets
    infoSurface = myfont.render("Position and Velocity of the planets orbiting around the star: ", False, WHITE)

    # White Planet
    white_planet_text = "Position of the White Planet:   X: {:.0f}  Y: {:.0f}".format(c1.x,c1.y)
    posSurfaceWhite = myfont.render(white_planet_text, False, WHITE)
    white_vel = math.sqrt(c1.x_vel**2 + c1.y_vel**2)
    white_force_text = "Velocity of the White Planet:    V: {:.2f}  Vx: {:.2f}  Vy: {:.2f}".format(white_vel,
                                                                                       c1.x_vel,
                                                                                       c1.y_vel)

    forceSurfaceWhite = myfont.render(white_force_text, False, WHITE)
    

    # Red Planet
    red_planet_text = "Position of the Red Planet:   X: {:.0f}  Y: {:.0f}".format(c3.x,c3.y)
    posSurfaceRed = myfont.render(red_planet_text, False, WHITE)
    red_vel = math.sqrt(c3.x_vel**2 + c3.y_vel**2)
    red_force_text = "Velocity of the Red Planet:    V: {:.2f}  Vx: {:.2f}  Vy: {:.2f}".format(red_vel,
                                                                                       c3.x_vel,
                                                                                       c3.y_vel)
    
    forceSurfaceRed = myfont.render(red_force_text, False, WHITE)


    # Blue Planet
    blue_planet_text = "Position of the Blue Planet:   X: {:.0f}  Y: {:.0f}".format(c4.x,c4.y)
    posSurfaceBlue = myfont.render(blue_planet_text, False, WHITE)
    blue_vel = math.sqrt(c4.x_vel**2 + c4.y_vel**2)
    blue_force_text = "Velocity of the Blue Planet:    V: {:.2f}  Vx: {:.2f}  Vy: {:.2f}".format(blue_vel,
                                                                                       c4.x_vel,
                                                                                       c4.y_vel)
    
    forceSurfaceBlue = myfont.render(blue_force_text, False, WHITE)
    

    screen.blit(infoSurface,(0, 2))
    screen.blit(posSurfaceWhite,(0, 40))
    screen.blit(posSurfaceBlue,(0,60))
    screen.blit(posSurfaceRed,(0, 80))
    screen.blit(forceSurfaceWhite,(0, 120))
    screen.blit(forceSurfaceBlue,(0, 140))
    screen.blit(forceSurfaceRed,(0, 160))

    
# Create the planets and the Sun: 
# Planets:
c1 = circle((600,460), (-0.25, 0), [255,255,255], mass = 10e3, num = 1)
c3 = circle((600,560), (-0.20, 0), [255,0,0], mass = 10e8, num = 3) 
c4 = circle((600,500), (-0.23, 0), [0,0,255], mass = 10e4, num = 4)

# Sun:
c2 = circle((500,400), (0, 0), [255,255,0], mass = 10e10, num = 2) 

# Red Planet's moon:
c5 = circle((595,575), (-0.14, 0), [0,255,0], mass = 10, num = 5)



# Loop until the user clicks the close button:
done = False
while not done:

    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
 
    # Set the background and count the fps
    screen.fill([0,0,0])
    
    # Draw the two planets
    draw_dot(screen, c1.color, (round(c1.x), round(c1.y)), 5)
    draw_dot(screen, c3.color, (round(c3.x), round(c3.y)), 7)   
    draw_dot(screen, c4.color, (round(c4.x), round(c4.y)), 6)     
    draw_dot(screen, c2.color, (round(c2.x), round(c2.y)), 10)  # Sun  
    draw_dot(screen, c5.color, (round(c5.x), round(c5.y)), 2)    

    
    # Compute the force between the planets and update their positions
    g_between(c1,c2)
    g_between(c3,c2)
    g_between(c4,c2)
    g_between(c5,c3)
    g_between(c5,c2)
    c1.update_pos()
    c3.update_pos()
    c4.update_pos()
    c5.update_pos()
    c2.update_pos()
    
    draw_text()
    
    # Update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(target_fps)
