import keyword
s="functools"
if keyword.iskeyword(s):
    print(s+"yes")
else:
    print(s+"no")
    