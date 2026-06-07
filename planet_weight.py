earth_weight = float(input('earth weight: '))
planet_number = int(input('planet number: '))

if planet_number == 1:
  relative_gravity = 0.38
elif planet_number == 2:
  relative_gravity = 0.91
elif planet_number == 3:
  relative_gravity = 0.38
elif planet_number == 4:
  relative_gravity = 2.53
elif planet_number == 5:
  relative_gravity = 1.07
elif planet_number == 6:
  relative_gravity = 0.89
elif planet_number == 7:
  relative_gravity = 1.14
else:
  print('invalid number')

destination_weight = earth_weight * relative_gravity
print(destination_weight)