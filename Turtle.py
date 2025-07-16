import turtle
import math

bob = turtle.Turtle()

# Draw a square using simple commands
for _ in range(4):
    bob.fd(100)
    bob.lt(90)

# General function to draw a square of any length
def square(t, length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 90)

# Function to draw a polygon with n sides
def polygon(t, length, n):
    angle = 360 / n
    for _ in range(n):
        t.fd(length)
        t.lt(angle)

polygon(bob, 100, 5)  # Draw a pentagon

# Function to draw a circle by approximating with a polygon
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, length, n)

circle(bob, 100)

# Function to draw an arc
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for _ in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc(bob, 100, 180)

# General polyline function for code reuse
def polyline(t, n, length, angle):
    for _ in range(n):
        t.fd(length)
        t.lt(angle)

# Refactored polygon and arc to use polyline
def polygon1(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)

def arc1(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def circle1(t, r):
    arc1(t, r, 360)

# Example usage of the improved functions
bob.penup()
bob.goto(-200, 0)
bob.pendown()
square(bob, 80)

bob.penup()
bob.goto(0, 0)
bob.pendown()
polygon1(bob, 6, 60)

bob.penup()
bob.goto(200, 0)
bob.pendown()
circle1(bob, 50)

# Keep the window open until closed by the user
turtle.done()
