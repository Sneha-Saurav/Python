#greatest element : 02_feb
no1 = input("Enter the no:")
no2 = input("Enter the no:")
no3 = input("Enter the no:")
if no1 > no2 and no1 > no3:
    print(no1)
elif no2 > no1 and no2 > no3:
    print(no2)
else:
    print(no3)