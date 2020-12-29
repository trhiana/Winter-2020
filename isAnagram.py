def isAnagram(s, t):
    char = dict()
    s = s.replace(' ', '').lower()
    t = t.replace(' ', '').lower()

    if len(s) != len(t):
        return False
    
    for val in s:
        if val in char:
            char[val] += 1
        else:
            char[val] = 1
    
    for val in t:
        if val in char:
            char[val] -= 1
        else:
            char[val] = 1
    
    for val in char:
        if char[val] != 0:
            return False
    
    return True

s, t = 'anagram', 'nagaram' # True
s1, t1 = 'rat', 'car' # False

print(isAnagram(s, t))
print(isAnagram(s1, t1))