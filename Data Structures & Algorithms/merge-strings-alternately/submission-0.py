class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combine_word=""
        if len(word1)>len(word2):
            for i in range(len(word2)):
                #print(combine_word)                
                if i<=len(word2):
                    combine_word+=word1[i]+word2[i]
                if i+1==len(word2):
                    #print(combine_word)                    
                    combine_word+=word1[i+1::]
        elif len(word1)<len(word2):
            for i in range(len(word1)):
                if i<len(word1):
                    combine_word+=word1[i]
                    combine_word+=word2[i]
                if i+1==len(word1):
                    combine_word+=word2[i+1::]
        else:
            for i in range(len(word1)):
                combine_word+=word1[i]+word2[i]          
        return combine_word