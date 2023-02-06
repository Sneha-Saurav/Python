import cmath

a = int(input("Enter the first root:"))
b = int(input("Enter the second root:"))
c = int(input("Enter the third root:"))
# d = b*b -4ac
D = b**2 - 4*a*c
root1 = (-b- cmath.sqrt(D) )/(2*a)
root2 =(-b+ cmath.sqrt(D) )/(2*a)

print(root1)
print(root2)
