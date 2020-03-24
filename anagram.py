import random as r


def anagram(number, strlist):
    i = 0
    f = open('../p.txt', 'w')
    while i < 100:
        r.shuffle(strlist)
        str2 = ''.join(strlist)
        f.write(str2[:number] + '\n')
        i += 1
    f.close()


n = int(input())
str1 = list(input())
anagram(n, str1)
