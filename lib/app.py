# import random

# random_number = random.randint(0,10)



# guess_count=1
# guess_limit = 3

# while guess_count<=guess_limit:
#     guess=int(input("take a guess: "))
#     guess_count+=1
#     if guess == random_number:
#         print("you won")
#         break
    
# else:
#         print("max guess limit")

# game=""
# started=False 
# stopped=False

# while True:
#     game = input(" ").lower()
#     if game=="start" and started==True:
#         print("car is already started")
#     elif game=="start" and started==False:
#         print("car started")
#         started=True
#         stopped=False
#     elif game=="stop" and stopped==True:
#         print("car is already stopped")
#     elif game =="stop" and stopped==False:
#         print("car stopped")
#         started==False
#         stopped==True
#     elif game =="quit":
#         break
#     elif game == "help":
#         print("start - to start the car")
#         print("stop - to stop the car")
#         print("quit - to exit")
#     else:
#         print("sorry didn't understand")
    


# prices = [10, 20, 30]
# total = 0
# for item in prices:
#     total+=item
# print(f"Total:{total}")


# for x in range(4):
#     for y in range(3):
#         print(f'({x}, {y})')


# xxxxx
# xx
# xxxxx
# xx
# xx

# numbers = [5,2,5,2,2]
# for x in numbers:
#     print("x")
#     for x in numbers:
#         print("x")

# names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
# names[0]="Jon"
# print(names[0:3])


# numbers = [23,24,64,32,234,64,4343,5]
# max = numbers[0]
# for number in numbers:
#     if number> max:
#         max = number
# print(max)


# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [8,8,9]

# ]
# matrix[0][1]=20
# print(matrix[0][1])

# for array in matrix:

#     for number in array:
#         print(number)









# numbers = [5,2,1,7,4,5]
# modNumbers= []
# for number in numbers:
#     modNumbers.append(number)
#     if modNumbers.count(number)==2:
#         numbers.remove(number)
        
# print(numbers)

# customer = {
#     "name": "John Smith", 
#     "age": 30,
#     "is_verified": True
# }

# print(customer['name']
# )
# customer["name"]="Jack Smith"
# print (customer["name"])



# phone = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
#     "0": "zero"
# }

# number = input("Phone: ")
# length = len(number)
# i = 0
# while i < length:
#     print(phone[str(number[i])],end=" ")
#     i+=1


# phone = input("Phone: ")
# digits_mapping = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
#     "0": "zero"
# }
# output = ""
# for ch in phone:
#     output +=digits_mapping.get(ch, "!")+ " "
# print(output)

# message = input(">")
# words = message.split(' ')
# emojis = {
#     ":)": "😊",
#     ":(": "☹️"
# }
# output = ""
# for word in words:
#     word = emojis.get(word, word)
#     output +=word+" "
# print (output)


# def greet_user(first_name, last_name):
#     print(f"Hi there {first_name} {last_name}!")
#     print("welcome aboard")


# print("start")
# greet_user("john", "smith")
# print("finish")



# def square(number):
#     return number*number
# result = square(3)
# print(result)

# message = input(">")

# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "😊",
#         ":(": "☹️"
#     }
#     output = ""
#     for word in words:
#         word = emojis.get(word, word)
#         output +=word+" "

#     return output
    

# print(emoji_converter(message)
# )





# try:
        
#     age = int(input("Age:"))
#     income = 20000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print("age can't be zero")
# except ValueError:
#     print('Invalid value')


# class Point: 
#     def __init__(self, x,y):
#         self.x=x
#         self.y=y
        
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")




# point = Point(10,20)
# point.x=11
# print(point.x)

# class Person:
#     def __init__(self, name):
#         self.name=name
#     def talk(self):
#         print(f"Hello I'm {self.name}")


# jake = Person("jake")

# jake.talk()

# class Mammal:
#     def walk(self):
#         print("walk")


# class Dog(Mammal):
#     def bark(self):
#         print("bark")


# class Cat(Mammal):
#     def meow(self):
#         print("meow")


# dog1 = Dog()
# dog1.bark()
# from utils import find_max
# from converters import kg_to_lbs
# print(kg_to_lbs(70))
# array = [4,2,53,34,324,34]
# print(find_max(array))




























