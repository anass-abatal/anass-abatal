number_1=int(input("Enter the first number: "))
number_2=int(input("Enter the segund number: "))
if number_1>number_2 :
    low= number_2
    top= number_1
else:
    low=number_1
    top=number_2
    for i in range (low,top +1):
        if i%2==0:
            print("the number is", i)




