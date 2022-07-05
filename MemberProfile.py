# Admin Member Profile

# Decoration
print('#'*30)
print(' Admin Member Profile '.center(30, '#'))
print('#'*30)

admins = ['khaled', 'mohammed', 'Brahim', 'iman', 'wafaa']

# Login Info
login = input('Please! Type Your name:\n').strip().lower()

# Login Condition
if login in admins:
    print(f'hello {login}, welcom back')

    # Decoration
    print('#'*30)
    print(' Admin Member Options '.center(30, '#'))
    print('#'*30)
    print('''1 - "Update" or "U"\n2 - "Delete" or "D"''')
    print('#'*30)

    option = input(
        f'Do You want {login} Update or Delete you name?\n').strip().capitalize()

    # Option Condition
    if option == 'Update' or option == 'U':
        new_name = input(
            f'Hi! {login} write your new name\n').strip().capitalize()
        admins[admins.index(login)] = new_name
        print('your name has been updated')
        print(admins)
    elif option == 'Delete' or option == 'D':
        admins.remove(login)
        print('your name has been deleted')
        print(admins)

# Add New Member_Profile
else:
    print(f'Sorry! {login} your are not admin\n')

    # Decoration
    print('#'*30)
    print(' Admin AddMember '.center(30, '#'))
    print('#'*30)
    print('''1 - "Yes" or "Y"\n2 - "No" or "N"''')
    print('#'*30)

    addMembers = input(
        f'Hi! Do you want  {login} to Become an admin ["yes","no"]\n').strip().capitalize()
    if addMembers == 'Yes' or addMembers == 'Y':
        admins.append(login)
        print(f'Hi! {login} you are now an admin')
        print(admins)
    elif addMembers == 'No' or addMembers == 'N':
        print('Thank you for visiting us')
