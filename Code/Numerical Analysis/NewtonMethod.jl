# Newton's method

x0 = 1  # The initial guess
f(x) = x^2 - 2  # The function whose root we are trying to find
fprime(x) = 2 * x  # The derivative of the function
tolerance = 10^(-7)  # 7 digit accuracy is desired
epsilon = 10^(-14)  # Do not divide by a number smaller than this
maxIterations = 20  # Do not allow the iterations to continue indefinitely
solutionFound = false  # Have not converged to a solution yet

for i = 1:maxIterations
  y = f(x0)
  yprime = fprime(x0)
 
  if abs(yprime) < epsilon  # Stop if the denominator is too small
    break
  end
 
  global x1 = x0 - y/yprime  # Do Newton's computation
 
  if abs(x1 - x0) <= tolerance  # Stop when the result is within the desired tolerance
    global solutionFound = true
    break
  end
 
  global x0 = x1  # Update x0 to start the process again
end

if solutionFound
  println("Solution: ", x1)  # x1 is a solution within tolerance and maximum number of iterations
else
  println("Did not converge")  # Newton's method did not converge
end