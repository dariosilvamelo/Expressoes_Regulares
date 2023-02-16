# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto
import re

# Funções
# findall search sub
# compile

string = 'expressões regulares.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'ABCD', string))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))
