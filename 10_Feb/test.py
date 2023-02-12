number=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
nty=["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninty"]
tens=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]

amount = int(input('Enter the amount: '))

def format_amount(amount):
    """
    This function is used to format the amount
    ex :25
    Rs: 25.00
    :param amount
    :return
    """
    return f"{amount}.00"

def convert_to_words(func):
    def inner(amt):  
        for_amount = func(amt)  # function uses another function 
        n = int(float(for_amount))
        print(n)
        print(type(n))
        if n>99999:   
             print("Cant solve for more than 5 digits")
        else:   
            d=[0,0,0,0,0]                   # input the amount digit in a list 
            i=0
            while n>0:
                d[i]=n%10
                i+=1
                n=n//10                         # input the number in list d []
            num=""
            if d[4]!=0:                      # ex : 3456 d =[6,5,4,3]
                if(d[4]==1):                 #  # Last element of list
                    num+=tens[d[3]]+ " Thousand "    # third element of list
                else:
                    num+=nty[d[4]]+" "+number[d[3]]+  " Thousand "    #combining the last and third words of list 
            else:
                if d[3]!=0:
                    num+=number[d[3]]+ " Thousand " # if last element is zero
            if d[2]!=0:
                num+=number[d[2]]+" Hundred "
            if d[1] != 0:                          # for first 2 digits for d list
                if (d[1] == 1):
                    num += tens[d[0]]
                else:
                    num += nty[d[1]] + " " + number[d[0]]
            else:
                if d[0] != 0:
                    num += number[d[0]]
        
        return num   
    return inner
            
div = convert_to_words(format_amount)
print(div(amount))

