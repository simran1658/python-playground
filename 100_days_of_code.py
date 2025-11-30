import random
# print("Day 1 - Python Print Function\nThe function is declared like this:")
# print("\'what to print\'")
# a = input()
# b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
# a=a+b
# b=a-b
# a=a-b
# print(a,b)

# two_digit_number = input()
# sum=0
# for i in two_digit_number:
#   sum+=int(i)
# print(sum)

# height = input()
# 2nd input: enter weight in kilograms e.g: 72
# weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# height=float(height)
# weight=float(weight)
# bmi=(weight/(height**2))
# print(int(bmi))

#Project1
# age = input()
# age=int(age)
# x=(90-age)*52
# print(f"You have {x} weeks left")
# print("Welcome to the band name generator")
# name=input("which city did you grow up")
# pet=input("what\'s your pet name?")
# print(f"Your brand name could be {name} {pet}")

#Project2
# bill=float(input("What was the total bill?$ "))
# percentage=float(input("What percentage tip would you like to give? 10, 12, or 15? "))
# people=float(input("How many people people to split the bill? "))
# tip=(percentage/100)*bill+bill
# final_bill="{:.2f}".format(tip/5)
# print("Each person should pay: $ ",final_bill)

#project3

# choice=input("Enter choice: left or right: ")
# if(choice=="right"):
#     print("Game over You lost!")
# elif(choice=="left"):
#     c=input("Swim or Wait: ")
#     if(c=="swim"):
#         print("Game over You lost!")
#     elif(c=="wait"):
#         door=input("Which door? Red? Yellow? Blue?")
#         if(door=="red"):
#             print("Game over You lost!")
#         elif(door=="blue"):
#             print("Game over You lost!")
#         elif(door=="yellow"):
#             print("You Win!")
# else:
#     print("Invalid choice")

#project4

# print("Welcome to Rock Paper Scissor Game!!!!!!!!!!....")
# print("1 for Rock\n2 for Paper\n3 for Scissor")
# computer=random.randint(1,3)
# c=1
# while(c!=0):
#     choice=int(input("enter your choice: "))
#     if(computer==1 and choice==2):
#         print("You win!")
#         break
#     elif(computer==2 and choice==3):
#         print("You win!")
#         break
#     elif(computer==3 and choice==1):
#         print("You win!")
#         break
#     elif(computer== choice):
#         print("Match Draw")
#     else:
#         print("You lose!!!")
#     print("Do you want to take a new chance to win?\nPress 1 for Yes\nPress 0 for No")
#     c=int(input("enter here: "))
# print("Thank you for visiting!!!!!!!!!!!")

#project5

# letters=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m","Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
# NUMBERS=[1,2,3,4,5,6,7,8,9,0]
# symbols=["!","@","#","$","%","&","*","(",")","+"]
# letter=int(input("Enter the no. of letters want to be in password"))
# symbol=int(input("enter the no. of symbols want to be in password "))
# number=int(input("enter the no. of numbers want to be in password "))
# password=[]
# for i in range(letter):
#     password.append(random.choice(letters))
# for i in range(symbol):
#     password.append(random.choice(symbols))
# for i in range(number):
#     password.append(random.choice(NUMBERS))
# print(password)
# hacker=""
# random.shuffle(password)
# print("".join(r))
# for i in password:
#     hacker+=str(i)
# print(hacker)

# Project6
# word_list=["ardvark","baboon","camel"]
# chosen_word=random.choice(word_list)
# guess=input("Guess a letter")
# guess=guess.lower()
# print("choosen word is ",chosen_word)
# for letter in chosen_word:
#     if(letter==guess):
#         print("you guess it right")
#     else:
#         print("you lose!!")
#         pass

# project7
# display=[]
# for i in chosen_word:
    # display.append("_")
# print(display)
# for i in range(len(chosen_word)):
#     if(chosen_word[i]==guess):
#         display.remove(display[i])
#         display.insert(i,chosen_word[i])
# print(display)

