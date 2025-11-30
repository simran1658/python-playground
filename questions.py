# import math
# a=int(input("enter the value of a"))
# b=int(input("enter the value of b"))
# c=int(input("enter the value of c"))
# x=((b*b)-4*a*c)
# d=math.sqrt(abs(x))
# if(x>0):
#     root1=(-b+d)//2*a
#     root2=(-b-d)//2*a
#     print("real and distinct are:")
#     print("root1:",root1)
#     print("root2:",root2)54
# elif(x==0):
#     root=(-b//2*a)
#     print("real and equal roots are",root)
# else:
#     print("root1",(-b//2*a),"+i",d)
#     print("root2",(-b//2*a),"-i",d)
#     print("real and complex roots")54


# def binaryToDecimal(num):
#     power=0
#     sum=0
#     while(num!=0):
#         n=num%10
#         if(n!=0 or n!=1):
#             print("invalid number")
#             break
#         sum=sum+n*pow(2,power)
#         num=num//10
#         power+=1
#     if(num==0):
#         return sum
# num=int(input("enter number"))
# s=str(num)
# flag=0
# print(s)
# for i in s:
#     if(i!="1" or i!="0"):
#         print("invalid number")
#         break
#     else:
# print("In Decimal",binaryToDecimal(num))
# print("In Decimal",binaryToDecimal(num))


# matrix1=[[1,2,3],[4,5,6],[7,8,9]]
# matrix2=[[1,1,3],[4,2,6],[1,8,1]] 
# result=[[0,0,0],[0,0,0],[0,0,0]]   
# for i in range(len(matrix1)):
# 	for j in range(len(matrix2)):
# 		result[i][j]=matrix1[i][j]+matrix2[i][j]
# for k in result:
# 	print (k)

# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]

# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]

# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]

# for i in range(len(X)):
#    for j in range(len(Y[0])):
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]

# for r in result:
#    print(r)

# for i in range(0,7):
#     if(i==3 or i==6):
#         continue
#     print(i,end=" ")

# for i in range(1,51):
#     if(i%3==0 and i%5==0):
#         print ("FizzBuzz")
#         continue
#     elif(i%5==0):
#         print("Buzz")
#         continue
#     elif(i%3==0):
#         print("Fizz")
#         continue
#     else:
#         print(i)

amount=int(input("Enter the amount"))
hundred=0
fifty=0
ten=0
while(amount>=10):
    hundred=amount//100
    amount=amount%100
    fifty=amount//50
    amount=amount%50
    ten=amount//10
    amount=amount%10
if(amount<10 and amount>0):
    print("invalid number")
else:
    print(f"Hundred: {hundred}\nFifty notes: {fifty}\nTen Notes: {ten}")
            
	
