count = 0

while count < 6:
    print(count)
    count += 1

# count 忘れると無限ループ

count2 = 0

while True:
    if count2 >= 5:
        break   # whileから抜ける

    if count2 == 2:
        count2 += 1
        continue    # printが出ずに次にいく. skip

    print(count2)
    count2 += 1


count3 = 0

while count3 < 5:
    print(count3)
    count3 += 1
else:
    print('Done')

# while ループが終わったらprint('Done')に行く


count4 = 0

while count4 < 5:
    if count4 == 1:
        break
    print(count4)
    count4 += 1
else:
    print('Done')

# breakしたらprint('Done')は実行されない
# while自体を抜ける
