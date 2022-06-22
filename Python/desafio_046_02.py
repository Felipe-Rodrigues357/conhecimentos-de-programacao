import time

for c in range(10, -1, -1):
    print('\033[1;33m{}\033[m'.format(c))
    time.sleep(1)
print('\033[1;4;31mBOOM\033[m')