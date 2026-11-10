class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_list=""
        for i in range(len(strs[0])):
            prefix_list_confirm=0
            for j in range(1,len(strs)):
                if len(strs[0])>len(strs[j]) and i==len(strs[j]):
                    return prefix_list
                if strs[0][i]  == strs[j][i]:
                    prefix_list_confirm+=1
                else:
                    return prefix_list
            if prefix_list_confirm==len(strs)-1:
                prefix_list+=(strs[0][i])
        return prefix_list
