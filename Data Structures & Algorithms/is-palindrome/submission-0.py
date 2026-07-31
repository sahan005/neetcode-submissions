class Solution:
    def isPalindrome(self, s: str) -> bool:
        check="".join(c for c in s if c.isalnum())
        check=check.lower()
        p=0
        q=len(check)-1
        
        while q>p:
            if check[p]!=check[q]:
                return False
            q=q-1
            p=p+1
        return True