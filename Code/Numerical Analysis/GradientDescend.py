# Example of Gradient Descent

x = 6  # Starting point
step_size = 0.01
step_tolerance = 0.00001
max_iterations = 10000

# Derivative function f'(x)
df = lambda x: 4 * x**3 - 9 * x ** 2

# Gradient descent iteration
for j in range(max_iterations):
    step = step_size * df(x)
    x -= step

    if abs(step) <= step_tolerance:
        break

print('Minimum:', x) # 2.2499646074278457
print('Exact:', 9/4) # 2.25
print('Iterations:',j) # 69