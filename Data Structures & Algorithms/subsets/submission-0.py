class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        end=[]
        def helper(start,temp,end):
            end.append(temp)
            for i in range(start,len(nums)):
                helper(i+1,temp+[nums[i]],end)
        helper(0,[],end)
        return end