"""
    コマンドライン引数

$ python sys.py option1
output ['sys.py', 'option1']
"""

import sys

print(sys.argv)

# use
for i in sys.argv:
    print(i)
