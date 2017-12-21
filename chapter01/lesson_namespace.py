"""
namespace & scope comment
 - name_space function dose not load global x
"""

x = "dog"


def name_space():
    # print(x)  globalのxは呼べない
    x = "cat"
    print("local:", x)
    print("locals():", locals())


name_space()
print("global:", x)
print("globals():", globals())
