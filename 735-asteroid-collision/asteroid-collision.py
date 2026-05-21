class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        st=[]
        for i in range(len(arr)):
            if arr[i]>0:
                st.append(arr[i])
            elif arr[i]<0:
                while(st and st[-1]>0 and st[-1]<abs(arr[i])):
                    st.pop()
                if st and st[-1]==abs(arr[i]):
                    st.pop()
                elif not st or st[-1]<0:
                    st.append(arr[i])
        return st

        