class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str =""
        for i in strs:
            encode_str= encode_str+str(len(i))+i
        return encode_str
    def decode(self, s: str) -> List[str]:
        print(s)
        decode_strs=[]
        str_count = 0
        str_add=""
        for j in s:
            if decode_strs==[] and str_count==0:
                str_count=int(j)
            elif decode_strs==[] and str_count!=0:
                str_add+=j
                str_count-=1
            elif decode_strs!=[] and str_count==0:
                str_count=int(j)
            elif decode_strs!=[] and str_count!=0:
                str_add+=j
                str_count-=1
            if str_count==0:
                decode_strs.append(str_add)
                str_add=""
        return decode_strs