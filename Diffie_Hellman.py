from random import randint

p = int(input("p: "))
g = int(input("g: "))

a = int(input("a: "))
x = pow(g,a,p)

b=int(input("b: "))
y = pow(g,b,p)

ka = pow(y,a,p)
kb = pow(x,b,p)

print("Alice secret: ",ka)
print("Bob secret: ",kb)
