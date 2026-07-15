class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for i in range(len(s)):
            seen = set()
            count = 0

            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    count += 1
                    max_len = max(max_len, count)
                else:
                    break

        return max_len