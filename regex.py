import re

pattern = "^abc"

x = "abcdef"

match = re.match(pattern,x)
print(match)

a = "i like going to the GYM"

replace = re.sub('like','love',a)
print(replace)

b = "what do u want"
search = re.search(b,'what')
print(search)