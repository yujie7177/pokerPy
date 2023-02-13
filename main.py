import random
from openpyxl import Workbook , load_workbook


def main():
    num = ['_Jocker',  '_J', '_j', '2', 'A',
           'K', 'Q', 'J', '10', '9', '8', '7', '6']
    wb = load_workbook('output.xlsx')
    sheet = wb['Sheet1']
    for nm in num:
        exec('count' + nm + '=[]')
    for i in range(10000):
        a = BH()
        for i in a:
            c = [x[3:] if len(x) > 3 else x for x in a[i]]
            for b in num:
                if '_' not in b:
                    exec('count' + b + ".append(c.count('{}'))".format(b))
            jnm = c.count('👻')
            Jnm = c.count('🤡')
            exec('count_j.append({})'.format(jnm))
            exec('count_J.append({})'.format(Jnm))
            exec('count_Jocker.append({})'.format(jnm + Jnm))

    for d in num:
        gg = 67
        g = chr(gg)
        for y in range(17):
            exec("gl = count{}.count(y)/(len(count{})/100)".format(d, d))
            if '_' not in d:
                exec("print('{}个{}的概率为'+str(gl)+'%')".format(str(y), d))
            elif d == '_j':
                exec("print('{}个{}的概率为'+str(gl)+'%')".format(str(y), '小王'))
            elif d == '_J':
                exec("print('{}个{}的概率为'+str(gl)+'%')".format(str(y), '大王'))
            else:
                exec("print('{}个{}的概率为'+str(gl)+'%')".format(str(y), '王'))
            


def BH():
    index = [chr(i) for i in range(65, 91)]

    cards = shuffle()
    a = 5
    c = {}
    d = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    e = {'2': 15}
    for i in range(a):
        b = [cards[i+x*a]
             for x in range(int(len(cards)/a)+1) if i+x*a < len(cards)]
        b = sorted(b, key=lambda i: int(i[3:]) if len(i) > 1 and i[3:].isnumeric() and i[3:] not in e.keys() else
                   d[i[3:]] if i[3:] in d.keys() else e[i[3:]] if i[3:] in e.keys() else 99, reverse=True)
        c[index[i]] = b
    return c


def shuffle():
    suit = ['❤️', '♠️', '♦️', '♣️']
    num = ['A', '2',
           # 保皇去掉
           # '3', '4', '5',
           '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    jocker = ['🤡', '👻']
    cards = [x + ' ' + y for x in suit for y in num]
    cards = cards + jocker
    # 保皇
    cards = cards*4
    random.shuffle(cards)

    return cards


if __name__ == "__main__":
    main()
