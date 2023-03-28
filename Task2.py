import math


# функция для вычисления Манхэттенского расстояния между двумя точками
def manhattan_distance(x1, y1, x2, y2, height):
    return abs(x1 - x2) + abs(y1 - y2) + 2 * height


# считываем данные из файла
with open('file.txt', 'r') as f:
    locations = [line.strip() for line in f]

# определяем высоту каждой площадки на основе адреса
heights = []
for location in locations:
    # здесь нужно определить высоту объекта на основе его адреса, например, с помощью 2GIS
    height = 2 * 3  # удвоенная высота равна удвоенной высоте этажа
    heights.append(height)

# вычисляем расстояние между каждой парой площадок и суммируем их
total_distance = 0
for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        loc1 = locations[i]
        loc2 = locations[j]
        height1 = heights[i]
        height2 = heights[j]
        # здесь нужно определить координаты объектов на основе их адреса, например, с помощью 2GIS
        x1, y1 = 0, 0
        x2, y2 = 0, 0
        distance = manhattan_distance(x1, y1, x2, y2, max(height1, height2))
        total_distance += distance

print(f"Для соединения всех площадок потребуется {total_distance} метров оптического кабеля.")
