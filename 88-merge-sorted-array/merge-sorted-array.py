class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ans=[]
        f=0
        l=0
        while (f<m and l<n):
            if nums1[f]<nums2[l]:
                ans.append(nums1[f])
                f+=1
            elif nums1[f]==nums2[l]:
                ans.append(nums1[f])
                f+=1
                
            else:
                ans.append(nums2[l])
                l+=1
        while(f<m):
            ans.append(nums1[f])
            f+=1
        while(l<n):
            ans.append(nums2[l])
            l+=1
        for i in range(len(ans)):
                nums1[i]=ans[i]


        