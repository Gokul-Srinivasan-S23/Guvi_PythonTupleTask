sort_list = [7,8,1,2,3,4,5,6,] #Intializing the list
leng = len(sort_list) #finding the lenght of the list
mid = leng//2 #findign the mid element index
if sort_list[mid] < sort_list[-1]: #finding the right side is properly sorted or not
    sort_list = sort_list[:mid]#making the list on the left side alone
    print("The minimum element in the list is ",min(sort_list)) #display statement with min function to find the minimum element
elif sort_list[mid] > sort_list[-1]: #finding the left side is properly sorted or not
    sort_list = sort_list[mid:] #making the list on the right side alone
    print("The minimum element in the list is ",min(sort_list)) #display statement with min function to find the minimum element
