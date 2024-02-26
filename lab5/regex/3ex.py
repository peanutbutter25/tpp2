import re

def find_seq(text):
    pattern = r'\b[a-z]+_[a-z]+\b'
    seq = re.findall(pattern, text)
    return seq

text = "This is a test_text for finding sequences like this_one or that_two."
found_seq = find_seq(text)
print("Found sequences:", found_seq)