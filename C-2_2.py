alphbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

number = int(input('番号＞ '))
if number >= 27:
    number = number // 27 + number % 27

print(alphbet[number-1])
