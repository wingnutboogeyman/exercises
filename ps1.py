print("Hello World!")

hello = "Hello"
name = input("What's your name?\n")
greeting = hello + " " + name
print(greeting)

age = int(input("How old are you?\n"))
# // = whole number division (integer division)
decades = age // 10
# % remainder after whole number division (modulus)
years = age % 10
print("You are " + str(decades) + " decades and " + str(years) + " years old.")