class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        l = len(s)
        
        for left in range(l):
            for right in range(left + 1, l + 1):
                substr = s[left:right]
                
                if right == l:
                    c = s[right - 1]
                else:
                    c = s[right]
                
                if c in substr:
                    if len(substr) > max_len:
                        max_len = len(substr)
                    break

        return max_len