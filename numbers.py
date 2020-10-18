# fun from StackOverflow :)
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

# init
a = int(input("Enter a> "))
b = int(input("Enter b> "))
c = int(input("Enter c> "))
d = int(input("Enter d> "))

# calc
f = toFixed((a+b) / (c+d), 2)

# output
print("(a + b) / (c + d) = ", f)


