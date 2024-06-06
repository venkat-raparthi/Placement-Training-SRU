"""a= "sairockstar"
a_= 10.8
print(int(a_))
print(id(a))
print(type(a))
print(a[-5])"""

"""a=int(input('Enter the number: '))
print(a)
print(type(a))
"""
"""a=10
print(id(a))
a=10
print(id(a))"""

'''list=(1,2,"venkat")
list.append("cat")
list.remove("cat")
print(list)'''

"""s={100, 0, 10, 200, 10, 'durga'}
s.add(60)
s.remove(100)
print(s)"""
""""a=int(input())
b=int(input())
print(a/b)
print(a//b)
print(a*b)
print(a+b)
print(a-b)
print(a%b)"""

'''a=10
b=20
a=b
print(a)
print(b)
print(a==b)'''

'''a=10
b=9
a,b=b,a
print(a,b)'''


'''a=[1,4,1,4,3,2,5,7,5,7,3]
uni=0
for i in a:
    uni^=i
print(uni)'''

'''a=80
print('odd' if a&1 else 'even')'''

'''a=int(input())
if a==1 or a==2:
    print('prime')
elif a%2!=0:
    if a%3!=0 or a==3:
        if a%5!=0 or a==5:
            if a%7!=0 or a==7:
                print("prime")
            else:
                print("not prime")
        else:
            print("not prime")
    else:
        print("not prime")
else:
    print("not prime")'''

'''a=float(input("Enter the no:"))
print(round(a,2))'''
''''a,b,c=(map(int,input().split(" ")))
print(a,b,c)'''
'''a,b,c=list((input().split("#")))
print(type(n[0]))
print(n)'''

''''n=int(input())
total=0
for i in range(n+1):
    total+=i
print(total)'''

''''n=int(input())
total=1
for i in range(1,n+1):
    total=total*i
print(total)'''

''''n=int(input())
a,b= 0,1
for i in range(n):
    print(a, end=" ")
    a,b =b, a+b'''

''''n=int(input())
total=1
for i in range(1,11):
    total=n*i
    print(total)'''

# num=int(input())
# rev = 0
# while num>0:
#     digit=num%10
#     rev= rev*10+digit
#     num=num//10
# print(rev)

''''n=int(input())
count=0
while n !=0:
    n//= 10
    count+=1
print(count)'''

''''n=int(input())
if n==1:
    print("prime")
elif n%2!=0 or n==2:
    if n%3!=0 or n==3:
        if n%5!=0 or n==5:
            if n%7!=0 or n==7:
                print("prime")
            else:
                print("not prime")
        else:
            print("not prime")
    else:
        print("not prime")
else:
    print("not prime")'''


'''n=int(input())
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
    if count>=3:
        break
if count<3:
        print('prime')
else:
    print("composite")'''

'''n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum^i
    print(sum)'''
    
''' 1 -> 1
    2 -> n+1
    3 -> 0
    4 -> n
    for ex or operation the above answers will be for every 4 numbers'''

'''N= int(input())
if(N%4==1):
    print(1)
if(N%4==2):
    print(N+1)
if(N%4==3):
    print(0)
if(N%4==0):
    print(N)'''



'''n=int(input())
x=int(input())
a=0
b=0
for i in range(1,n+1):
    a=a^i
for i in range(1,x):
    b=b^i
c=a^b
print(c)'''




'''L=[1,2,3,4,5]
L.insert(1,100)
print(L)'''

'''L=[1,2,3]
L[0]=4
L1=L

print(L1)'''

'''L=[15,2,10,5,2,3,1.5]
print(L.count(10))
print(L.index(10))
L.sort()
print(L)
L.reverse()
print(L)
print(sum(L))
print(max(L))
print(min(L))
print(all(L))
print(any(L))
print(len(L))'''

'''L = [10,11,12,13,25,26]
print(L[1:])
print(L[1:6:2])'''

'''n1 = ['python', 'flask', 'django', 'tkinter']

n2 = n1

n3 = n1[:2]

print(n3)


n2[0] = 'scipy'

n3[1] = 'numpy'

s = 10
for i in (n1, n2, n3):
    if i[0] == 'python':
        s += 1
    if i[1] == 'python':   
        s += 2
print(s)     '''   

