import re

def match_pat(s):
    pattern = r'^ab*$'
    if re.match(pattern, s):
        return True
    else:
        return False

test_str = ['a', 'ab', 'abb', 'abbbb', 'b', 'bbb']
for test in test_str:
    print(f"{test}: {match_pat(test)}")