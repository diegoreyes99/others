#Comments
print("Helllo World")

#Variable = A container for a value (string, integer, float, boolean)
# A variable behaves as if it was the value it containes

#Strings
first_name = "Bro"
food = "pizza"
email = "Bro123@fake.com"

print (f"Hello {first_name}") #Interpolation
print (f"You like {food}")

#Integers
age = 25
quantity = 3

print(f"You are {age} years old")
print(f"You are buying {quantity} items")

#Float
price = 10.99
gpa = 3.2

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")

# Boolean (true or false)
is_student = False
for_sale = True

print(f"Are you a student?: {is_student} ")

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if for_sale:
    print("That item is for sale")
else:
    print("That item is not available")

# Typecasting = the process of converting a variable from one data type to aonother
# str(), int(), float(), bool()

name = ""

print(type(first_name))
print(type(age))
print(type(gpa))

gpa = int(gpa) #3.2
print(gpa) #3

age = float(age)
print(age)

quantity = bool(quantity)
print(quantity)

name = bool(name)
print(name) # Imprime falso porque no es un string vacio 
