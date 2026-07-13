class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3 = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                num3.append(nums1[i])
                i += 1
            else:
                num3.append(nums2[j])
                j += 1

        while i < len(nums1):
            num3.append(nums1[i])
            i += 1

        while j < len(nums2):
            num3.append(nums2[j])
            j += 1

        n = len(num3)

        if n % 2 == 1:
            return num3[n // 2]
        else:
            return (num3[n // 2] + num3[n // 2 - 1]) / 2