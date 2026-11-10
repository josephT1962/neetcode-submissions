class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list={}
        for i in strs:
            key = "".join(sorted(i))
            if key not in dict_list:
                dict_list[key]=[]
            dict_list[key].append(i)
        #print(dict_list)
        return list(dict_list.values())