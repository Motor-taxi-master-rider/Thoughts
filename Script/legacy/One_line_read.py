import re

print (sum([int(a) for a in re.findall('[0-9]+',open(r'F:\How to be a good qingnian\Learn\Python\regex_sum_304579.txt').read())]))
