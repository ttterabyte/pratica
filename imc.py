mass = float(input('seu peso (kg): '))
height = float(input('sua altura (m): '))
bmi = mass / (height ** 2)
print(bmi)


if bmi < 18.5:
    print('bo come fiote')
elif bmi < 24.9:
    print('ta saudavel')
else:
    print('gordo')

#ezzzz eze z ez ez