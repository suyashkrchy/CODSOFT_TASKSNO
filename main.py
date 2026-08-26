import string
import random

if __name__ =="__main__":
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.digits
    s4=string.punctuation

    try:
        plen=int(input("Enter password length\n"))
        if plen<=0:
            print(f"Invalid length:{plen}.Length must be greater than 0")
        else:
            s=[]
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            #print(s)
            random.shuffle(s)
            # #print(s)
            password="".join(s[0:plen])
            print(f"Generated password is:{password}")
    except ValueError:
        #if user will enter "abc" or something like that in input i.e not integer value
        print(f"Gibberish detected! Please enter a valid number")
