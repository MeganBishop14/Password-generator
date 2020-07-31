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
    if int(length)<3:
        length = 3
    for x in range (0, int(length)):
    #add one random character each loop
        password += letters[random.randrange(0,len(letters))]
    passlist= list(password)
    #STRING METHODS
    position_number=random.randrange(0,len(passlist))
    position_capitalization=random.randrange(0,len(passlist))
    position_special=random.randrange(0,len(passlist))
    if number:
        passlist[position_number]= numbers[random.randrange(0,len(numbers))]
#get random index (hint method) of the password and replace it (hint method) with a random number from 0-9
#random.randint(0,9)
    if capitalization:
        while position_capitalization == position_number:
            position_capitalization=random.randrange(0,len(passlist))
        passlist[position_capitalization]= (passlist[position_capitalization]).upper()
#get random index and make that character capital (method)
    if special:
        while position_capitalization == position_special or position_special == position_number:
            position_special=random.randrange(0,len(passlist))
        passlist[position_special]= punctuation[random.randrange(0,len(punctuation))]
        #(similar to the number) you will replace a random index with a special
    password = " ".join(passlist)
    return password