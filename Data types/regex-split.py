import re
text = "Apple,Banana,Cherry,Date"
pattern = r","

split_result = re.split(pattern, text)
print("Split result:", split_result)