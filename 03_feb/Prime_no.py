# Prime number 
lower  = int(input("Enter the lower limit:"))
upper = int(input("Enter the upper limit:"))
res =[]
def Prime_no(lower, upper):
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
    
            
#call fuction 
Prime_no(lower, upper)




