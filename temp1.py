from string import ascii_letters, punctuation, digits
from random import choice

all_chars = ascii_letters + ascii_letters + punctuation + digits + digits
print(all_chars)

x = [choice(all_chars) for i in range(20)]
print(''.join(x))
