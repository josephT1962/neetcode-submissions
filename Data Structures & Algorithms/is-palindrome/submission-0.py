class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= "".join(char for char in s if char.isalnum())
        s=s.lower()
        start_loc=0
        end_loc=len(s)-1
        if len(s)%2==0:
            for i in range(len(s)//2):
                if s[start_loc]!=s[end_loc]:
                    return False
                start_loc+=1
                end_loc-=1
            return True

        elif len(s)%2==1:
            for i in range(len(s)//2):
                #print(start_loc)
                #print(end_loc)
                if s[start_loc]!=s[end_loc]:
                    return False
                start_loc+=1
                end_loc-=1
            return True  
