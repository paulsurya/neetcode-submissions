class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "@" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '@':
                j += 1
            
            length_of_str = int(s[i:j])
            start_of_str = j+1
            end_of_str = start_of_str + length_of_str

            decoded_string.append(s[start_of_str:end_of_str])

            i = end_of_str
        return decoded_string
