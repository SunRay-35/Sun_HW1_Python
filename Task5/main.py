# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print('Данная программы определяет расстояния между двумя точками на координатной плоскости')
x1 = int(input('Введите координату X первой точки: '))
y1 = int(input('Введите координату Y первой точки: '))
x2 = int(input('Введите координату X второй точки: '))
y2 = int(input('Введите координату Y второй точки: '))
if x1 > x2:
    delta_x = x1 - x2
else:
    delta_x = x2 - x1
if y1 > y2:
    delta_y = y1 - y2
else:
    delta_y = y2 - y1
print(f'Расстояние между точками ({x1};{y1}) и ({x2};{y2}) равно {round((delta_x**2+delta_y**2)**(0.5),2)}')