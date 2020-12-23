'''
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''

# With data structure
def isUnique(string):
    unique = []
    for char in string:
        if char in unique:
            return False
        else:
            unique.append(char)
    return True


# Without data structure
def isUniqueWithoutDS(string):
    length = len(string)
    if len(string) > 256:
        return False
    char_set = [False] * 128
    for char in range(length):
        value = ord(string[char])
        if char_set[value]:
            return False
        char_set[value] = True
    return True


a = "abcsd"
b = "12jfbernk23rnl3rk24r"
c = "rhiana"
d = "1234567"

print(isUnique(a)) # True
print(isUnique(b)) # False
print(isUnique(c)) # False
print(isUnique(d)) # True

print(isUniqueWithoutDS(a)) # True
print(isUniqueWithoutDS(b)) # False
print(isUniqueWithoutDS(c)) # False
print(isUniqueWithoutDS(d)) # True