"""
 input 関数
"""

while True:
    word = input('Enter:')  # string型で入ってくる
    if word == 'ok':
        break
    num = int(word)         # int型に変更する
    if num == 100:
        break
    print('next')
