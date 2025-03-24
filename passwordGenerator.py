import random
def generate_password(length):
    char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password=""
    for _ in range(length):
        password=password+random.choice(char);
    return password

length=int(input("Enter the length of the password : "))
password=generate_password(length)
print("Here is Your password:- ",password)