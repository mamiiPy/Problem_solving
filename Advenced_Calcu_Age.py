# Decoration
print("#"*60)
print(' Get Your Age Unite '.center(60, "#"))
print("#"*60)

# Get your Information
age = input("please! Type your age: ")
print('#'*30)
print(' The Time Unite '.center(30, '#'))
print('#'*30)
print('''1 - 'month' or 'm'
2 - 'week' or 'w'
3 - 'day' or 'd'
4 - 'hour' or 'h'
5 - 'minute' or 'm'
6 - 'second' or 's' ''')
print('#'*30)

unite = input('Please! Choose your time unite: ')

#  Get your time Unites
month = int(age) * 12
week = month * 4
days = int(age) * 365
hour = days * 60
minute = hour * 60
second = minute * 60

# Your Favorite Unites
if unite == 'month' or unite == 'm':
    print('you choose months unite ')
    print(f'your Age is {age} and you lived in months {month:,} months')
elif unite == 'week' or unite == 'w':
    print('you choose week unite ')
    print(f'your Age is {age} and you lived in week {week:,} weeks')
elif unite == 'day' or unite == 'd':
    print('you choose days unite ')
    print(f'your Age is {age} and you lived in week {days:,} weeks')
elif unite == 'hour' or unite == 'h':
    print('you choose hour unite ')
    print(f'your Age is {age} and you lived in hours {hour:,} hours')
elif unite == 'minute' or unite == 'min':
    print('you choose minute unite ')
    print(f'your Age is {age} and you lived in week {minute:,} minutes')
elif unite == 'second' or unite == 's':
    print('you choose second unite ')
    print(f'your Age is {age} and you lived in week {second:,} seconds')
else:
    print('Please! choose the write unite')
print('Thank You')
