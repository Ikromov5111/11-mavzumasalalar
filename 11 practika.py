# # 1 masala
# n = int(input("N = "))
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i,end=(" "))
#     i += 1

# #2-masala
# lis=[]
# k = True
# while(k):
#     n = int(input())
#     lis.append(n)
#     if n == 0:
#         k = False
# sum = 0
# for x in lis:
#     sum +=x
#
# print(sum)
# 3- maasala
# n = int(input("N= "))
# fact = 0;
# def factorial(n):
#     s=1
#     n = int(n)
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 1
#     else : s= s*n*factorial(n-1)
#
#     return s
#
#
# for x in range(1,n+1):
#     if x == n:
#         print(x,end = "=")
#         print(factorial(n))
#     else:
#         print(x, end = "*")


# #4-masala
# print(" a va b sonlarni kiriting ( 15 25 ) kabi : " ,end = " ")
# a,b = [int(item) for item in input().split(" ")]
# if a >= b :
#     print(a - b)
# elif b >= a :
#     print(b-a)

# # 5- masala yulduzcha
# n = int(input("N= "))
# a=""
# s = ""
# d = 1
#
#
# for x in range(0,n):
#     i = 0
#     j = 0
#     while j < n-d:
#         a+=' '
#         j+=1
#     s+='*'
#     while i < (x*2-1):
#         s+='*'
#         i+=1
#     d +=1
#     print(a,s)
#     s='*'
#     a=''
# s=''
# x = n-1
# d=n-1
# while x > 0:
#     i=0
#
#     j =0
#     while j < n-d:
#         a+=' '
#         j+=1
#     while i < 2*x-1 :
#         s+='*'
#         i+=1
#
#     d-=1
#     print(a,s)
#     a = ''
#     s = ''
#     x-=1


#6-masala

s='1234567890'
i =0
while i< 10:
    j=i
    a=0
    while j < 10:

        print(s[j],end=' ')
        a+=1


for x in s :
    print(x,end=" ")
