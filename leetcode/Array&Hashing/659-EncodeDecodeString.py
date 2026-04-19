
from typing import List

def encode(strs: List[str]) -> str:
    encoded_str = ''
    for word in strs:
        delimiter = str(len(word)) + '#'
        encoded_str += (delimiter + word)
    return encoded_str

# Now String == "4#leet4#code"
def decode(big_str: str) -> List[str]:
    result_array, pointer = [], 0

    # Loop through the string
    while pointer < len(big_str):
        another_pointer = pointer # to get the length and delimiter
        # Check for the delimiter and get the string 
        while big_str[another_pointer] != '#':
            another_pointer += 1
        string_length = int(big_str[pointer:another_pointer]) 
        
        #add the string to the result array
        result_array.append(big_str[another_pointer + 1:another_pointer + 1 + string_length])
        # Increment the pointer for the next word
        pointer = another_pointer + 1 + string_length
    return result_array



if __name__ == '__main__':
    strs = ["leet#", "co#de^"]
    print("Encode String")
    encoded_string = encode(strs)
    print(encoded_string)
    print("======================")
    print("Decoded Array of Strings")
    print(decode(encoded_string))