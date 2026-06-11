class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """i=0
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
            return (new[first]+new[second])/2"""

        # Space Optimized code ...
        """n=len(nums1)+len(nums2)
        idx2=n//2
        idx1=idx2-1
        i=0
        j=0
        count=0
        ele1=-1
        ele2=-1
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]<nums2[j]:
                if count==idx1:
                    ele1=nums1[i]
                if count==idx2:
                    ele2=nums1[i]
                count+=1
                i+=1
            elif nums1[i]>nums2[j]:
                if count==idx2:
                    ele2=nums2[j]
                if count==idx1:
                    ele1=nums2[j]
                count+=1
                j+=1
            else:
                if count==idx1:
                    ele1=nums1[i]
                if count==idx2:
                    ele2=nums1[i]
                count+=1
                i+=1
        
        while(i<len(nums1)):
            if count==idx1:
                ele1=nums1[i]
            if count==idx2:
                ele2=nums1[i]
            count+=1
            i+=1

        while(j<len(nums2)):
            if count==idx1:
                ele1=nums2[j]
            if count==idx2:
                ele2=nums2[j]
            count+=1
            j+=1
        if n%2==0:
            return (ele1+ele2)/2
        else:
            return ele2"""

        # Optimized code....
        n1=len(nums1)
        n2=len(nums2)
        if n1>n2:
            return self.findMedianSortedArrays(nums2,nums1)
        low=0
        high=n1
        left=(n1+n2+1)//2   
        n=n1+n2
        while(low<=high):
            mid1=(low+high)//2
            mid2=left-mid1
            l1=l2=-(math.inf)
            r1=r2=math.inf
            if mid1<n1:
                r1=nums1[mid1]
            if mid2<n2:
                r2=nums2[mid2]
            if mid1-1>=0:
                l1=nums1[mid1-1]
            if mid2-1>=0:
                l2=nums2[mid2-1]
            if l1<=r2 and l2<=r1:
                if n%2==1:
                    return max(l1,l2)
                return (max(l1,l2)+min(r1,r2))/2
            elif l1>r2:
                high=mid1-1
            else:
                low=mid1+1
        return 0
                

        