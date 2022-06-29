print('=='*20 + ' Calculate Your Ages ' + '=='*20)
Age = int(input('What\'s Your age? :'))
months = Age * 12
weeks = months * 4
days = Age * 365
hours = days * 60
minutes = hours * 60
second = minutes * 60
print(
    f'your Age is: {Age}.\nYour Age with months is : {months}.\nYour Age with weeks is : {weeks:,}.\nYour Age with days is : {days:,}.\nYour Age with hours is : {hours:,}.\nYour Age with minutes is : {minutes:,}.\nYour Age with second is : {second:,}\n')
