penguin = int(input("Enter the number of penguins:"))
seals = int(input("Enter the number of seals:"))
polarBears = int(input("Enter the number of polar bears:"))
daily_penguin_ration = 0.9
daily_seal_ration = 2.9
daily_polar_bear_ration = 30
monthlyP = round(daily_penguin_ration * penguin * 30)
monthlyS = round(daily_seal_ration * seals * 30)
monthlyPO = round(daily_polar_bear_ration * polarBears * 30)
print(f"""The food consumed by penguins is {monthlyP} kg
The food consumed by seals is {monthlyS} kg
The food consumed by polar bears is {monthlyPO} kg""")
