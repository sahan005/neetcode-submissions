class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        p="".join(sorted(s))
        q="".join(sorted(t))

        if p==q:
            return True
        else:
            return False

        