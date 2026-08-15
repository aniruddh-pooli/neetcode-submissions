from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        q = deque()

        for i in range(len(nums)):

            # Remove indices that are outside the window
            while q and q[0] <= i - k:
                q.popleft()

            # Remove smaller elements from the back
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            # Add current index
            q.append(i)

            # Start adding answers once the first window is complete
            if i >= k - 1:
                out.append(nums[q[0]])

        return out