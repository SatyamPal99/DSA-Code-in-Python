class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        new=[]
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]<nums2[j]:
                new.append(nums1[i])
                i+=1
            elif nums1[i]>nums2[j]:
                new.append(nums2[j])
                j+=1
            else:
                new.append(nums2[j])
                i+=1
                
        if i<len(nums1):
            while(i<len(nums1)):
                new.append(nums1[i])
                i+=1
        if j<len(nums2):
            while(j<len(nums2)):
                new.append(nums2[j])
                j+=1

        if len(new)%2==1:
            return new[len(new)//2]
        elif len(new)%2==0:
            first=len(new)//2
            second=first-1
            return (new[first]+new[second])/2
        