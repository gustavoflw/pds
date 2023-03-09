import time
import random
import string

t_start = time.time()

s = string.ascii_letters + '                                                                                                                                                       ' + '>'
print(s)

while time.time() - t_start < 3:
    line = ""
    while len(line) < 100:
        line = line + random.choice(s)
    print(line)
    time.sleep(0.05)
print()