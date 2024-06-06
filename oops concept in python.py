# class Person:
#     def __init__(self,name,character):
#         self.name=name
#         self.character=character
#     def info(self):
#         print(f"Hi my name is {self.name} and my favourite movie character is {self.character}")
# class Cricket(Person):
#     def __init__(self,name,character,role):
#         super().__init__(name,character)
#         self.role=role
#     def info(self):
#         print(f"Hi my name is {self.name}and my favourite movie character is {self.character}. I am {self.role}")
# v=Cricket("venkat","tony stark","batsmen")
# v1=Person("manish","itachi")
# v.info()
# v1.info()

# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def info(self):
#         print(f"Hi my name is {self.name} and he/she is {self.age}")
# class Dog(Animal):
#     def __init__(self,name,age,breed):
#         super().__init__(name,age)
#         self.breed=breed
#     def info(self):
#         print(f"Hi my name is {self.name} and is cute he is {self.age} old. His breed is {self.breed}")
# class Cat(Animal):
#     def __init__(self, name, age,colour):
#         super().__init__(name, age)
#         self.colour=colour
#     def info(self):
#         print(f"Hi my name is {self.name} and is cute he is {self.age} old. His colour is {self.colour}")
# v=Dog("Simba",5,"Lab")
# v1=Animal("Leo",2)
# v3=Cat("mike",6,"black")
# v.info()
# v1.info()
# v3.info()

# arr=input("Enter the list of numbers seperated by spaces: ").split()
# arr=[int(x) for x in arr]
# target=int(input("Enter the target to search: "))
# found=False
# for i in range(len(arr)):
#     if arr[i]==target:
#         print(f"Target {target} found at index {i}.")
#         found=True
#         break
# if not found:
#     print(f"target {target} not found in array.")

# class Person:
#     def __init__(self,name,character):
#         self.name=name
#         self.character=character
#     def info(self):
#         print(f"Hi my name is {self.name} and my favourite movie character is {self.character}")
# class Cricket(Person):
#     def __init__(self,name,role):
#         super().__init__(name,character=0)
#         self.role=role
#     def info(self):
#         print(f"Hi my name is {self.name}. I am {self.role}")
# v=Cricket("venkat","batsmen")
# v1=Person("manish","itachi")
# v.info()
# v1.info()

# def first_and_last_position(arr, k):
#     n = len(arr)
#     first = first_occ(arr, n, k)
#     last = last_occ(arr, n, k)
#     return (first, last)

# # Example usage
# arr = [1, 2, 2, 3, 3, 3, 4, 5, 5]
# k = 3
# result = first_and_last_position(arr, k)
# print(f"First and last position of {k}: {result}")

# program for authentication password.
# def authentication():
#     password="Sash123"
#     attempts=3

#     while attempts>0:
#         user_input=input("Enter the password:")

#         if user_input==password:
#             print("welcome!")
#             break
#         else:
#             attempts-=1
#             if attempts>0:
#                 print(f"wrong password! you have {attempts} attempts left.")
#             else:
#                 print("Account Blocked.")
#                 break
# authentication()

# authentication of password in oops
# class authentication():
#     def __init__(self,password,attempts):
#         self.password=password
#         self.attempts=attempts

#     def user_input(self):
#         while self.attempts>0:
#             user_input=input("Enter the password:")

#             if user_input==self.password:
#                 print("welcome!")
#                 break
#             else:
#                 self.attempts-=1
#                 if self.attempts>0:
#                     print(f"wrong password! you have {self.attempts} attempts left.")
#                 else:
#                     print("Account Blocked.")
#                     break

# authenticator=authentication(password="venkat",attempts=3)
# authenticator.user_input()
    
# Method ovverriding
# class Animal:
#     def speak(self):
#         return "Animal makes a sound"
    
# class Dog(Animal):
#     def speak(self):
#         return "Hoof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
    
# class Cow(Animal):
#     pass

# dog=Dog()
# cat=Cat()
# cow=Cow()

# print("Dog says:",dog.speak())
# print("Cat says:",cat.speak())
# print("Cow says:",cow.speak())



