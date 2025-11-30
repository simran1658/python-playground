# a=int(input("enter first number: "))
# b=int(input("enter second number: "))
# c=int(input("enter third number: "))
# if(a>b and a>c):
#     print("a is greater and its value is",a)
# if(b>c and b>a ):
#     print("b is greater and its value is",b)
# if(c>a and c>b):
#     print("a is greater and its value is",c)
# a=int(input("enter number"))
# x=10
# y=30
# z=20
# if(a==x):
#     print("x is equal to given number")
# elif(a==y):
#     print("y is equal to given number")
# elif(a==z):
#     print("z is equal to given number")
# else:
#     print("it is available")
# num=[1,2,3,4,5,6]
# square=0
# squares=[]
# for x in num:
#     square=x**2
#     squares.append(square)
# print(squares)




# print(range(0,10,2))
# print(type(range(0,10,)))
# lis=[1,2,3,4,5]
# print(tuple(lis))
# subject1=int(input("enter the 1 subject number"))
# subject2=int(input("enter the 2 subject number"))
# subject3=int(input("enter the 3 subject number"))
# subject4=int(input("enter the 4 subject number"))
# subject5=int(input("enter the 5 subject number"))
# sum=0
# for i in range(0,5):
#     a=int(input("enter marks "))
#     sum=sum+a
# percentage=(sum)/5
# msg=f'your percentage is {percentage}'
# print(msg)
# if(percentage>=90):
#     print("A++")
# elif(percentage>=85 and percentage<90):
#     print("A+")
# elif(percentage>=75 and percentage<85):
#     print("A")
# elif(percentage>=70 and percentage<75):
#     print("B++")
# elif(percentage>=65 and percentage<70):
#     print("B+")
# elif(percentage>=60 and percentage<65):
#     print("B")
# else:
#     print("fail")
# n=int(input("enter the no. of term in series"))
# x=int(input("enter the no. in series"))
# sum=0
# sum1=0
# for i in range(0,n):
#     sum=10*sum+x
#     print(sum,"+",end="")
#     # print("\n")
#     sum1=sum1+sum
# print("\n",sum1)

# a,b=-2,-89
# max=a if a>b else b
# print(max)


# a=['ab','cd']
# for i in a:
#     a.append(i.upper())
# print(x)
# mystr="hello123"
# print(mystr.isalnum())
# mystr="123456"
# print(mystr.isalnum())

# mystr="python is a programming"
# print(mystr.isalnum())

# str1="abcd"
# str2="xyz"
# for i in range(len(str1)):
#     for j in range(len(str2),0,-1):
#         str3=str1[i]+str[j]
# print(str3)

#join method
# sep=','
# names=['simran','shivani','shreya','shrishti','shalini']
# print(sep.join(names))

# mystr=[1,2,3,4]
# print(sep.join(mystr))
# it will show an type error as join mehod is only use in string not in int

#replace
# syntax:- str.replace(old,new,count())

# mystr='hello world!'
# print(mystr.replace('world','guys'))

# mystr='apples,mango,apples,grapes,banana,apples'
# print(mystr.replace('apples','cherry',2))

#split method
# syntax:-str.split()

# mystr='hello world!'
# print(mystr.split())

# print('heloo\nworld'.split())

# if we want to split by using particular symbol
# print('heloo,,world'.split(','))

# print('heloo@world'.split('@'))

# the split()method will raise the value error if a separator is an empty string

#splitlines()
# syntax:- str.splitlines(keepends)
# mystr=''' python is a 
# bakwaas'''
# print(mystr.splitlines())

#startswith()method
#syntax:- str.startswith(')

# str1=str(input("enter string:-"))
# str1='abcdef'
# n=len(str1)
# if(n%2==0):
#     print(str1[0]+str1[(n//2)-1]+str1[n//2]+str1[n-1])
# else:
#     print(str1[0]+str1[n//2]+str1[n-1])
# str1='abcdef'

