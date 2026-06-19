import math

print('==================')
print('Area Calculator 📐')
print('==================')

print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')

shape = int(input('Which shape: '))

area = 0

if shape == 1:
    base = float(input('Base: '))
    height = float(input('Height: '))
    area = (height * base) / 2
    print('Your area is:', area)
elif shape == 2:
    base = float(input('Base: '))
    height = float(input('Height: '))
    area = height * base
    print('Your area is:', area)
elif shape == 3:
    side = float(input('Side: '))
    area = side * side
    print('Your area is:', area)
elif shape == 4:
    radius = float(input('Radius: '))
    area = math.pi * radius * radius
    print('Your area is:', area)
else:
    print('Goodbye')