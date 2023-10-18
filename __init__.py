import areas
import combinatorics

choice = input('выберите модуль: ')
if 'комбинаторика' in choice.lower():
    choice2 = input('выберите формулу: ')
    if 'факториал' in choice2.lower():
        n = int(input('введите число: '))
        print(combinatorics.factorial(n))
    elif 'перестановка' in choice2.lower():
        n = int(input()) # length
        k = int(input()) # 1 to k
        s = [k+1 for k in range(k)]
        for line in combinatorics.permutation(s):
            print(line)       
elif 'геометрия' in choice.lower():
    choice2 = input('выберите формулу: ')
    if 'прямоугольник' in choice2.lower():
        a = int(input('a: '))
        b = int(input('b: '))
        print(areas.rectangle(a, b))
    if 'квадрат' in choice2.lower():
        a = int(input('a: '))
        print(areas.square(a))
    if 'треугольник' in choice2.lower():
        a = int(input('a: '))
        h = int(input('h: '))
        print(areas.triangle(a, h))
    if 'шар' in choice2.lower():
        r = int(input('r: '))    
        print(areas.sphere(r))       


