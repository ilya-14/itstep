#1
name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))
print(f"Привіт {name}, тобі {age}!")

#2
age = int(input("Введіть ваш вік: "))
if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")

#3
import random

number = random.randint(1, 10)
attempts = 3

while attempts > 0:
    guess = int(input("Вгадай число від 1 до 10: "))

    if guess < number:
        print("Більше")
    elif guess > number:
        print("Менше")
    else:
        print("Правильно! Ви вгадали число.")
        break

    attempts -= 1

if attempts == 0:
    print(f"Ви не вгадали. Загадане число було {number}.")

#4
start = int(input("Введіть число з: "))
end = int(input("Введіть число по: "))

for i in range(start, end + 1):
    print(i, end=" ")

#5
n = int(input("Введіть число n: "))

for i in range(n, 0, -1):
    if i % 2 == 0:
        print(i, end=" ")

#6
score = int(input("Введіть кількість балів: "))

if 0 <= score <= 49:
    print("Незадовільно")
elif 50 <= score <= 69:
    print("Задовільно")
elif 70 <= score <= 89:
    print("Добре")
elif 90 <= score <= 100:
    print("Відмінно")
else:
    print("Некоректна кількість балів")

#7
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть математичну операцію (+, -, *, /): ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b == 0:
        result = "Ділення на нуль!"
    else:
        result = a / b
else:
    result = "Невідома операція!"

print(f"Результат: {result}")
