class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        # Characters we need
        need = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        # Characters currently inside the window
        window = {}

        left = 0
        have = 0
        need_count = len(t)

        result = ""
        result_length = float("inf")

        for right in range(len(s)):

            # Add s[right] to the window
            c = s[right]
            window[c] = window.get(c, 0) + 1

            # This character is useful
            if c in need and window[c] <= need[c]:
                have += 1

            # We have everything we need
            while have == need_count:

                # Save the smallest window
                if right - left + 1 < result_length:
                    result = s[left:right + 1]
                    result_length = right - left + 1

                # Remove s[left] from the window
                left_char = s[left]
                window[left_char] -= 1

                # If we removed something we actually needed,
                # the window is no longer valid
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        return result