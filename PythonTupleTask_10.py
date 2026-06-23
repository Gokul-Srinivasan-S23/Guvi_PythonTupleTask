org_list = [4,2,-3,1,6] #Initializing the list
final_list = [] #empty list to store the sub list
for i in range(0,len(org_list)-1): #looping through first iteration on each element
    final_list.clear() #clearing the final list
    summ = 0 # intializing the variable to store the sum
    for j in range(i,len(org_list)-1): #looping through the org list
        summ += org_list[j] #adding and storing in the sum
        final_list.append(org_list[j]) #appending in sub list
        if summ == 0: #valdiating the sum of appended elements
            print("The sublist is ",final_list) #display statement