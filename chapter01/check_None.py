is_empty = None
# print(help(is_empty))

# if is_empty == None:
# isがある
if is_empty is None:
    print('None!!')

# notの場合
if is_empty is not None:
    print('None')


print(1 == True)    # true
print(1 is True)    # false
print(None is None)

# isはNoneのチェックするときのみ