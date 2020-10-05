class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m-=1
        n-=1
        while m>=0 and n>=0:
            if nums1[m]>nums2[n]:
                nums1[m+n+1]=nums1[m]
                m-=1
            else:
                nums1[m+n+1]=nums2[n]
                n-=1
        while n>=0:
            nums1[n]=nums2[n]
            n-=1