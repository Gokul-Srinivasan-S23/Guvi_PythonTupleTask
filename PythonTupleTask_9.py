org_list = [10,20,30,9] #intializing the list
spl = 0 #Intializing the variable to Zero
for i in range(0,len(org_list)-1): #looping the list
   if i < len(org_list)-2: #validating the element iteration to add the next three elements
    res = org_list[i]+org_list[i+1]+org_list[i+2] #getting the summ of three elements
   elif i== len(org_list)-2: #validating the element iteration to add the next three elements
    res = org_list[i]+org_list[i+1]+org_list[0] #getting the summ of three elements
    spl = 1 #variable to decide in display
   if res == 59 and spl == 1 : #validation of sum of variable with 59
       print("The Triplet to make sum of 59 is ",org_list[i],",",org_list[i+1],"&",org_list[0]) #display statement
   elif res == 59 and spl != 1:
       print("The Triplet to make sum of 59 is ",org_list[i],",",org_list[i+1],"&",org_list[i+2]) #display statement