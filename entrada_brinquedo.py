height = int(input('your height(cm): '))
credits = int(input('your credits: '))

if height >= 137 and credits >= 10:
  print('enjoy the ride')
elif height < 137 and credits >= 10:
  print('you are not tall enough to ride')
elif height >= 137 and credits < 10:
  print('you dont have enought credits')
else:
  print('you dont have not met either requirement')