# 1. OPTIMIZATION IN SCIPY

# Application: Find the dimensions of a rectangle with a fixed perimeter that maximizes the area.
from scipy.optimize import minimize

# Define the function to maximize (negative area for minimization)
def objective(x):
    return -(x[0] * x[1])  # Area = length * width

# Constraints: Perimeter = 20 -> 2*(length + width) = 20
constraints = [{'type': 'eq', 'fun': lambda x: 2 * (x[0] + x[1]) - 20}]

# Bounds for length and width
bounds = [(0, None), (0, None)]

# Initial guess
initial_guess = [1, 1]

# Perform optimization
result = minimize(objective, initial_guess, bounds=bounds, constraints=constraints)

print("Optimal dimensions:", result.x)
print("Maximum area:", -result.fun)


# 2. STATISTICS
# SciPy provides statistical functions to compute probabilities, distributions, and summaries.
# Application: Compute the mean, variance, and PDF of a normal distribution.

from scipy.stats import norm

# Mean and standard deviation
mean, std_dev = 0, 1

# Create a normal distribution
dist = norm(loc=mean, scale=std_dev)

# Compute PDF at specific points
x_values = [-2, 0, 2]
pdf_values = dist.pdf(x_values)

print("PDF values at", x_values, ":", pdf_values)
print("Mean:", dist.mean(), "Variance:", dist.var())


# 3. Signal Processing
# SciPy includes tools for filtering and signal analysis.
# Application: Apply a low-pass filter to remove noise from a signal.

from scipy.signal import butter, lfilter
import numpy as np

# Create a noisy signal
np.random.seed(42)
t = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 5 * t) + np.random.normal(0, 0.5, len(t))

# Design a low-pass Butterworth filter
b, a = butter(4, 0.1)

# Apply the filter
filtered_signal = lfilter(b, a, signal)

# Compare original and filtered signals
print("Original signal:", signal[:10])
print("Filtered signal:", filtered_signal[:10])


# 4. Integration
# SciPy can compute definite integrals and solve differential equations.
# Application: Compute the area under a curve.

from scipy.integrate import quad
import numpy as np

# Define the function
def func(x):
    return np.sin(x)

# Integrate from 0 to pi
result, error = quad(func, 0, np.pi)

print("Integral of sin(x) from 0 to π:", result)

# 5. Linear Algebra
# SciPy extends NumPy's linear algebra capabilities with advanced solvers.
# Application: Solve a system of linear equations.

from scipy.linalg import solve

# Coefficient matrix (A) and constant vector (b)
A = [[3, 1], [1, 2]]
b = [9, 8]

# Solve the system Ax = b
x = solve(A, b)

print("Solution to the system Ax = b:", x)


