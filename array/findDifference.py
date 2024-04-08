'''
2215. Find the Difference of Two Arrays                                                  

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
Explanation:
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

Example 2:

Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
Explanation:
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

'''
     
def findDifference(nums1, nums2):     
    n1 = set(nums1)
    n2 = set(nums2)
    angka = n1.union(n2)
    print(angka)
    
    t = []
    t2 = []
    for k in angka:
        if k in n1 and k not in n2:
            t.append(k)
        elif k not in n1 and k in n2:
            t2.append(k)
            
    return [t, t2]
    
n1 = [1,2,3]
n2 = [2,4,6]
print(findDifference(n1, n2))