list1= [1,2,3,4,5,6] #Intialaizing the list
list2= [4,5,6,7,8,9] #Intialaizing the list
list3= [7,8,9,10,11] #Intialaizing the list

list4 = list1+list2+list3 #concatenating the list
list5 = [] #Initializing the list to save the unique element
duplicate_list = [] #Initializingthe list to save the duplicate element
for num in list4:#Looping the concatenated list
    if num in list5:#Validating the duplicate element
        duplicate_list.append(num) #adding the duplicate to the list
        continue
    list5.append(num)#appending to the unique list element
    
print("The duplicate numbers in the list are ",duplicate_list)#printing the duplicate list