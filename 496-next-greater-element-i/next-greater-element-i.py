class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        d={}
        for i in range(len(nums2)-1,-1,-1):
            if not st:
                st.append(nums2[i])
                d[nums2[i]]=-1

            else:
                if st[-1]>nums2[i]:
                    d[nums2[i]]=st[-1]
                    st.append(nums2[i])
                else:
                    while st:
                        if st[-1]<=nums2[i]:
                            st.pop()
                        else:
                            d[nums2[i]]=st[-1]
                            st.append(nums2[i])
                            break
                    if not st:
                        st.append(nums2[i])
                        d[nums2[i]]=-1
        for i in range(len(nums1)):
            nums1[i]=d[nums1[i]]
        return nums1


        
        