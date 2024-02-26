import re

def spl_upp(s):
    return re.findall('[A-Z][^A-Z]*', s)

user_str = str(input())
res = spl_upp(user_str)
print("Original string:", user_str)
print("Split result:", res)