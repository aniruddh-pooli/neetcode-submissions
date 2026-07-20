class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        for i in range(n+1):
            count=0
            x=i
            while x:
                if x&1==1:
                    count+=1
                x>>=1
            ans.append(count)
        return ans