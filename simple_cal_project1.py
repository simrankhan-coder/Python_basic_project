def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error:Division by zero"
    return x/y
print("==Simple Calculator==")
print("Do operation Like:")
print("1.Add(+)")
print("2.Subtract(-)")
print("3.Multipy(*)")
print("4.Divide(/)")
op=input("Enter you choice(+,-,*,/):")
a=float(input("Enter first num:"))
b=float(input("Enter Second num:"))

if op=='+':
    result=add(a,b)
elif op=='-':
    result=subtract(a,b)
elif op=='*':
    result=multiply(a,b)
elif op=='/':
    result=divide(a,b)
elif op=='-':
    result="invalid operator"

print("Result:",result)