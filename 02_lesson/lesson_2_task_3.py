import math

def square(side):
    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area)
    return area

side_length = 4.3
area = square(side_length)
print(f"Площадь квадрата со стороной {side_length} равна {area}")