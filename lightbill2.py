try: # data input for usage
 people = int(input('How many people use the electrical appliance? '))
 minutes = int(input('For how many minutes each (per day)? '))

 # calculate daily usage in hours
 daily_use = people * minutes
 hours_per_day = daily_use / 60

 # period of days to calculate
 days = int(input('How many days would you like to calculate for? '))

 # Power input and conversion (Watts to kW)
 power = float(input('How many Watts does the appliance use? '))
 power_kw = power / 1000

 # calculate total energy consumption (kWh)
 energy_kwh = power_kw * hours_per_day * days

 # electricity tariff input
 tariff = float(input('What is the kWh rate on your electricity bill (e.g., 0.75)? $ '))

 # calculate total cost
 total_cost = energy_kwh * tariff

 # display the final result
 print(f'The estimated cost for {days} days is: $ {total_cost:.2f}')
except ValueError:
  print('\n[Error] Invalid input. Please enter numbers only.')  