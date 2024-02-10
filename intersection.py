'''
349. Intersection of two arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''

# # todo myway
# def intersection(nums1, nums2):
#     temp = []
#     for i in nums1:
#         if i in nums2 and i not in temp:
#             temp.append(i)
#     return temp

# todo simple way
def intersection(nums1, nums2):
    return set(nums1).intersection(nums2)

print(intersection([1,2,2,1], [2,2]))