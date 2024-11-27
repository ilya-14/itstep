'''try:
    print("start code")
    print(10/0)
    print("No errors")
except NameError:
    print("We have an NameError")
except ZeroDivisionError:
    print("We have an ZeroDivisionError")

print("code after capsule")'''

'''try:
    print("start code")
    print(10/0)
    print("No errors")
except (NameError,ZeroDivisionError) as error:
    print("We have an ", error )

print("code after capsule")'''

'''try:
    print("Hello")
    print(error)
    print("No error")
except NameError as error:
    print(error)
else:
    print("No problems")
finally:
    print("Finally code")'''

text1 = "hello world"
print(text1*5)
