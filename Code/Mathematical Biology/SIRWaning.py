# SIR model with waning immunity

import matplotlib.pyplot
import numpy

h = 0.5 # days (timestep)
end_time = 60. # days
num_steps = int(end_time / h)
times = h * numpy.array(range(num_steps + 1))

def waning():
    transmission_coeff = 5e-9 # 1 / (day * person)
    infectious_time = 5. # days

    waning_time = infectious_time *2.0 #days

    s = numpy.zeros(num_steps + 1)
    i = numpy.zeros(num_steps + 1)
    r = numpy.zeros(num_steps + 1)

    s[0] = 1e8 - 1e6 - 1e5
    i[0] = 1e5
    r[0] = 1e6

    for step in range(num_steps):
        s2i = h * transmission_coeff * s[step] * i[step]
        i2r = h / infectious_time * i[step]
        r2s = h / waning_time*r[step]
        s[step + 1] = s[step] + r2s - s2i
        i[step + 1] = i[step] + s2i - i2r
        r[step + 1] = r[step] + i2r - r2s

    return s, i, r

s, i, r = waning()



s_plot = matplotlib.pyplot.plot(times, s, label = 'Susceptible')
i_plot = matplotlib.pyplot.plot(times, i, label = 'Infectious')
r_plot = matplotlib.pyplot.plot(times, r, label = 'Removed')
matplotlib.pyplot.legend(('Susceptible', 'Infectious', 'Removed'), loc = 'upper right')
matplotlib.pyplot.title('Population dynamics for the SIR model')

axes = matplotlib.pyplot.gca()
axes.set_xlabel('Time in days')
axes.set_ylabel('Number of persons')
matplotlib.pyplot.xlim(xmin = 0.)
matplotlib.pyplot.ylim(ymin = 0.)
matplotlib.pyplot.show()


