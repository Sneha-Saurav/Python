#fibonnaci number
#use of generator function 
#next function 



#generator 
def fibonacciGenerator(n):
    a=0
    b=1
    for i in range(n):
        yield a
        a,b= b,a+b

obj = fibonacciGenerator(10)
print("fibonacci Series is :")
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))


#lambda 
print("Lambda Function ")
add = lambda x,y:x+y
print("Sum is ",add(4,5))


