import math

# Power: 2 raised to 1.25
x = math.pow(2, 1.25)
print("2 raised to 1.25:", x)

# Floor and ceil
print("math.floor(x):", math.floor(x))  # Largest integer <= x
print("math.ceil(x):", math.ceil(x))    # Smallest integer >= x

# Square root
print("math.sqrt(16):", math.sqrt(16))

# Exponential (e^2)
print("math.exp(2):", math.exp(2))

# Logarithms
print("math.log(100):", math.log(100))           # Natural log (base e)
print("math.log10(100):", math.log10(100))       # Base-10 log
print("math.log2(8):", math.log2(8))             # Base-2 log

# Trigonometric functions (angles in radians)
angle_rad = math.pi / 4  # 45 degrees in radians
print("sin(45°):", math.sin(angle_rad))
print("cos(45°):", math.cos(angle_rad))
print("tan(45°):", math.tan(angle_rad))

# Constants
print("math.pi:", math.pi)
print("math.e:", math.e)

# Factorial
print("math.factorial(5):", math.factorial(5))

# Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
print("math.gcd(24, 36):", math.gcd(24, 36))
print("math.lcm(15, 20):", math.lcm(15, 20))

# Absolute value and copy sign
print("math.fabs(-7.5):", math.fabs(-7.5))
print("math.copysign(5, -3):", math.copysign(5, -3))

# Radians and degrees conversion
print("math.degrees(math.pi):", math.degrees(math.pi))  # Radians to degrees
print("math.radians(180):", math.radians(180))          # Degrees to radians
