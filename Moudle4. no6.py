import random

# Ask the user for number of random points
N = int(input("Enter the number of random points to generate: "))

inside_circle = 0  # counter for points inside the unit circle

for _ in range(N):
    x = random.uniform(-1, 1)  # random x between -1 and 1
    y = random.uniform(-1, 1)  # random y between -1 and 1

    # Check if the point is inside the circle
    if x**2 + y**2 < 1:
        inside_circle += 1

# Approximation of pi
pi_approx = 4 * inside_circle / N

print(f"Approximation of pi using {N} points: {pi_approx}")
