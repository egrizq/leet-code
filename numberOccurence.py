def numberOccurence(arr):
    # temp = {}
    
    # for i in arr:
    #     if i not in temp:
    #         temp[i] = 1
    #     else:
    #         temp[i] += 1
    
    # return len(set(temp.values())) == len(temp)
    temp = []
    for i in set(arr):
        temp.append(arr.count(i))
    return len(temp) == len(set(temp))
    
print(numberOccurence([1,2,1]))