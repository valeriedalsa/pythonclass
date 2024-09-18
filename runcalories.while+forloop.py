CALORIES_PER_MINUTE = 4.2

print('Minutes\t\tCalories Burned')
print('-------------------------------')

for minutes in range(10, 31, 5):
    calories_burned = CALORIES_PER_MINUTE * minutes
    print   ( minutes, '\t\t', calories_burned)

print('Minutes\t\tCalories Burned')
print('-------------------------------')
minutes = 10
while minutes <= 30:
    calories_burned = CALORIES_PER_MINUTE * minutes
    print(minutes, '\t\t', calories_burned)
    minutes +=5

        
