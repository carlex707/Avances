two = 2
three = 3
is_equal = two = three
print(is_equal)

name = "Jhon"
age = 17
print(name == "Jhon" or age == 17)

print(name == "Jhon" and not (age==23))

name = "Jhon"
age = 17
print(name == "Jhon" or not age > 17)
print(name is "Ellis" or not (name is "Jhon" and age == 17))

x = 1 + 2 ** 3 / 4 * 5
print(x)