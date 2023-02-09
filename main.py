import random

def main():
    JockerNm = []
    jockerNm = []
    JNm=[]
    for i in range(10000):
        a = BH()
        for x in a:
            JockerNm.append(a[x].count('🤡'))
            jockerNm.append(a[x].count('👻'))
            JNm.append(a[x].count('🤡')+a[x].count('👻'))
    # print(JockerNm)
    # print(jockerNm)
    # print(JNm)
    print("8个王的概率为{}%".format(JNm.count(8)/500))
    print("7个王的概率为{}%".format(JNm.count(7)/500))
    print("6个王的概率为{}%".format(JNm.count(6)/500))
    print("5个王的概率为{}%".format(JNm.count(5)/500))
    print("4个王的概率为{}%".format(JNm.count(4)/500))
    print("3个王的概率为{}%".format(JNm.count(3)/500))
    print("2个王的概率为{}%".format(JNm.count(2)/500))
    print("1个王的概率为{}%".format(JNm.count(1)/500))
    print("0个王的概率为{}%".format(JNm.count(0)/500))


def BH():
    # cards = shuffle()
    index = [chr(i) for i in range(65, 91)]
    # print(cards)

    # 发牌
    # a = int(input("请输入参与人数："))
    # c = int(input("请输入牌数："))
    # a = 6
    # c = 3
    # for i in range(a):
    #     b = [cards[i + x*a] for x in range(c)]
    #     print(index[i] + ": " + str(b))

    # 保皇
    cards = shuffle()*4
    random.shuffle(cards)
    # print(cards)
    a = 5
    c = {}
    for i in range(a):
        b = [cards[i+x*a]
             for x in range(int(len(cards)/a)+1) if i+x*a < len(cards)]
        d = {'J': 11, 'Q': 12, 'K': 13}
        e = {'1':14,'2':15}
        b = sorted(b, key=lambda i: int(i[3:]) if len(i) > 1 and i[3:].isnumeric() and i[3:] not in e.keys() else 
        d[i[3:]] if i[3:] in d.keys() else e[i[3:]] if i[3:] in e.keys() else 99, reverse=True)
        c[index[i]] = b
    # for x in c:
        # print(x,c[x])
    return c
        


def shuffle():
    suit = ['❤️', '♠️', '♦️', '♣️']
    num = ['1', '2', 
    # 保皇去掉
    # '3', '4', '5', 
    '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    jocker = ['🤡', '👻']
    lensuit = len(suit)
    lennum = len(num)
    total = lensuit*lennum
    cards = []
    while len(cards) < total:
        i1 = random.randint(0, lensuit-1)
        i2 = random.randint(0, lennum-1)
        card = suit[i1] + ' ' + num[i2]
        if card not in cards:
            cards.append(card)
    i3 = random.randint(0, total)
    cards.insert(i3, jocker[0])
    i4 = random.randint(0, total+1)
    cards.insert(i4, jocker[1])
    return cards


if __name__ == "__main__":
    main()
