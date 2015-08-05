__author__ = 'Junpyeong Kim'

# euler.py
# Multiples of 3 and 5
# - list and sum all the natural numbers below 10 or 1000
# - http://projecteuler.net

result = 0
result_array = []
for i in range(1, 10):
    if i % 3 == 0 or i % 5 == 0:
        # print(i)
        result_array.append(i)
        result += i

print("result is %d" % result)
print("the array result is %s" % result_array)
