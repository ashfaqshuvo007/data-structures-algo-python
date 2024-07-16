'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''

# import re
def isAlphaNumeric(self, c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

def isPalindrome(self, s: str) -> bool:
    # ============= APPROACH 3 =======================
    # NOT USING ANY LIBRARY FUNCTION AND MEMORY

    start = 0
    end = len(s) - 1

    # Check if the cleaned string is a palindrome
    while start < end:
        while start < end and not self.isAlphaNumeric(s[start]):
            start += 1
        while end > start and not self.isAlphaNumeric(s[end]):
            end -= 1

        if s[start].lower() != s[end].lower():
            return False

        start += 1
        end -= 1

    return True


    # ============= APPROACH 2 =======================
    #  FASTER BUT USES EXTRA MEMORY SPACES
        # Remove non-alphanumeric characters and convert to lowercase
    # working_string = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    
    # start = 0
    # end = len(working_string) - 1

    # # Check if the cleaned string is a palindrome
    # while start < end:
    #     if working_string[start] != working_string[end]:
    #         return False
    #     start += 1
    #     end -= 1

    # return True

    # ============ TRIAL 1 ================
    # working_string = re.sub(r'[^a-zA-Z0-9]','',s.lower())
    # isPalinDrome = False
    # start = 0
    # end = len(working_string) - 1

    # if (working_string != "" and len(working_string) > 1):
    #     while(start < end):
    #         if (working_string[start] == working_string[end]):
    #             isPalinDrome = True
    #         else:
    #             isPalinDrome = False
    #         start += 1
    #         end -= 1
    # else:
    #     isPalinDrome = True

    # return isPalinDrome


        
       