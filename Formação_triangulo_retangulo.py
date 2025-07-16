# This script checks whether three given segments can form a triangle,
# and if so, whether it is a right triangle.

# Input: three segment lengths
side1 = float(input('Enter the length of the first segment: '))
side2 = float(input('Enter the length of the second segment: '))
side3 = float(input('Enter the length of the third segment: '))

# To form a triangle: the sum of any two sides must be greater than the third side
can_form_triangle = (
    side1 + side2 > side3 and
    side1 + side3 > side2 and
    side2 + side3 > side1
)

if can_form_triangle:
    # Sort sides so that hypotenuse is the largest
    sides = sorted([side1, side2, side3])
    cateto1, cateto2, hypotenuse = sides  # The largest will be the hypotenuse

    # Check for right triangle using Pythagoras' theorem
    if abs(hypotenuse**2 - (cateto1**2 + cateto2**2)) < 1e-8:
        print(f"The segments form a right triangle with hypotenuse {hypotenuse} and legs {cateto1} and {cateto2}.")
    else:
        print("The segments form a triangle, but it is not a right triangle.")
else:
    print("The segments cannot form any triangle.")
