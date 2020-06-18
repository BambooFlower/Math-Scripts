# Spacecraft orbit around the Earth using Forward Euler

import numpy
import matplotlib.pyplot

h = 0.01 # Time-step
earth_mass = 5.97e24 # in kilogram
gravitational_constant = 6.67e-11 # N m2 / kg2

def acceleration(spaceship_position):
    # Assume the Earth is located at the origin
    vector_to_earth = -spaceship_position
    return gravitational_constant * earth_mass / \
           numpy.linalg.norm(vector_to_earth)**3 *vector_to_earth

    
def ship_trajectory():
    num_steps = 1320000
    x = numpy.zeros([num_steps + 1, 2]) # in meters
    v = numpy.zeros([num_steps + 1, 2]) # in meters per second

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3

    for step in range(num_steps):
        x[step+1] = x[step] + h*v[step]
        v[step+1] = v[step] + h*acceleration(x[step])

    return x, v

x, v = ship_trajectory()


matplotlib.pyplot.plot(x[:, 0], x[:, 1])
matplotlib.pyplot.scatter(0, 0)
matplotlib.pyplot.axis('equal')
matplotlib.pyplot.title('Example of Elliplictal Orbit around the Earth')
axes = matplotlib.pyplot.gca()
axes.set_xlabel('Longitudinal position in meters')
axes.set_ylabel('Lateral position in meters')
matplotlib.pyplot.show()

  


