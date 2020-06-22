import sys

a= sys.argv[1]
b= sys.argv[2]
print("a is:", a)
print("b is:", b)
a= int (a)
b= int(b)

def adder(a, b):
    c=a+b
    return c

print(adder(a,b))