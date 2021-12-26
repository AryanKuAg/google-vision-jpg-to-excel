import re

pattern = re.compile('[a-z][a-z]')

name = 'aryan is the best thing 12-May-55the god has ever created'

print(pattern.search(name).group())
