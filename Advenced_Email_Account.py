# Advenced_email_slicing
print("#"*30)
print(' Email_Account '.center(30, '#'))
print("#"*30)

# Get Information
username = input('Whats\'s Your Name:\n').strip()
print('#'*30)
print(' Email Account '.center(30, '#'))
print('#'*30)
print('''1 - 'gmail' or 'G'
2 - 'outlook' or 'O'
3 - 'live' or 'L'
4 - 'Yahoo' or 'Y' ''')
print('#'*30)
E_mail = input('Choose your email\n').strip().upper()

# print(f'{username}{E_mail}')


# your email
gmail = '@gmail.com'
outlook = '@outlook.fr'
live = '@live.com'
yahoo = '@yahoo.fr'

# Favorite Email

# gmail Condition
if E_mail == 'gmail' or E_mail == 'G':
    E_mail = gmail[gmail.index('@') + 1: gmail.index('.')]
    print(f'hello! {username} you choose a {E_mail} account.')
    print(f'your New Email Account is :{username}{gmail} ')
# OutLook Condition
elif E_mail == 'outlook' or E_mail == 'O':
    E_mail = outlook[outlook.index('@') + 1: outlook.index('.')]
    print(f'hello! {username} you choose a {E_mail} account.')
    print(f'your New Email Account is :{username}{outlook} ')
# Live Condition
elif E_mail == 'live' or E_mail == 'L':
    E_mail = live[live.index('@') + 1: live.index('.')]
    print(f'hello! {username} you choose a {E_mail} account.')
    print(f'your New Email Account is :{username}{live} ')
# Yahoo Condition
elif E_mail == 'yahoo' or E_mail == 'Y':
    E_mail = yahoo[yahoo.index('@') + 1: yahoo.index('.')]
    print(f'hello! {username} you choose a {E_mail} account.')
    print(f'your New Email Account is :{username}{yahoo} ')
else:
    print('Sorry! you choose a wrong Account Name ?')
