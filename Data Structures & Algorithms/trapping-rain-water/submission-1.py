class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        if n<1:
            return 0 
        ans=0
        leftm=[0]*n
        rightm=[0]*n
        leftm[0]=height[0]
        rightm[-1]=height[-1]     
        for i in range(1,n):
            leftm[i]=max(leftm[i-1],height[i])   
        for i in range(n-2,-1,-1):
            rightm[i]=max(rightm[i+1],height[i])
        for i in range(n):
            ans+= min(leftm[i],rightm[i])-height[i]

        return ans