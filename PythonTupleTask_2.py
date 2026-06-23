org_list = [10 , 501 , 22 , 37, 100 , 999, 87 , 351 ] #Intializing the given list

prime_numbers = [] #Initializing the new list to store even numbers
for num in org_list:
    flag = True #Initialising the flag
    i = num
    if num == 1 or i == 1: #Validating the number is one and skipping it
        next
    else:
        while i != 2: #Validating the number is not two
           i -=1 #decreasing the the i by 1
           if num % i == 0: #validating the i is divisible by other numbers less than it
               flag = False #if it is divisible then assiging the boolean to false        
               break  #breaking the loop to avoid unwanted iterartion
        if flag == True: #boolean will be same as intialized value if it is prime number
            prime_numbers.append(num) #adding the prime numbers to the list
        else:
            continue
print("Prime Numbers List:", prime_numbers) #printing the prime number list
