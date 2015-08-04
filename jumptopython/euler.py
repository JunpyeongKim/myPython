__author__ = '1000938'

# euler.py
# http://projecteuler.net

result = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        # print(i)
        result += i

print("result is %d" % result)