# project8
# while("_" in display):
#     guess=input("Guess a letter")
#     guess=guess.lower()
#     for i in range(len(chosen_word)):
#         if(chosen_word[i]==guess):
#             display[i]=chosen_word[i]
    # print(display)
# print("you won!!!!")

#project9
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# lives = 6
# print(f'Pssst, the solution is {chosen_word}.')
# display = []
# for _ in range(word_length):
#     display += "_"
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#     for position in range(word_length):
#         letter = chosen_word[position]
#         if letter == guess:
#             display[position] = letter

#     if guess not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     print(f"{' '.join(display)}")
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#     print(stages[lives])

# def greet():
#     print("hello")
#     print("my name is simran singh")
#     print("cool!!!!!!!")
# greet()

# def greet(name,location):
#     print(f"hello {name}")
#     print(f"What is like in {location}")
# greet("Simran","kanpur")


# day 8
# alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# print(" enter \'encode\' for encoding or enter \'decode\' for decoding ")
# user=input("Enter your choice: ")
# message=input("Type the message: ").lower()
# shift=int(input("enter no. of shifts: "))
# if(shift>26):
#     new_shift=shift%26
# s=""
# def encrypyt(text,shift_amount):
#     global s
#     for letter in text:
#         position=alphabet.index(letter)+new_shift
#         if(position>=26):
#             new_position=(position-26)
#             s+=alphabet[new_position]
#         else:
#              s+=alphabet[position]
#     print(s)


# decode_msg=""
# def decrypt(s,shift):
#     global decode_msg
#     for letter in s:
#         position=alphabet.index(letter)-new_shift
#         if(position<0):
#             new_position=(26-abs(position))
#             decode_msg+=alphabet[new_position]
#         else:
#             decode_msg+=alphabet[position]
        
#     print(decode_msg)


# if(user=='encode'):
#     encrypyt(message,shift)
# elif(user=="decode"):
#     decrypt(message,shift)
# else:
#     print("please follow the given instruction given above!!!!")

# day 9

# d={}
# choice=True
# while(choice):
#     name=input("Enter your name: ")
#     bid=int(input("Enter the bid: $"))
#     d[name]=bid
#     user=input("Are there any other bidders? Type \"yes\" or \"no\": ")
#     if(user=="yes"):
#         continue
#     else:
#         choice=False
# print(d)
# max=0
# for i in d:
#     if(d[i]>max):
#         max=d[i]
#         naam=i
# print(f"The winner is {naam} with a bid of ${max}")

# day 10

# def add(a,b):
#     return a+b

# def subtract(a,b):
#     return a-b

# def multiply(a,b):
#     return a*b

# def divide(a,b):
#     return a/b

# def check(input1,input2,operator):
#     global output
#     if(operator=="+"): 
#         output=add(input1,input2)
#         print(f"{input1}{operator}{input2}= ",output)
#     elif(operator=="-"):
#         output=subtract(input1,input2)
#         print(f"{input1}{operator}{input2}= ",output)
#     elif(operator=="*"):
#         output=multiply(input1,input2)
#         print(f"{input1}{operator}{input2}= ",output)
#     elif(operator=="/"):
#         output=divide(input1,input2)
#         print(f"{input1}{operator}{input2}= ",output)
#     else:
#         print("invalid input or operator")

