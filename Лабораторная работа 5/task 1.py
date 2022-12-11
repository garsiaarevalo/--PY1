# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

for i in [i for i in range(16)]:
    pprint(['bin:',bin(i),'dec:',i,'hex:',hex(i),'oct:',oct(i)])