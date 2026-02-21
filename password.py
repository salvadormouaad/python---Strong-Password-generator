import math
import random
def strongpassword():
    Email = input("The email:")
    For_what = input("For what plateform is this password: ")
    
    password = []
    Caps = ["A","B" , "C", "D", "E" ,"F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X" ,"Y", "Z"]
    Small = [ "a" ,"b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


    for i in range(4):
        password.extend([
            random.choice(Caps),
            random.choice(Small),
            random.choice(symbols),
            random.choice(numbers)
        ])   
    random.shuffle(password)
    password = "".join(password)

    file = open("/home/salvador/Desktop/Python/Password_Creator/Passwords.txt","a")
    file.write(f'{Email} ,  {password} ,  {For_what}\n')
    file.close()
    
    print("This is the perfect password u can use: ",password)
    print("For your",For_what, "With this email: ", Email)
    print("You are going to find everything saved the password file Have a great day <3")

strongpassword()