# Python program to print positive Numbers in a List
 
# list of numbers
list1 = [3,6,-10,11,-18,2]
num = 0
 
# using while loop    
while(num < len(list1)):
     
    # checking condition
    if list1[num] >= 0:
        print(list1[num], end = "\n")
     
    # increment num
    num += 1
list2=[56,32,-9,-46,98,-33,81]
print([a for j,a in enumerate(list2) if a>=0])

