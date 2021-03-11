import string
from random import *

print('''
!@#$%^-----> PASSWORD GENERATOR <-----^%$#@!
''')

chars = string.ascii_letters + string.punctuation + string.digits

length = input('password length?')
length = int(length)

#Asking user for length of password
#Adding Warning if length is less than 8 char

if length < 8:
  strenght = input('Strong password requires 9 characters or more, continue anyways? yes/no ')
  if strenght == "no":
    length = input('password length?')
    length = int(length)

password = ""

#Generating Random password with desired length

for x in range(length):
  password += password.join(choice(chars))

print("Newly generated password :")
print(password)