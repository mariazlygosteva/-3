import math

university = (-200, 300)
victory_square = (300, -350)

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

total_distance = distance(university, victory_square)

print("Расстояние, преодоленное дроном до сквера Победы (в метрах):", round(total_distance))