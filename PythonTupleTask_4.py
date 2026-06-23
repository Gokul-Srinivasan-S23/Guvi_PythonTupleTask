num=input("Enter an Interger greater than 9  ") #getting the value from use
if num.isdigit():
    if int(num) >= 9: #validating the input has two digits
       res = int(num[0]) + int(num[-1]) # adding the first and last digit of the input
       print ("The Sum of the first and last digit of the interger is ",res)
    else:
        print ("Enter value is less than 9 , Please enter an interger more than one digits") #displaying the error message
else:
    print ("Enter value is incorrect , Please enter an integer") #displayign the error message