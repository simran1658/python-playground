# def exchange_list(number_list):
#     #start writing your code here
#     l=[]
#     for i in range(len(number_list)-1,len(number_list)//2-1,-1):
#         l.append(number_list[i])
#     for i in range(0,len(number_list)//2):
#         l.append(number_list[i])
#     return l



# A = [2,4, 5, 1, 4, 5, 3]  # Read input elements into the array A

# def equal(A):
#     for i in range(1, len(A)):
#         if A[i] != A[0]:
#             return False
#     return True

# i = 1
# flag = 0
# while i < len(A) and not equal(A):
#     if i > 0 and i < len(A) - 1 and A[i] >= A[i - 1] and A[i] >= A[i + 1]:
#         A[i] -= 1
#     else:
#         i += 1
#     if equal(A):
#         flag = 1
#         print("Yes")
#         break

# if flag == 0:
#     print("No")
    
    
# Read the number of test cases
# T = int(input())

# # Iterate over each test case
# for _ in range(T):
#     # Read the number of elements in the array
#     N = int(input())

#     # Read the array elements as a space-separated string
#     A = list(map(int, input().split()))

#     # Now A contains the array elements as integers
#     print("Number of elements in array:", N)
#     print("Array elements:", A)  # For testing, you can print the array

# T = int(input())
# for i in range(T):
#     N = int(input())
#     A = list(map(int, input().split()))
#     print("Number of elements in array:", N)
#     print("Array elements:", A)

#     def equal(A):
#         for i in range(1, len(A)):
#             if(len(A)==1):
#                 return True
#             if A[i] != A[0]:
#                 return False
#         return True

#     i = 1
#     flag = 0
#     if(len(A)==1):
#         print("YES")
#         flag=1
#     while (i <len(A) and not equal(A)):
#         if i > 0 and i < len(A) - 1 and A[i] >= A[i - 1] and A[i] >= A[i + 1]:
#             A[i] -= 1
#         else:
#             i += 1
#         if equal(A):
#             flag = 1
#             print("YES")
#             break

#     if flag == 0:
#         print("NO")

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     A = list(map(int, input().split()))

#     def equal(A):
#         if len(A) == 1:
#             return True
#         for i in range(1, len(A)):
#             if A[i] != A[0]:
#                 return False
#         return True

#     i = 1
#     flag = 0
#     while (i <= len(A) and not equal(A)):
#         if(len(A)==1):
#             flag=1
#             print("YES")
#             break
#         if i > 0 and i < len(A) - 1 and A[i] >= A[i - 1] and A[i] >= A[i + 1]:
#             A[i] -= 1
#         else:
#             i += 1
#         if equal(A):
#             flag = 1
#             print("YES")
#             break

#     if flag == 0:
#         print("NO")

# s="foo"
# t="bar"

# d1={}
# d2={}
# for i in s:
#     if i in d1:
#         d1[i]+=1
#     else:
#         d1[i]=1

# for i in t:
#     if i in d2:
#         d2[i]+=1
#     else:
#         d2[i]=1

# a=list(d1.values())
# b=list(d2.values())
# a.sort()
# b.sort()
# if(a==b):
#     print("True") 
# else:
#     print("False") 