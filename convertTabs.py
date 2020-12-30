'''
Implement a function that, given a piece of code and a positive integer 
x will turn each tabulation character in code into x whitespace characters.
'''

def convertTabs(code, x):
    return code.replace('\t', ' ' * x)

code, x = '\treturn False', 4 # '    return False'
code1, x1 = '    for x in range(20)', 16 # '    for x in range(20)'
code2, x2 = '\tyield\t', 7 # '       yield       '

print(convertTabs(code, x))
print(convertTabs(code1, x1))
print(convertTabs(code2, x2))