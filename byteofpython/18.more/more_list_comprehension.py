# encoding=utf-8

# more_list_comprehension.py

# 18.5 List Comprehension
#   - to derive a new list from an existing list.
#   - the original list remains unmodified.
#   - advantage : reduce the amount of boilerplate code

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print listtwo