# output=0
# input1=int(input("enter one number "))
# input2=int(input("enter second number "))
# operator=input("enter the operation u want to perform ")
# check(input1,input2,operator)
# choice=True
# while(choice):
#     user=input("if u want to do more operations:  type yes for more otherwise no: ")
#     if(user=="yes"):
#         operation=int(input("enter the value: "))
#         oper=input("enter the operator: ")
#         check(output,operation,oper)
#     elif(user=="no"):
#         print("thank u for visiting!!!   ")
#         choice=False
#     else:
#         print("Invalid statement ")
        
        
# day 12
# count_easy=10
# count_hard=5
# print("WELCOME TO NUMBER GUESSING GAME")
# print("I am thinking of guessing a number between 1 to 100")
# print("choose a dificulty level : \n Type : easy \n Type : hard")
# num=random.randint(1,100)
# level=input("enter your level ")
# if(level=="easy"):
#     flag=False
#     while(count_easy!=0):
#         user=int(input("Make a guess: "))
#         if(user>num):
#             print("Too high")
#             print("guess again")
#             count_easy-=1
#             print(f"You have {count_easy} attempt remaining to guess a number")
#         elif(user<num):
#             print("Too low")
#             print("guess again")
#             count_easy-=1
#             print(f"You have {count_easy} attempt remaining to guess a number")
#         else:
#             print("You got it !!! The answer is "+str(user))
#             flag=True
#             break
#     if(flag==False):
#         print("You lost")
# elif(level=="hard"):
#     flag=False
#     while(count_hard!=0):
#         user=int(input("Make a guess: "))
#         if(user>num):
#             print("Too high")
#             print("guess again")
#             count_hard-=1
#             print(f"You have {count_hard} attempt remaining to guess a number")
#         elif(user<num):
#             print("Too low")
#             print("guess again")
#             count_hard-=1
#             print(f"You have {count_hard} attempt remaining to guess a number")
#         else:
#             print("You got it !!! The answer is "+ str(user))
#             flag=True
#             break
#     if(flag==False):
#         print("You lost")
# else:
#     print("enter valid level")

#day15 coffee machine

water=500
milk=500
coffee=100
bank_amount=0
def report():
    print("Water: "+str(water))
    print("Milk: "+str(milk))
    print("Coffee: "+str(coffee))
    print("Money: "+str(bank_amount))
    
def espresso_req():
    if(water<50):
        print("Sorry, there is not enough water ")
    elif(coffee<18):
        print("Sorry, there is not enough coffee")
    else:
        return True

def latte_req():
    if(water<200):
        print("Sorry, there is not enough water ")
    elif(coffee<24):
        print("Sorry, there is not enough coffee")
    elif(milk<150):
        print("Sorry, there is not enough milk")
    else:
        return True
    
def cappuccino_req():
    if(water<250):
        print("Sorry, there is not enough water ")
    elif(coffee<24):
        print("Sorry, there is not enough coffee")
    elif(milk<100):
        print("Sorry, there is not enough milk")
    else:
        return True
    

def coins():
    print("Please insert coins")
    global quarter
    quarter=int(input("How many Quarters?: "))
    global dimes 
    dimes=int(input("How many dimes?: "))
    global nickles
    nickles=int(input("How many dimes?: "))
    global pennies
    pennies=int(input("How many pennies?: "))

user=True
while(user==True):
    choice=input("What would you like? (espresso/latte/cappuccino)").lower()
    if(choice=="espresso"):
        if(espresso_req()==True):
            coins()
            amount=0.25*quarter+0.1*dimes+0.05*nickles+0.01*pennies
            if(amount>=1.50):
                bank_amount+=1.50
                water-=50
                coffee-=18
                print("Here is your espresso Enjoy!!")
            else:
                print("Sorry that's not the enough money.  Money Refunded. ")
            
    elif(choice=="latte"):
        if(latte_req()==True):
            coins()
            amount=0.25*quarter+0.1*dimes+0.05*nickles+0.01*pennies
            if(amount>=2.50):
                bank_amount+=2.50
                water-=200
                coffee-=24
                milk-=150
                print("Here is your latte Enjoy!!")
            else:
                print("Sorry that's not the enough money.  Money Refunded. ")
            
    elif(choice=="cappuccino"):
        if(cappuccino_req()==True):
            coins()
            amount=0.25*quarter+0.1*dimes+0.05*nickles+0.01*pennies
            if(amount>=3.00):
                bank_amount+=3.00
                water-=250
                coffee-=24
                milk-=100
                print("Here is your cappuccino Enjoy!!")
            else:
                print("Sorry that's not the enough money.  Money Refunded. ")
    elif(choice=="report"):
        report()
    elif(choice=="off"):
        user=False
        break
    else:    
        print("Sorry it is not avilable. enter a valid drink!!!")
        
    
    