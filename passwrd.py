import random

Password = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*_-?"
pass_Len = int(input("Enter length of Password: "))

pwd= ""
for i in range(pass_Len):
    pwd+= ''.join(random.choice(Password))
    
print(pwd)