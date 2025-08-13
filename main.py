import random
computer=random.choice([-1,0,1])
print(f"Compueter Choice:{computer}")
youStr=input("Enter your choice: ")
youDict={"r":-1,"p":0,"s":1}
you=youDict[youStr]
reverseStr={-1:"Rock",0:"Paper",1:"Scissor"}
print(f"Computer chose{reverseStr[computer]} and You chose {reverseStr[you]}")

if(computer==you):
    print("its a draw")
else:
    # differnce the below all(computer-you)
    if(computer==-1 and you==0):#-1
        print("You win")
    elif(computer==-1 and you==1):#-2
        print("you loose")
    elif(computer==0 and you==-1):#1
        print("You win")
    elif(computer==0 and you==1):#-1
        print("You win")
    elif(computer==1 and you==0):#1
        print("You loose")
    elif(computer==1 and you==-1):#2
        print("You win")
    else:
        print("Something went wrong")


"""
#shortcut for above conditional statements(else condition)
if((computer-you)==-2 or (computer-you)==1):
    print("You loose")
else:
    print("You win")
"""


