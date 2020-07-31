import random
import string 
def checkReq (formDict, key):
    if key in formDict:
        return True
    else:
        return False 
def get_password(length, number, capitalization, special):
    password= ""
    letters = string.ascii_lowercase
    numbers = string.digits
    punctuation = string.punctuation
    for x in range (0, int(length)):
    #add one random character each loop
        password += letters[random.randrange(0,len(letters))]
    passlist= list(password)
    #STRING METHODS
    if number:
        position=random.randrange(0,len(passlist))
        passlist[position]= numbers[random.randrange(0,len(numbers))]
#get random index (hint method) of the password and replace it (hint method) with a random number from 0-9
#random.randint(0,9)
    if capitalization:
        position=random.randrange(0,len(passlist))
        passlist[position]= (passlist[position]).upper()
#get random index and make that character capital (method)
    if special:
        position=random.randrange(0,len(passlist))
        passlist[position]= punctuation[random.randrange(0,len(punctuation))]
        password = " ".join(passlist)
        #(similar to the number) you will replace a random index with a special
    return password