'''PASSWORD = "Venkat123"
username=input("Enter the user name: " )
def valid_pass():
    password = input("Enter the password: ")
    for i in range(2):    
        if password == PASSWORD:
            return "Welcome!"
        else:
            print(f"Only {2-i} attempts left.")
            password = input("Enter the correct password: ")
            if password == PASSWORD:
                return "Welcome!"
    return "3 Incorrect attempts. Account blocked."
print(valid_pass())'''

'''L = [x**2 for x in range(1,11) if x%2==0]
print(L)'''

''''L1= [1,2,3,6]
L2= [0,5,7]
L1.extend(L2)
L1.sort()
print(L1)
'''
'''L1= input().split()
L1.sort(key=len)
print(L1)'''

''''L1= input().split()
L1[0],L1[-1]=L1[-1],L1[0]
print(L1)'''

'''a=input().split()
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b) '''
'''a=input().split()
b=[]
for i in a:
    if a.count(i)%2!=0 and i not in b:
        b.append(i)
print(b) '''

'''L = list(map(int,input().split( )))
L.sort()
b=[]
for i in L:
     if i not in b:
          b.append(i)
print(sum(b[-3:]))'''



'''a=[1,2,3,4,5,6,7,8]
a.sort()
b=[]
c=[]
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])
for i in range(len(a)):
    if a[i]%2!=0 :
        c.append(a[i])
b=b[::-1]
b.extend(c)
print(b)'''

'''a=[1,2,3,4,5,6,7,8]
b=[]
a.sort()
for i in a:
    if i%2==0:
        b.insert(0,i)
    else:
        b.append(i)
print(b)'''

'''L = [1,2,3,4,5]
for i in range(1,4):
    L[i - 2 ] = L[i]
for i in range(0,4):
    print(L[i], end=" ")'''

'''n=int(input())
x=int(input())
sum=0
for i in range(n,x+1):
    sum=sum^i
    print(sum)'''

'''a=list(map(int,input().split( )))
b=[]
m,n=map(int,input().split( ))
for i in a:
    if i in range(m,n+1):
        b.append(i)
p=1
for i in b:
    p*=i
print(p)'''

# n = int(input())
# a= [map(int,input().split()) for i in range(n)]
# m=0
# for i in a:
#     s=sum(i)
#     if s>m:
#         m=s
#         ind=a.index(i)
# print(ind)

'''a=[1,2,3,4]
a=tuple(a)
print(a)
'''

'''t=tuple(input().split(' '))
l=len(t)
print(l)
i=int(input())
t=t[:i]+t[i+1:]
print(t)'''

'''t=tuple(map(int,input().split( )))
print(t[::-1])
'''
'''t=tuple(map(int,input().split( )))
dic={}
for i in t:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
num=int(input())
print(dic[num])'''

'''T=(1,2,3,3,4,5,6,5,8,4,2)
max_count=max(T.count(item) for item in T)
print(f"Maximum count: {max_count}")'''


'''list=[(),(),(1,2),(1,2,3)]
ist=[t for t in list if t]
print(list)
'''

'''s={1,4,2,5}
s.add(3)
print(s)
b=(6,5,7)
s.update(b)
print(s)
s1=s.copy()
print(s1)
s.remove(1)
print(s)
s.discard(10)
print(s)
print(s.pop())
print(s)'''

'''a={1,2,3}
b={3,4,5}
c={5,4,6}
a.intersection_update(b)
b.intersection_update(c)
print(a|b)
print(a.union(b))
print(a.intersection(b))
print(a&b)
print(a)
print(b)
print(c)
print(a.difference(b))
print(a-b)
a.difference_update(b)
print(a)
print(a.symmetric_difference(b))
print(a^b)
a.symmetric_difference_update(b)
print(a)
print(a.isdisjoint(b))
print(a.issuperset(b))
print(b.issubset(a))'''

'''s={0,1,2,3,4,5}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
print(all(s))
print(any(s))
print(sorted(s)) ''' "prints the set as a list with sorted"

'''L=[1,1,2,2,2,3,5,7,7,5]
L=set(L)
print(sorted(L))
'''
'''a={1,2,3}
b={1,2,3}
print(a>b)
'''
'''a=frozenset([1,2,3])
print(a)'''

