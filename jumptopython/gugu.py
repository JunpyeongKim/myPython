__author__ = 'Junpyeong Kim'

# gugu.py

# result = GuGu(2)


def gugu(n):
    result = []

    i = 1;
    while i < 10:
        result.append(n*i)
        i = i + 1
    return result

print(gugu(2))
