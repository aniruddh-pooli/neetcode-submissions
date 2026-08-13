class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        maxl=0
        chars=set()
        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left+=1
            chars.add(s[right])
            maxl=max(maxl,right-left+1)

        return maxl
        