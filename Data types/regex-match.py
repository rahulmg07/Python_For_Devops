import re
text = "The quick brown fox jumps over the lazy dog"
patter = r"quick"
match = re.match(patter, text)
if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found")