# str1="gywde33138@#$%&^*&"
# c_alpha=0
# c_digit=0
# c_symbol=0
# for i in str1:
#     if(i.isalpha()):
#         c_alpha += 1
#     elif(i.isdigit()):
#         c_digit += 1
#     else:
#         c_symbol += 1
# print(str(c_alpha)+" "+str(c_digit)+" "+str(c_symbol))


# str1=input("enter numeric value only:-")
# sum=0 
# n=len(str1)
# for i in str1:
#     sum += int(i)
# print("sum:-",sum)
# print("average:-",sum//n)

# stri= int(input("enter kuch bhi:"))
# print(stri)

#LIST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# mylist=[1,"jeff","computer",75.60,True]
# print(type(mylist[3]))

# mylist=list({1:'one',2:'two'})
# print(type(mylist))

# cities=["mumbai","london","paris"]
# capitals={'new delhi':'india','washington':'jjj'}
# cities.extend(capitals)
# print(cities)

# cities=['kanpur','paris','london','allahabad']
# for i in cities:
#     print(cities.pop())



#exercise1
# list=[]
# size=int(input("enter the no. of element"))
# for i in range(size):
#     l=int(input("enter number"))
#     list.append(l)
# for i in list:
#     print(i**2,end=" ")
# list3=[]
# list1=["hello","take"]
# list2=["dear","sir"]

# for i in range(0,len(list1)):
#     for j in range(0,len(list2)):
#         x=(list1[i]+list2[j])
#         list3.append(x)

# print(list3)

# list1=["hello","take"]
# list2=["dear","sir"]
# for i in range(len(list1)):
#     print(list1[i],list2[i],end=" ")

# even=[]
# odd=[]
# number=[1,2,3,4,5,6]
# for i in number:
#     if(i%2==0):
#         even.append(i)
#     else:
#         odd.append(i)
# print("even:",even)
# print("odd:",odd)

#reverse a tuple

# a=(1,2,3,4,5)
# for i in range(len(a),0,-1):
#     print(tuple[i],end=" ")

# tuple1=("orange",[10,20,30],(5,15,25))
# print(tuple1[1][1])

# swap two tuples
# a=(1,2)
# b=(3,4)
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

# d1={'name':'harshit','age':'24'}
# d2={'name':'simran','age':'18'}
# d=dict({[3],[4,5,6]})
# list1=[1,2,3]
# list2=['simran','shivani','srishti']
# d={}
# for i in range(len(list1)):
#     d[list2[i]]=list1[i]
# print(d)

# d1={'name':'harshit','age':'24'}
# d2={'year':'2','section':'e'}
# for i in d2.keys():
#         d1[i]=d2[i]
# print(d1)
# for i,j in d2.items():
#     d1[i]=j
# print(d1)

# d1={}
# for i in range(2):
#     key=input("enter the key1")
#     value=input("enter the value")
#     d1[key]=value
# print(d1)
# d2={}
# for i in d1.keys():
#     values=input("enter the value")
#     d2[i]=values
# print(d2)

# //sets
# A set is a collection which is unordered, unchangeable*, and unindexed.

# s={1,2,3}
# s1=s.copy
# print(id(s))
# print(id(s1))

# adding an element in sets

# 1. add():- add element at random position
# sets={"a","f","s","j","g"}
# sets.add("e")
# print(sets)

# 2. update():-
# sets={3,4,5,7,8}
# s=[3,7,0]
# sets.update(s)
# print(sets)

# write a program to generate the sets of prime number
# s2=odd number
# 1.union 0000000000000000000000000
# intersection
# set1={1,2,3,5,7}
# set2={1,3,5,7,9}
# set3 = set1.union(set2)
# print(set3)
# set4=set1.intersection(set2)
# # set2.intersection_update(set1)
# print(set4)


file = open('hello.txt', 'w')
file.write("My name is Simran Singh")
file.close()
f=open("hello.txt","r")
print(f.read())
f.close()



































