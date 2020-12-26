'''
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
The palindrome does not need to be limited to just dictionary words.
'''

def palindromePermutation(string):
    count = 0
    char = dict()
    string = string.lower()
    string = string.replace(' ', '')

    for val in string:
        if val in char:
            char[val] += 1
        else:
            char[val] = 1
    
    for 


n = "Tact Coa"
print(palindromePermutation(n))