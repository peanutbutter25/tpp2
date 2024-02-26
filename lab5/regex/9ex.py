import re

def ins(txt):
    modified = re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)
    return modified

user_str = str(input())
res = ins(user_str)
print("Original string:", user_str)
print("Modified string:", res)