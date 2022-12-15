# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Данная программы определяет номер четверти по координатам')
x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))
if (x == 0 and y == 0):
    print(f'Точка({x};{y}) лежит в точке начала координат')
elif (x == 0 and y > 0):
    print(f'Точка({x};{y}) лежит на оси Y между I и II четвертями')    
elif (x == 0 and y < 0):
    print(f'Точка({x};{y}) лежит на оси Y между III и IV четвертями')
elif (x > 0 and y == 0):
    print(f'Точка({x};{y}) лежит на оси X между I и IV четвертями')    
elif (x < 0 and y == 0):
    print(f'Точка({x};{y}) лежит на оси X между II и III четвертями')    
elif (x > 0 and y > 0):
    print(f'Точка({x};{y}) лежит в I четверти')
elif (x < 0 and y > 0):
    print(f'Точка({x};{y}) лежит в II четверти')
elif (x > 0 and y < 0):
    print(f'Точка({x};{y}) лежит в IV четверти')
else:
    print(f'Точка({x};{y}) лежит в III четверти')