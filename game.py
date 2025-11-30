import random
computer=random.randint(1,100)
repeat=1
i=0
while(i==0):
    choice=int(input("guess the number between 1 se 100 "))
    if(choice==computer):
        print("jeet gye badhai ho mithayi kb khila rhe")
        print("itni der m hattttt  ",repeat)
        i+=1
    elif(choice<computer):
        print(" thoda bada socho yrr")
        print("guess again")
        repeat+=1
    elif(choice>computer):
        print("thoda niche socho hawa m na udoo")
        print("guess again")
        repeat+=1
    else:
        print("get lost")


        