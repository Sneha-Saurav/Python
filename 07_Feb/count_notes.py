notes= (500,200,100,50,10)

amount  = int(input("Enter the amount: "))
def total_count(amount , notes):
    for note in notes:
        count =0
        if amount >= note:
            if note == 500:
                count = amount // note  
                amount  = amount % note 
            elif note == 200:
                count = amount // note
                amount  = amount % note 
            elif note == 100:
                count = amount // note 
                amount  = amount % note
            elif note == 50:
                count = amount // note
                amount  = amount % note  
            elif note == 10:
                count = amount // note
                amount  = amount % note 
            print("Total no of {} : is {}".format(note, count))
        else:
            print("Total no of {} : is {}".format(note, count))


total_count(amount,notes)








