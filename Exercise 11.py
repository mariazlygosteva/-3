import math

a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))
c = int(input("Введите длину стороны c: "))

def calculate_angles(a, b, c):
    angle_a = int(math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c))))
    angle_b = int(math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c))))
    angle_c = int(180 - angle_a - angle_b)
    return angle_a, angle_b, angle_c

angle_a, angle_b, angle_c = calculate_angles(a, b, c)

print(f"Угол A: {angle_a} градусов")
print(f"Угол B: {angle_b} градусов")
print(f"Угол C: {angle_c} градусов")