'''res={s for s in [1,2,3,4,5] if s % 2==0}
print(res)'''

'''d={1:'hi','a':123,100:32.4}
print(d[1])
print(d['a'])
print(d[100])
print(d.get('a'))
for i in d:
    print(i,":",d[i])
d[1]=1000
print(d)
d[2]='python'
print(d)
del d[1]
print(d)
del(d)
print(d)'''

'''d={1:'hi','a':123,100:32.4}
print(d.get(100))
d.update({1:'jack',2:10})
print(d)
d1=d.copy()
print(d1)
d.pop('a')
print(d)
d.popitem()
print(d)
print(d.items())
print(d.keys())
print(d.values())
d.clear()
print(d)
'''
'''d={'a','b','c','d'}
d=dict.fromkeys(d,10)
print(d)'''
'''d1={1:'hi','a':123,100:32.4}
print(d1.setdefault('a'))
print(d1.setdefault('b'))
print(d1)
print(d1.setdefault('c',200))
print(d1)'''

'''d1={1:'hi','a':123,100:32.4}
print(d1.setdefault('b'))
d1['b']=150
print(d1)
'''
'''d1={1:'hi','a':123,100:{2:35,'a':143},32.4:'python'}
print(d1[100]['a'])'''

'''d1={1:'hi','a':123,100:{2:35,'a':143},32.4:'python'}
del d1[1:'a']
print(d1)'''

'''import operator
d={}
n=int(input("no of elements:"))
for i in range(n):
    k=input("enter key for first dist:")
    v=input("enter its value")
    d[k]=v
key=input()
value=input()
print(d)'''

'''import operator
d={}
n=int(input("no of elements:"))
for i in range(n):
    k=input("enter key for first dist:")
    v=input("enter its value")
    d[k]=v
key=input()
if key in d:
    print("key is present in the dictionary")
else:
    print("key is not present in the dictionary")'''

'''import operator
d={}
n=int(input("no of elements:"))
for i in range(n):
    k=i+1
    v=k*k
    d[k]=v
key=input()
value=input()
print(d)'''

'''n=int(input("input a number"))
d={}
for x in range(1,n+1):
    d[x]=x*x
print(d)'''

'''d={}
d1={}
n=int(input("no of elements:"))
for i in range(n):
    k=input("enter key for first dist:")
    v=input("enter its value")
    d[k]=v
for i in range(n):
    k=input("enter key for first dist:")
    v=input("enter its value")
    d1[k]=v
d2=d.copy()
d2.update(d1)
print(d2)
'''
'''d={}
n=int(input("no of elements:"))
for i in range(n):
    k=input("enter key for first dist:")
    v=input("enter its value")
    d[k]=v
k=input("key to delete:")
del d[k]
print(d)'''

'''d={}
n=int(input("no of elements:"))
for i in range(n):
    k=input("enter key for first dist:")
    v=input("enter its value")
    d[k]=v
key=input()
if key in d:
    del d[key]
print(d)'''

'''keys=input().split()
values=input().split()
d=dict(zip(keys,values))
print(d)'''

# l1=(input().split())
# l2=(input().split())
# d={}
# for i in range(0,3):
#     key=l1[i]
#     values=l2[i]
#     d[key]=values
# print(d)

# d1={'a':10,'b':20,'c':30}
# d2={'b':5,'c':15,'d':25}
# combined_dict={}
# for key in d1:
#     if key in d2:
#         combined_dict[key]=d1[key]+d2[key]
#     else:
#         combined_dict[key]=d1[key]
# for key in d2:
#     if key not in  combined_dict:
#          combined_dict[key]=d2[key]
# print(combined_dict)
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)

# print('venkat'.endswith('t'))
# print('venkat'.endswith('0'))
# print('venkat'.startswith('t'))
# print('venkat'.startswith('0'))
# print('hip')
# print('hip'.replace('i','o'))
# print('123'.isdigit())
# print('avs'.isalpha())
# print('123'.isdecimal())
# print('avs12@'.isalnum())
# print('Hello World'.istitle())
# print('venkat'.lower())
# print('venkat'.upper())
# print('vEnKaT'.swapcase())
# import string
# print(string.punctuation)

# str="shanks is my nickname"
# print(str.partition("is"))
# str2="""shanks 
# is
# my nickname"""
# print(str2.splitlines())
# ''str3="sasankan"
# print(str3.index("a"))
# print(str3.rindex("a"))''

