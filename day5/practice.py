# n=int(input('Enter the size of Array: '))
# nums=[]

# for i in range(n):
#     nums.append(int(input('Enter Array element: ')))
# # print(nums)

# nums=[79,77,34,81,48,34,25,16]
# ans = 0 
# for ele in nums:
#     i=1
#     while (i*i) <= ele:
#         if i*i == ele:
#             ans+=1
#             break
#         i+=1
# print(ans)
        

# def func(value,values):
#     var=1
#     values[0]=44

# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[0])
# options
# A. 1 44
# B. 3 1
# C. 3 44
# D. 1 3


# def f(i,values=[]):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)
# Options
# A. [1] [2] [3]
# B. [1, 2, 3]
# C. [1] [1, 2] [1, 2, 3]
# D. 1 2 3


# fruit={}
# def addone(index):
#     if index in fruit:
#         fruit[index]+=1
#     else:
#         fruit[index]=1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))
# print(fruit)
# Options
# A. 1
# B. 2
# C. 3
# D. 4


# Write a program to accept student name and marks from a keyboard
# and create a dictionary. Also display student markes by taking student name
# n=int(input('Enter the number of Students: '))
# std={}
# for i in range(n):
#     name=input('Enter Student Name: ')
#     mark=int(input('Enter Student Marks: '))
# while True:
#     name=input('Enter Student Name to get Marks: ')
#     mark=std.get(name,-1)
#     if mark == -1:
#         print('Student not found')
#     else:
#         print('The Marks of {} are {}',name,mark)
#     option=input('Do you want to find another student marks [Yes/No].')
#     if option == 'No':
#         break
# print('Thanks for using our application')


# Write a program to access each charactor to string in forward and 
# backward direction by using while loop?
input='Learning Python is very easy'
i=0
while i<len(input):
    print(input[i],end=' ')
    i+=1
print()
print('Backword')
j=len(input)-1
while j>=0:
    print(input[j],end=' ')
    j-=1
