s = "abca"
def is_palindrome(l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


start, end = 0, len(s) - 1
while start < end:
    if s[start] != s[end]:
        res = is_palindrome(start + 1, end) or is_palindrome(start, end - 1)
    start += 1
    end -= 1

print(res)