# print('python programming'.capitalize)
# print('python cython'.find('th'))
# print('python cython'.rfind('th'))
# print('python cython'.count('th'))
# str='pythoncython'
# print(len(str))
# print(max(str))
# print(min(str))

# if letter in odd place conver into lower,even conver into upper
# a="kumar"
# b=""
# for i in range(0,len(a)):
#     if i%2==0:
#         b+=a[i].upper()
#     else:
#         b+=a[i].lower()
# print(b)

# remove the spaces in a string and move the space to front of the string and print the string
# a=input()
# spaces=""
# result=""
# for char in a:
#     if char==" ":
#         spaces+=char
#     else:
#         result+=char
# final_string=spaces+result
# print(final_string)

#remove consequent letters in a string 
# a=input(" ")
# result=a[0]
# for i in range(1,len(a)):
#     if a[i]!= result[-1]:
#         result+=a[i]
# print(result)

# print length of string without inbuilt function length
# a=input()
# print(len(a))
# def len1(str1):
#     count=0
#     for char in str1:
#         count+=1
#     return count
# str1=input()
# print(len1(str1))

# str=input()
# print("Your input in upper case ", str.upper())
# print("Your input in lower case ", str.lower())

# txt = "HELLO, And Welcome To My World!"
# x = txt.casefold()
# print(x)

# print wanted word in a string int0 upper/lower
# s1="my car is BmW"
# s2="BmW"
# s3=s1.replace(s2,s2.upper())
# print(s3)

# convert a string into upper and lower
# def swap(str1):
#     res=""
#     for i in str1:
#         if i.isupper():
#             res+=i.lower()
#         else:
#             res+=i.upper()
#     return res
# str1=input()
# print(swap(str1))

# a=input(" ")
# b=input(" ")
# result=a[0]
# for i in range(0,len(a)):
#     if a[i]!= b:
#         result+=a[i]
# print(result)

# print elements which are not repeated
# a=input()
# b=input()
# c=a+b
# for i in c:
#     if c.count(i)==1
#         print(i,end="")

# s1=input()
# s2=input()
# uncommon_char="".join(set(s1) ^ set(s2))
# print(uncommon_char)

# s=input()
# max_char=max(s,key=s.count)
# print(f"max occuring char: {max_char}")

# print elements which are not repeated
# v=input()
# b=input()
# k=v+b
# for i in k:
#     if k.count(i)==1:
#        print(i,end="")

# def fun():
#     print("Welcome")
# fun()

# sum of 2 numbers using def function
# def sum(num1:int,num2: int):3

#     num3=num1+num2
#     return num3
# num1,num2 = 5,2
# ans=sum(num1,num2)
# print(ans)
# print(f"the addition of {num1} and {num2}= {ans}")

# def prime(num1):
#     if num1%2==0 and num1%num1==0:
#             print("not prime")
#     else:
#             print("prime")
#     x=num1
#     return x     
# num2=int(input())
# prime(num2)
# print()

# def check_prime():
#     num=int(input())
#     if num>1:
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")
#     else:
#          print("prime")
# check_prime()

# def diff(num1:int,num2:int): 
#     num3=num1-num2
#     return num3
# # num1=int(input())
# # num2=int(input())
# ans=diff(num2=5,num1=10)
# print(ans)

# def student(firstname,lastname):
#     print(firstname,lastname)
# student(firstname='geeks',lastname='practice')
# student(lastname='practice',firstname='geeks')

# positional arguments
# def nameAge(name,age):
#     print("hi, i am",name)
#     print("my age is",age)
# print("case-1:")
# nameAge("suraj",18)
# print("case-2:")
# nameAge(26,"suraj")

#     '''* means unpacking : unpacks the list and adds the elements in list'''
# def my_sum(*args):  
#     result=0
#     for x in args:
#         result+=x
#     return result
# print(my_sum(1,2,3))

# # ** means unpacking operator used for adding the words
# def concatenate(**words):
#     result=""
#     for arg in words.values():
#         result+=arg
#     return result
# print(concatenate(a='real',b='python'))

# factorial of a number using reccursive_factorial function

