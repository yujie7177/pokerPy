import random


def main():
    cards = shuffle()
    index = [chr(i) for i in range(65, 91)]
    print(cards)
    # a = int(input("请输入参与人数："))
    # c = int(input("请输入牌数："))
    a = 6
    c = 3

    for i in range(a):
        b = [cards[i + x*a] for x in range(c)]
        print(index[i] + ": " + str(b))


def shuffle():
    suit = ['❤️', '♠️', '♦️', '♣️']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    jocker = ['🤡', '👻']
    cards = []
    while len(cards) < 52:
        i1 = random.randint(0, 3)
        i2 = random.randint(0, 12)
        card = suit[i1] + ' ' + num[i2]
        if card not in cards:
            cards.append(card)
    i3 = random.randint(0, 52)
    cards.insert(i3, jocker[0])
    i4 = random.randint(0, 53)
    cards.insert(i4, jocker[1])
    return cards


if __name__ == "__main__":
    main()
