# Practise about Email Slicing
import email
from unicodedata import name


print('=====================================  Email_Slicing =============================')
Name = input('What \s is your Namme?: ')
Email = input('what\s is your email?: ')

user_name = Email[:Email.index('@')]
domaine = Email[Email.index('@') + 1:]

print(f'Your name is: {Name}.  \nyour email is: {Email}.')
print(f'Your user_Name is: {user_name} \nYour Domaine is {domaine}')
