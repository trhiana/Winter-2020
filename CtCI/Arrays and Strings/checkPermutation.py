'''
Given two strings, write a method to decide if one is a permutation of the other.
'''

def checkPermutation(string1, string2):
    string1 = sorted(string1)
    string2 = sorted(string2)

    if len(string1) != len(string2):
        return False
    
    length = len(string1)

    for i in range(length):
        if string1[i] != string2[i]:
            return False
    
    return True

s1 = 'google'
s2 = 'ogogle'

s3 = 'toggle'
s4 = 'gotle'
print(checkPermutation(s1, s2))
print(checkPermutation(s3, s4))