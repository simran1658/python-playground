# i=0
#         result=[]
#         while(i<len(l)):
#             k=[]
#             for j in range(l[i],r[i]+1):
#                 k.append(nums[j])
#             k=sorted(k)
#             # print(k)
#             mini=k[1]-k[0]
#             flag=0
#             for x in range(len(k)-1):
#                 if(k[x+1]-k[x]!=mini):
#                     flag=1
#                     break
#             # print(flag)
#             if(flag==0):
#                 result.append("true")
#             else:
#                 result.append("false")
#             i+=1
        # print(result)
        # return result
        # str_result = [str(val) for val in result]  # Convert boolean values to strings
        # print(str_result)
        # return str_result
a={1:"A",2:"B",3:"C"}
print(a.setdefault(3))
