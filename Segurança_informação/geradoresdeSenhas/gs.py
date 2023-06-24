import random
import string

size = 16

chars = string.ascii_letters + string.digits + 'ç!@#$%¬&*¨||()_+=,.;:></\|[]{}´`~^_?-'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(size)))