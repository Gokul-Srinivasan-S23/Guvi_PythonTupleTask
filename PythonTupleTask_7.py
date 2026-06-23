list1=[1,2,3,1,2,3,4,5,6,7,5,6,7]#Initializing the list
for num in list1:#looping the list
    counter = 0 #initializing the variable to zero
    for num1 in list1: #looping the list inside a loop
        if num == num1: #Validating the repeated numbers
            counter+=1 #added to the counter the number of times it repeated
    if counter == 1: #if repeated count is one then it has occured only once in the list
        print("The first non-repeating number in the list",num) #printing the statement
        break #if first non-repeating is found then stopping the loop