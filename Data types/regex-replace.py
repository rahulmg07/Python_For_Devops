import re
text = "The quick brown fox jumps over the lazy brown dog"
patter = r"brown"
replacement = "red"

new_text = re.sub(patter, replacement, text)
print("Modified text:", new_text)