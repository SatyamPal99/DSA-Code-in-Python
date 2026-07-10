class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Bruteforce
        """maxlen=0
        for i in range(len(fruits)):
            mapp=set()
            for j in range(i,len(fruits)):
                mapp.add(fruits[j])
                if len(mapp)<=2:
                    maxlen=max(maxlen,j-i+1)
                else:
                    break
        return maxlen"""


        # better
        mapp={}
        l=0
        r=0
        maxlen=0
        while(r<len(fruits)):
            mapp[fruits[r]]=mapp.get(fruits[r],0)+1
            while len(mapp)>2:
                mapp[fruits[l]]-=1
                if mapp[fruits[l]]==0:
                    del mapp[fruits[l]]
                l+=1
            maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen

        # Optimal...

