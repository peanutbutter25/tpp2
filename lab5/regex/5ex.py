import re

def match_pat(s):
    pattern = r'^a.*b$'
    if re.match(pattern, s):
        return True
    else:
        return False

strr = ['ab', 'acd', 'axxxxxb', 'a_b', 'a', 'b']
for x in strr:
    print(f"{x}: {match_pat(x)}")