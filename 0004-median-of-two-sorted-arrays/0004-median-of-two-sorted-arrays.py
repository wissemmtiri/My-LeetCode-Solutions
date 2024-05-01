class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        elem1, elem2 = 0, 0
        len1, len2 = len(nums1), len(nums2)

        for count in range((len1 + len2) // 2 + 1):
            elem2 = elem1
            if i < len1 and j < len2:
                if nums1[i] > nums2[j]:
                    elem1 = nums2[j]
                    j += 1
                else:
                    elem1 = nums1[i]
                    i += 1
            elif i < len1:
                elem1 = nums1[i]
                i += 1
            else:
                elem1 = nums2[j]
                j += 1

        if (len1 + len2) % 2 == 1:
            return elem1
        else:
            return (elem1 + elem2)/2