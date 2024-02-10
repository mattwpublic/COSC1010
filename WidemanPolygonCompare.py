#Matthew Wideman
#COSC1010 401
#9/19/22

shape1 = input("What is your first shape?")
sideLength1 = float(input("What is the length of its side?"))
shape2 = input("What is your second shape?")
sideLength2 = float(input("What is the length of its side?"))

if shape1 == 'triangle':
    area1 = ((3**(1.0/2))/4)*(sideLength1**2)
    per1 = (sideLength1 * 3)
elif shape1 == 'square':
    area1 = (sideLength1**2)
    per1 = (sideLength1 * 4)
elif shape1 == 'hexagon':
    area1 = ((3*(3**(1.0/2)))/2)*(sideLength1**2)
    per1 = (sideLength1 * 6)
else:
    print("ERROR: first shape is not a triangle, square, or hexagon.")
    exit()

if shape2 == 'triangle':
    area2 = ((3**(1.0/2))/4)*(sideLength2**2)
    perimeter2 = (sideLength2 * 3)
elif shape2 == 'square':
    area2 = (sideLength2**2)
    perimeter2 = (sideLength2 * 4)
elif shape2 == 'hexagon':
    area2 = ((3*(3**(1.0/2)))/2)*(sideLength2**2)
    perimeter2 = (sideLength2 * 6)
else:
    print("ERROR: second shape is not a triangle, square, or hexagon.")

if area1 > area2:
    print("Polygon 1's area is larger")
    print(area1, area2)
elif area1 < area2:
    print("Polygon 2's area is larger")
    print(area1, area2)
else:
    print("The areas are equal")
    print(area1, area2)

if per1 > perimeter2:
    print("Polygon 1's perimeter is larger")
    print(per1, perimeter2)
elif per1 < perimeter2:
    print("Polygon 2's perimeter is larger")
    print(per1, perimeter2)
else:
    print("The perimeters are equal")
    print(per1, perimeter2)
