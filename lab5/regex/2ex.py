import re

def match_pat(s):
    pattern = r'^ab{2,3}$'
    if re.match(pattern, s):
        return True
    else:
        return False
test_str = ['a', 'ab', 'abb', 'abbb', 'abbbb', 'b']
for x in test_str:
    print(f"{x}: {match_pat(x)}") 