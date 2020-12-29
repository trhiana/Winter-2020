def isPalindrome(s):
    s = s.lower()
    s = s.replace(' ', '')
                
    start = 0
    end = len(s) - 1
    while start < end:
        while not s[start].isalnum() and start < end:
            start += 1
        while not s[end].isalnum() and start < end:
            end -= 1
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

s = 'A man, a plan, a canal: Panama' # True
s1 = 'race a car' # False
s2 = 'Google' # False

print(isPalindrome(s))
print(isPalindrome(s1))
print(isPalindrome(s2))