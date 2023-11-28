    if side1==side2==side3:
        return "Equilateral Triangle"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

side1 = int(input("Enter the length of side 1: "))
side2 = int(input("Enter the length of side 2: "))
side3 = int(input("Enter the length of side 3: "))

result = triangle_type(side1, side2, side3)
print("The triangle is a", result)