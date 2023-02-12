import random


def main():
    JockerNm = []
    jockerNm = []
    JNm = []
    for i in range(10000):
        a = BH()
        for x in a:
            Jockernm = a[x].count('🤡')
            jockernm = a[x].count('👻')
            JockerNm.append(Jockernm)
            jockerNm.append(jockernm)
            JNm.append(jockernm+Jockernm)
    lenjnm = len(JNm)
    print("8个王的概率为{}%".format(JNm.count(8)/(lenjnm/100)))
    print("7个王的概率为{}%".format(JNm.count(7)/(lenjnm/100)))
    print("6个王的概率为{}%".format(JNm.count(6)/(lenjnm/100)))
    print("5个王的概率为{}%".format(JNm.count(5)/(lenjnm/100)))
    print("4个王的概率为{}%".format(JNm.count(4)/(lenjnm/100)))
    print("3个王的概率为{}%".format(JNm.count(3)/(lenjnm/100)))
    print("2个王的概率为{}%".format(JNm.count(2)/(lenjnm/100)))
    print("1个王的概率为{}%".format(JNm.count(1)/(lenjnm/100)))
    print("0个王的概率为{}%".format(JNm.count(0)/(lenjnm/100)))


def BH():
    index = [chr(i) for i in range(65, 91)]

    cards = shuffle()
    a = 5
    c = {}
    d = {'J': 11, 'Q': 12, 'K': 13}
    e = {'1': 14, '2': 15}
    for i in range(a):
        b = [cards[i+x*a]
             for x in range(int(len(cards)/a)+1) if i+x*a < len(cards)]
        b = sorted(b, key=lambda i: int(i[3:]) if len(i) > 1 and i[3:].isnumeric() and i[3:] not in e.keys() else
                   d[i[3:]] if i[3:] in d.keys() else e[i[3:]] if i[3:] in e.keys() else 99, reverse=True)
        c[index[i]] = b
    return c


def shuffle():
    suit = ['❤️', '♠️', '♦️', '♣️']
    num = ['1', '2',
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
