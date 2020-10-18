

# init
a = int(input("Enter a two-digit number a> "))
b = int(input("Enter a two-digit number b> "))

# calc
a_first = a / 10
a_second = a % 10
b_first = b / 10
b_second = b % 10

# output
print("Result = %i%i" % (a_first + b_first, a_second + b_second))


