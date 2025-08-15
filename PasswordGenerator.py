import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

n= int (input ("Enter the length of password: "))


password = ""
for i in range (1,n+1):
    password += random.choice(characters)
    

print("\n Recomended Password: {password}".format(password=password))
print()
print()