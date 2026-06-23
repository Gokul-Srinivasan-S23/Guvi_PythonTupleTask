def calculate_happynumber(num1):
    num2 = str(num1)

    while int(num2) > 9:
        num2 = sqauring_number(num2)
        return num2
def sqauring_number(num3):
    num4 = str(num3)
    num5 =0
    for j in range(len(num4)):
        num5 += int(num4[j]) ** 2
    return num5

org_list = [10, 501, 22, 37, 100, 999, 87, 351,40,999]  #Intializing the given list
happy_list = []
for num in org_list:
    fi = calculate_happynumber(num)
    if fi == 1:
        happy_list.append(num)
    else:
        continue
print(happy_list)