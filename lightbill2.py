try:
    people = int(input('How many people use the electrical appliance? '))
    minutes = int(input('For how many minutes each (per day)? '))

    daily_use = people * minutes
    hours_per_day = daily_use / 60

    days = int(input('How many days would you like to calculate for? '))

    power = float(input('How many Watts does the appliance use? '))
    power_kw = power / 1000

    energy_kwh = power_kw * hours_per_day * days

    base_tariff = float(input('What is the base kWh rate (for the first 50 kWh)? $ '))
    additional_charge = float(input('How much does the tariff increase every 50 kWh? $ '))

    total_cost = 0.0
    remaining_energy = energy_kwh
    faixa = 0

    while remaining_energy > 0:
        energy_in_this_faixa = min(remaining_energy, 50.0)
        
        current_tariff = base_tariff + (faixa * additional_charge)

        total_cost += energy_in_this_faixa * current_tariff

        remaining_energy -= energy_in_this_faixa
        faixa += 1

    print(f'\nTotal energy consumed: {energy_kwh:.2f} kWh')
    print(f'The estimated cost for {days} days is: $ {total_cost:.2f}')

except ValueError:
    print('\n[Error] Invalid input. Please enter numbers only.')