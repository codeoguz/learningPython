# For loops and collections

employees = {'Kubilay': 'working', 'Oguz': 'playing', 'Omer': 'On Call', 'Emir': 'playing'}

print(employees)

for employee, status in employees.copy().items():
    if status == 'playing':
        del employees[employee]
        
print(employees)