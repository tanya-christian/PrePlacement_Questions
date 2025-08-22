def findMissingNum(arr):
    missing_num = []
    for i in range(1,101):
        if i not in arr:
            missing_num.append(i)
    print(missing_num)
    
list1=[12,34,67,89]
findMissingNum(list1)

#another way to do it
def findMissingNum(arr):
    number_set = set(arr)
    missing_numbers = [i for i in range(1,101) if i not in number_set]
    return missing_numbers
    
user_input = input("Enter numbers between 1-100, seperated by comma:")
num_list = [int(num.strip()) for num in user_input.split(",")]
    
missing = findMissingNum(num_list)
    
print("Missing Numbers:", missing)
