# todo using one-pass hash table 

def sum_two(array, target):
    num_dict = {}
    
    for index, number in enumerate(array):
        complement = target - number
        
        if complement in num_dict:
            return [num_dict[complement], index]
        
        num_dict[number] = index
    
    return []

array = [2,4,3,5,7]

print(sum_two(array, 6))

# create an empty hash table/ dictionary
# enumerate array to get index and value
# create a var that calc target - number
# create if statement, if var in hash table
# by returning array (hash table[var], index)
# create if not, then add value to hash table
# by using key as number then the value is the index from array