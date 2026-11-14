class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        changed_loc=0
        for i in range(len(s)-1,0,-1):
            if i!=changed_loc:
                og_loc=s[changed_loc]
                s[changed_loc]=s[i]
                s[i]=og_loc
                changed_loc+=1
            if i== changed_loc:
                break