import secrets 
import string
import random

def password_generator(min_length,special_characters=True,numbers=True):
        letters=string.ascii_letters
        nums=string.digits
        special_symbols=string.punctuation
        pswd=random.choice(letters)
        plate=letters
        if numbers:
            plate+=nums
        if special_characters:
            plate+=special_symbols
        for i in range(min_length-1):
            pswd+=secrets.choice(plate)
        return pswd

if __name__=="__main__":
    key=input("Do you want to create our own password(Y/N): ")
    if key.lower()=="n": 
        my_pass=password_generator(10,special_characters=True,numbers=True)
        print(f"Password= {my_pass}")
    else:
        password=""
        jockey=input(f"Enter your Password: {password}")
        print(f"Your Password is: {jockey}")