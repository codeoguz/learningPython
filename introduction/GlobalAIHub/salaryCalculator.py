"""
Employees salary is being increased overtime.

< 1000 - 15%
< 2000 - 10%
< 3000 - 5%
> 3000 - 2.5%
"""
import time


salary = int(input('Enter your salary: '))
isInsurance = True if input('Is insurance included? (y, n)').capitalize == 'Y' else False

def salaryAnalyzer(salary):
    if(isInsurance):
        insurance = 800 + salary * .01
    else:
        insurance = 0
    
    newSalary = None
    if salary < 1000:
        newSalary = salary*1.15
    elif salary < 2000:
        newSalary = salary*1.10
    elif salary < 3000:
        newSalary = salary*1.05
    elif salary > 3000:
        newSalary = salary*1.025

    return {'newSalary': newSalary, 'insurance': insurance, 'total': newSalary + insurance}

for i in range(4):
    time.sleep(.8)
    b = 'Loading' + '.' * i
    print(b, end='\r')
    

result = salaryAnalyzer(salary)

print(
f'''
Thanks for using our service :)

Your info is below:
Salary: {result['newSalary']}
Insurance: {result['insurance']}

TOTAL: {result['total']}
''')