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
# # 3- maasala
#
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
# for y in range(2,11):
#     print(y,"!= ",end=" ")
#     for x in range(1,y+1):
#         if x == y:
#             print(x,end = "=")
#             print(factorial(y))
#         else:
#             print(x, end = "*")
#     print()
#
# #4-masala
# print(" a va b sonlarni kiriting ( 15 25 ) kabi : " ,end = " ")
# a,b = [int(item) for item in input().split(" ")]
# if a >= b :
#     print(a - b)
# elif b >= a :
#     print(b-a)

# # # 5- masala yulduzcha
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


# #6-masala
#
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# i = 0
# k=0
# while i < 10:
#     for x in s :
#         print(x, end=" ")
#     s.append((s[k]))
#     s.remove(s[k])
#     # k=i+1
#     print()
#     i += 1




# #problem 6 ni 2 -si
# k = 0
# n = int(input(" N = "))
# i = 3
# while i <= n:
#     a = i
#     while a:
#
#         if a % 10 == 3:
#             k += 1
#         a = a // 10
#
#     i += 1
# print(k)


# # problem 7
# n = int(input(" N = "))
# k = 0
# d = 1
# s = [1,2,3,4,5,6,7,8,9,0]
# for x in range(0, n+1):
#
#     a = " "
#     i = 0
#
#     w = 0
#     while w < n+1//2 - d:
#         a += " "
#         w += 1
#     print(a, end=" ")
#     while i < x:
#
#         print(s[k % 10], end=" ")
#         k += 1
#         i += 1
#     print()
#     d += 1

# # 8 problem
# n = int(input("N= "))
# s = 0
# while n:
#     s += n % 10
#     n //= 10
#
# k = s % 10
# k += s // 10
#
# print(k)

#9.1
#
# # problem
# count = 0
# for x in range(1,7):
#     for y in range(1, 7):
#         for z in range(1, 7):
#             if (x + z + y ) == 10 :
#                 print(x, " ", y, " ", z)
#                 count +=1
#
# print("count = " , count)

# # 9.2 problem
# n = int(input(" N = "))
# sum = 0
# for x in range(0,n+1):
#     sum += x
#
# print(sum)
#


# # 10 problem
#
# x = [int(x) for x in input("LIST ELEMENTLARINI KIRITING(3 5 6 7 8) SHAKLDA ").split(" ")]
# sum = 0
# for y in x:
#     sum += y
# print(sum, " ", sum / len(x), len(x))