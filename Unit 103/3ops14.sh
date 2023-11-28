def triangle_type(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral Triangle"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"