def findDuplicate(nums):
    slow = fast = 0

    while True:
        slow = nums[slow]

        temp = nums[fast]
        fast = nums[temp]

        if slow == fast:
            break
        
    curr = 0
    while slow != curr:
        slow = nums[slow]
        curr = nums[curr]

    return curr

print(findDuplicate([3,1,3,4,2]))