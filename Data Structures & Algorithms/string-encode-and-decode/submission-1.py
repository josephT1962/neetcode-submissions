class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str =""
        for i in strs:
            encode_str= encode_str+str(len(i))+"#"+i
        return encode_str
    def decode(self, s: str) -> List[str]:
        decode_strs = []
        str_count = 0
        str_add = ""
        length_str = ""
        reading_length = True

        for j in s:
            if reading_length:
                if j != "#":
                    length_str += j
                else:
                    str_count = int(length_str)
                    length_str = ""
                    reading_length = False

                    if str_count == 0:
                        decode_strs.append("")
                        reading_length = True
            else:
                str_add += j
                str_count -= 1

                if str_count == 0:
                    decode_strs.append(str_add)
                    str_add = ""
                    reading_length = True
        return decode_strs