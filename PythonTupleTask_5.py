coins = [1, 2, 5, 10] #Intializign the list
target = 10 #initializing the target

print("Combinations to make rs.10:")

# Nested loops to find coin counts
for i in range(target // 1 + 1):
    for j in range(target // 2 + 1):
        for k in range(target // 5 + 1):
            for l in range(target // 10 + 1):
                
                # Check if the total equals the target
                if (i*1 + j*2 + k*5 + l*10) == target:
                    # Multiply the coin by its count and combine them into a single list
                    combination = ([coins[0]] * i + 
                                   [coins[1]] * j + 
                                   [coins[2]] * k + 
                                   [coins[3]] * l)
                    print(combination)
