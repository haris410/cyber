#lab program no 5
# Write a Python program that creates a password strength meter. The program should
# prompt theuser to enter a password and check its strength based on criteria such as
# length, complexity, andrandomness. Afterwards, the program should provide
# suggestions for improving the password'sstrength.


import re
def cps(passwd):
    score=0
    sug=[]
    if len(passwd)>=8:
     score+=1
    else:
       sug.append("password should be atleast 8 characters long")

    if re.search(r"[A-Z]",passwd):
       score+=1
    else:
       sug.append("password should contain atleast one uppercas letter")

    if re.search(r"[a-z]",passwd):
       score+=1
    else:
       sug.append("password should contain atleast one lowercase letter")

    if re.search(r"\d",passwd):
       score+=1
    else:
       sug.append("password should contain atleast one numeric letter")

    if re.search(r'[!@#$%^&*()<>,.{}|?]',passwd):
       score+=1
    else:
       sug.append("password should contain atleast one special letter [!@#$%^&*()<>,.{}|?]")
    return score,sug

passwd=input("input a password:")
print(cps(passwd))



