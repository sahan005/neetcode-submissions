class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest=0
        sett=set()

        for r in range(0, len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l=l+1
            
            w=r-l+1
            longest=max(longest, w)
            sett.add(s[r])
            

        return longest


            

        