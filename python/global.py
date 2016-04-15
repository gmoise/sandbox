#the variable y is defined global and is used to exchange information in between global namespace and functions or objects
global y
y=0

def f (x):
    global y
    y=x
    z=0

f(2)
print("y=",y)

#print("z=",z)

def g(x):
    global y
    y=y+x

g(4)
print("y=",y)
