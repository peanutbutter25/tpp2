import re

def find_seq(txt):
    pattern = r'\b[A-Z][a-z]+\b'
    seq = re.findall(pattern, txt)
    return seq

text = "This is a Test string With Multiple Sequences Like This One and That Two"
found_seq = find_seq(text)
print("Found sequences:", found_seq)