org_list = [10, 501, 22, 37, 100, 999, 87, 351] #Intializing the given list

even_numbers = [] #Initializing the new list to store even numbers
odd_numbers = [] #Initializing the new list to store odd numbers

for num in org_list:
    if num % 2 == 0:
        even_numbers.append(num) #appending in even number list
    else:
        odd_numbers.append(num) #appending in odd number list

print("Even Numbers List:", even_numbers) #printing the even number list
print("Odd Numbers List:", odd_numbers) #Printing the odd number list