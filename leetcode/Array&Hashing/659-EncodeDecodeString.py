
from typing import List

def encode(strs: List[str]) -> str:
    encoded_str = ''
    for word in strs:
        encoded_str += str(len(word)) + '#' + word
    return encoded_str

# Now String == "4#leet4#code"
def decode(big_str: str) -> List[str]:
    result_array, i = [], 0

    # Loop through the string
    while i < len(big_str):
        j = i
        #Find the delimiter
        while big_str[j] != "#":
            j += 1
        print(big_str[i:j])
        length = int(big_str[i:j])
        # Update pointers
        i = j + 1
        j = i + length
        # Apend to result
        result_array.append(big_str[i:j])
        # Update pointer
        i = j
        
    return result_array



if __name__ == '__main__':
    strs = ["leet", "code"]
    print("Encode String")
    encoded_string = encode(strs)
    print(encoded_string)
    print("======================")
    print("Decoded Array of Strings")
    print(decode(encoded_string))