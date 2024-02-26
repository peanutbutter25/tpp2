import re

def rep(txt):
    return txt.replace(' ', ':').replace(',', ':').replace('.', ':')

text = "This is a test, for replacing spaces. And commas, with colons."
res = rep(text)
print("Original text:", text)
print("Modified text:", res)