# printing factorial of n number using reccursive function
# def reccursive_factorial(n):
#     if n==1:
#         return n
#     else:
#         return n*reccursive_factorial(n-1)
# num=(int(input()))
# if num<0:
#     print("invalid.")
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     print("Factorial of number",num,"=",reccursive_factorial(num))

# printing sum of n natural numbers using reccursive function
# def reccursive_sum(n):
#     if n==1:
#         return n
#     else:
#         return n+reccursive_sum(n-1)
# num=int(input())
# if num<0:
#     print("invalid.")
# elif num==0:
#     print("sum of 0 is 0")
# else:
#     print("sum  of first" ,num,"number",num,"=",reccursive_sum(num))

# print fibonnaci value of a number
# n=int(input())
# a=0
# b=1
# for i in range (0,n):
#     c=a+b
#     a=b
#     b=c
# print(c)

# printing numbers before n in reverse order
# def fun(n):
#     if(n>0):
#         print(n)
#         fun(n-1)
# n=int(input())
# fun(n)

# printing numbers before n in correct order
# def fun(n):
#     if(n>0):
#         fun(n-1)
#         print(n)     
# n=int(input())
# fun(n)

# print fibonacci of a number
# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
    
# num_terms=int(input("enter the no of terms:"))
# for i in range(num_terms):
#     print(f"fibonacci({i})={fibonacci(i)}")

# in oops 
# attribute=variables
# methods=functions

# oops in python
# class Person:
    # def __init__(venkat,name): 'constructor'
#         venkat.name=name      
#     def say_hi(venkat):       'method' 
#         print('hello,my name is',venkat.name)
# p=Person("subhan")   'object'
# p.say_hi()     'accessing method using object

# class Person:
#     def __init__(venkat,name,age): #'constructor'
#         venkat.name=name
#         venkat.age=age     
    
#     def say_hi(venkat):       #'method' 
#         print('hello,my name is',venkat.name)
#         print('my age is',venkat.age)
# p=Person("subhan", 30)   #'object'
# p.say_hi()    # 'accessing method using object'

# 4 pillars of oops
# 1.inheiritance
# 2.data encapsulation
# 3.data abstraction
# 4.polymorphism

# class Test:
#     def __init__(self):
#         self.x=0
# class Derived_Test(Test):
#     def __init__(self):
#         Test.__init__(self)
#         self.y=1
# def main():
#     b= Derived_Test()
#     print(b.x,b.y)
# main()

# class Animals:
#     def __init__(self,name,species,sound):
#         self.name=name
#         self.species=species
#         self.sound=sound
#     def make_sound(self):
#         print(f"The {self.species} named {self.name} sounds {self.sound} ")
# class Lion(Animals):
#     def get_info(self):
#         print("lions are the kings of the jungle")
# class Elephant(Animals):
#     def get_info(self):
#         print("Elephants are the largest land animals")
# class Snake(Animals):
#     def get_info(self):
#         print("Snakes can be found on every continent except antartica")

# obj=Animals('lion', 'leo', 'roar')
# obj.make_sound()
# li=Lion(Animals)
# li.get_info(self)

# class Animals:
#     def __init__(self,name,species,sound):
#         self.name=name
#         self.species=species
#         self.sound=sound
#     def make_sound(self):
#         print(f"The {self.species} named {self.name} sounds '{self.sound}' ")
# class Lion(Animals):
#     def __init__(self,name):
#         super().__init__(name, "Lion","roar")
#     def get_info(self):
#         print("lions are the kings of the jungle")
# class Elephant(Animals):
#     def __init__(self,name):
#         super().__init__(name, "Elephant","Trumpet")
#     def get_info(self):
#         print("Elephants are the largest land animals")
# class Snake(Animals):
#     def __init__(self,name):
#         super().__init__(name, "Snake","Hiss")
#     def get_info(self):
#         print("Snakes can be found on every continent except antartica")

# leo = Lion("Leo")
# ellie = Elephant("Ellie")
# slyther = Snake("Slyther")

# leo.make_sound()
# leo.get_info()
# print()

# ellie.make_sound()
# ellie.get_info()
# print()

# slyther.make_sound()
# slyther.get_info()
# print()

# giving input till negative number is given and break the loop
# while True :
#     x=int(input())
#     if x<0:
#         break
#     else:
#         False




































































